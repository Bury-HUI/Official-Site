# -*- coding: utf-8 -*-
"""通过 GitHub REST API 推送本地文件到仓库（绕过 git/https 的 TLS 问题）"""
import base64
import json
import os
import sys
import urllib.error
import urllib.request

TOKEN = sys.argv[1] if len(sys.argv) > 1 else os.environ.get('GH_TOKEN', '')
OWNER = 'Bury-HUI'
REPO = 'Official-Site'
SRC = r'E:\WorkBuddy AI\2026-09-27-12-00-14\software-launcher-web'
MESSAGE = '''站点初始化：软件官网导航

国内 / 国外软件官网导航页，点击图标直达官方站点。
纯静态实现（单文件 index.html + 16 个图标），无构建依赖。

- 国内：豆包、DeepSeek、千问、小米 MiMo、Kimi、WorkBuddy、看剧AI
- 国外：GitHub、ChatGPT、TikTok、X、YouTube、Facebook、Telegram、Instagram、WhatsApp
- 支持搜索过滤、国内/国外分组切换、深色模式'''

# Git Data API 对二进制更可靠；先建 blob/tree/commit，再更新 ref
API = 'https://api.github.com'
UA = {'User-Agent': 'workbuddy-deploy', 'Accept': 'application/vnd.github+json',
      'Authorization': 'Bearer ' + TOKEN, 'Content-Type': 'application/json'}


def call(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(API + path, data=data, method=method, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            body = r.read().decode()
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        detail = e.read().decode()[:500]
        raise SystemExit('[HTTP %d] %s %s\n%s' % (e.code, method, path, detail))


# 收集文件（相对路径）
files = []
for root, dirs, names in os.walk(SRC):
    dirs[:] = [d for d in dirs if d != '.git']
    for n in names:
        full = os.path.join(root, n)
        rel = os.path.relpath(full, SRC).replace('\\', '/')
        files.append((rel, full))
files.sort()
print('待推送文件 %d 个' % len(files))

# 0) 空仓库无法直接用 Git Data API，先用 Contents API 建立首个提交
first_rel, first_full = files[0]
with open(first_full, 'rb') as f:
    first_b64 = base64.b64encode(f.read()).decode()
call('PUT', '/repos/%s/%s/contents/%s' % (OWNER, REPO, first_rel), {
    'message': MESSAGE,
    'content': first_b64,
    'branch': 'main',
})
print('已建立首个提交（%s），仓库初始化完成' % first_rel)

rest = files[1:]
if not rest:
    print('\n推送完成')
    raise SystemExit(0)

# 1) 每个文件建 blob
tree_items = []
base_tree = None
for rel, full in rest:
    with open(full, 'rb') as f:
        raw = f.read()
    blob = call('POST', '/repos/%s/%s/git/blobs' % (OWNER, REPO), {
        'content': base64.b64encode(raw).decode(),
        'encoding': 'base64',
    })
    tree_items.append({'path': rel, 'mode': '100644', 'type': 'blob', 'sha': blob['sha']})
    print('  blob ok  %-28s %8d B' % (rel, len(raw)))

# 2) 建 tree（基于首个提交的 tree，保证不丢文件）
ref = call('GET', '/repos/%s/%s/git/ref/heads/main' % (OWNER, REPO))
parent_sha = ref['object']['sha']
parent = call('GET', '/repos/%s/%s/git/commits/%s' % (OWNER, REPO, parent_sha))
tree = call('POST', '/repos/%s/%s/git/trees' % (OWNER, REPO),
            {'base_tree': parent['tree']['sha'], 'tree': tree_items})
print('tree ->', tree['sha'][:12])

# 3) 建 commit（带上 parent）
commit = call('POST', '/repos/%s/%s/git/commits' % (OWNER, REPO), {
    'message': '补充图标资源',
    'tree': tree['sha'],
    'parents': [parent_sha],
})
print('commit ->', commit['sha'][:12])

# 4) 更新 main 分支
call('PATCH', '/repos/%s/%s/git/refs/heads/main' % (OWNER, REPO),
     {'sha': commit['sha'], 'force': True})
print('branch main 已更新')

print('\n推送完成')
