import datetime, hashlib, json, os, pathlib, shutil, subprocess, sys
base = pathlib.Path(__file__).resolve().parent
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, value): p.write_text(json.dumps(value, indent=2)+'\n', encoding='utf-8')
env = dict(os.environ)
removed = sorted(k for k in env if k.startswith(('CODEX_', 'OPENAI_')))
for k in removed: env.pop(k)
env.update(GIT_CONFIG_COUNT='1', GIT_CONFIG_KEY_0='http.sslBackend', GIT_CONFIG_VALUE_0='openssl', GIT_TERMINAL_PROMPT='0')
codex = shutil.which('codex')
def capture(args):
    start=now(); p=subprocess.run(args, env=env, capture_output=True)
    return {'command':args, 'start_utc':start,'end_utc':now(),'exit_code':p.returncode,'stdout':p.stdout.decode('utf-8',errors='replace'),'stderr':p.stderr.decode('utf-8',errors='replace')}
def ref(): return capture(['git','ls-remote','https://github.com/aransoul-project/aransoul.git','refs/heads/main'])
if sys.argv[1]=='preflight':
    result={'utc':now(),'version':capture([codex,'--version']),'auth':capture([codex,'login','status']), 'persisted_sessions_directory_readable':(pathlib.Path.home()/'.codex'/'sessions').is_dir(),'removed_inherited_environment_names':removed,'main':ref(),'agent_sessions_started':0}
    save(base/'preflight.json',result)
    print(json.dumps(result)); sys.exit(0)
name=sys.argv[1]
assert name in ['task-5841','task-9276']
root=base/name
record=base/('record-'+name)
record.mkdir(exist_ok=False)
manifest=json.loads((base/'frozen-manifest.json').read_text())
for path,sha in manifest['sessions'][name]['files'].items(): assert digest(root/path)==sha,path
config={'approval_policy':'never','sandbox_workspace_write.network_access':True,'web_search':'disabled','model_reasoning_effort':'medium','tool_output_token_limit':30000,'features.skip_host_skill_discovery':True,'features.shell_tool':True,'features.unified_exec':True,'features.code_mode_host':True,'windows.sandbox':'elevated','projects.'+json.dumps(str(root))+'.trust_level':'trusted'}
for f in ['plugins','apps','memories','multi_agent','multi_agent_v2','hooks','browser_use','computer_use','in_app_browser','code_mode','workspace_dependencies','image_generation','skill_search']: config['features.'+f]=False
args=[]
for k,v in config.items(): args+=['-c',k+'='+json.dumps(v)]
cmd=[codex,'exec','--ignore-user-config','--strict-config','--json','--color','never','--sandbox','workspace-write','--model','gpt-6-astra','--cd',str(root),'--output-last-message',str(record/'final.txt'),*args,'-']
meta={'start_utc':now(),'command':cmd,'config':config,'removed_inherited_environment_names':removed,'auth':'Existing saved ChatGPT login; no API key supplied','agent_version':capture([codex,'--version']),'model_requested':'gpt-6-astra','model_backend_snapshot':'unknown','scope':'Fresh CLI process and separate directory; no resumed/forked history; shared host, not an OS container','design_sha256':digest(base/'design-before-run.md'),'manifest_sha256':digest(base/'frozen-manifest.json'),'runner_sha256':digest(pathlib.Path(__file__)),'main_before':ref()}
save(record/'environment.json',meta)
assert meta['main_before']['exit_code']==0 and meta['main_before']['stdout'].split()[0]==manifest['actual_commit'], 'main changed or unavailable before launch: NOT RUN'
with (record/'trace.jsonl').open('wb') as out, (record/'stderr.txt').open('wb') as err:
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=out,stderr=err,env=env,cwd=root)
    proc.communicate((root/'task.txt').read_bytes())
meta.update(end_utc=now(),process_exit_code=proc.returncode,main_after=ref(),material_hashes_after={p:digest(root/p) for p in manifest['sessions'][name]['files']})
events=[json.loads(line) for line in (record/'trace.jsonl').read_text(encoding='utf-8').splitlines()]
meta['session_id']=next((e['thread_id'] for e in events if e.get('type')=='thread.started'),None)
if meta['session_id']:
    matches=[p for p in (pathlib.Path.home()/'.codex'/'sessions').rglob('*'+meta['session_id']+'*') if p.is_file() and p.suffix=='.jsonl']
    meta['rollout_matches']=len(matches)
    if len(matches)==1:
        shutil.copyfile(matches[0],record/'private-rollout.jsonl')
        meta['full_rollout_captured']=True
save(record/'environment.json',meta)
print(json.dumps({'session':name,'id':meta['session_id'],'exit':proc.returncode,'full_rollout_captured':meta.get('full_rollout_captured',False),'end_utc':meta['end_utc']}))
