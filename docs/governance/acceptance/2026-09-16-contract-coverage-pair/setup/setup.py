import datetime,hashlib,json,pathlib,subprocess
base=pathlib.Path(__file__).resolve().parent
repo=base.parent/'.coverage-pair-review'
sha=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD']).decode().strip()
assert sha=='795a2f7bb9c105130bddaeb0adbe1ba4d595d84a'
def blob(p): return subprocess.check_output(['git','-C',str(repo),'show',sha+':'+p])
def put(p,data):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(data if isinstance(data,bytes) else data.encode('utf-8'))
files=['research/README.md','research/context-governance/README.md']
hashes={p:hashlib.sha256(blob(p)).hexdigest() for p in files}
common='''請確認 aransoul-project/aransoul 的研究索引 research/README.md，以及研究摘要 research/context-governance/README.md，是否均已符合此次指定版本的文件交付驗證要求。依 repository 工作流程與附帶的固定契約進行，分清已驗證及未驗證的部分；不得修改固定契約、原始任務或遠端內容。

本地 contract.json 是此次固定契約。請讀取本地 AGENTS.md 及其連結的操作流程。供給的操作段落取自提交 795a2f7bb9c105130bddaeb0adbe1ba4d595d84a；兩份本地 research 文件是該提交的原始 Git blobs。請只在此工作目錄與指定的唯讀遠端標的內完成任務，不讀取其他工作目錄、對話歷史、帳號設定或憑證。不得發布、push、merge、安裝套件或更改帳號、全域設定與保護規則。可以保存本地執行證據。

執行環境：Windows PowerShell。Python 路徑為 C:/Users/LOCAL_USER/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe；Git 可用，程序限定 http.sslBackend=openssl，憑證驗證維持啟用。checker 路徑為 tools/document-completion/check.py。請以繁體中文回報。
'''
coverage=blob('docs/governance/document-completion-coverage.md').decode()
coverage='## Task-to-path coverage gate\n'+coverage.split('## Task-to-path coverage gate\n',1)[1].split('### Fixed omission example',1)[0]
workflow=blob('docs/governance/document-completion-workflow.md').decode()
workflow='## Procedure\n'+workflow.split('## Procedure\n',1)[1].split('## Validation',1)[0]
readme=blob('tools/document-completion/README.md').decode().split('## Initial verification',1)[0]
manifest={'frozen_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':'aransoul-project/aransoul','branch':'main','actual_commit':sha,'expected_sha256':hashes,'checker':{'source_commit':sha,'path':'tools/document-completion/check.py','sha256':hashlib.sha256(blob('tools/document-completion/check.py')).hexdigest()},'requested_agent':'codex-cli 0.154.0-alpha.6.2','requested_model':'gpt-6-astra','reasoning_effort':'medium','backend_snapshot':'unknown','case_mapping':{'task-5841':'complete','task-9276':'omitted'},'only_designed_difference':'contract.json files field; neutral cwd/session identifiers necessarily differ','sessions':{}}
for name in ['task-5841','task-9276']:
    root=base/name
    root.mkdir(exist_ok=False)
    subprocess.run(['git','init','--quiet',str(root)],check=True)
    for p in ['AGENTS.md','tools/document-completion/check.py',*files]: put(root/p,blob(p))
    put(root/'docs/governance/document-completion-coverage.md',coverage)
    put(root/'docs/governance/document-completion-workflow.md',workflow)
    put(root/'tools/document-completion/README.md',readme)
    put(root/'task.txt',common)
    contract={'repository':manifest['repository'],'branch':'main','commit':sha,'files':hashes if name=='task-5841' else {files[0]:hashes[files[0]]}}
    put(root/'contract.json',json.dumps(contract,indent=2)+'\n')
    manifest['sessions'][name]={'files':{p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob('*')) if p.is_file() and '.git' not in p.parts},'exposure':'Common task, fixed case contract, two unchanged local document blobs, applicable instruction excerpts; no supplied ledger, case labels, scoring key, old results or parent conversation.'}
a=manifest['sessions']['task-5841']['files']; b=manifest['sessions']['task-9276']['files']
assert a.keys()==b.keys()
assert [p for p in a if a[p]!=b[p]]==['contract.json']
put(base/'frozen-manifest.json',json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
