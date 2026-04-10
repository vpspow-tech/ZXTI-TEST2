import re

with open('/Users/foneclaw/.openclaw/workspaces/feishu-minimax-bot/sbti-clone/app/data.ts', 'r') as f:
    content = f.read()

image_map = {
    'GFG': '/types/GFG.png',
    'MASTER': '/types/MASTER.png',
    'EXCEED': '/types/EXCEED.png',
    'PERF': '/types/PERF.png',
    'REWORK': '/types/REWORK.png',
    'BOSS2': '/types/BOSS2.png',
    'FOMO': '/types/FOMO.png',
    'COLORG': '/types/COLORG.png',
    'ECO': '/types/ECO.png',
    'THINKL': '/types/THINKL.png',
    'TINDER': '/types/TINDER.png',
    'WATCHL': '/types/WATCHL.png',
    'SHAFT': '/types/SHAFT.png',
    'COMP': '/types/COMP.png',
    'SIBL': '/types/SIBL.png',
    'FLEX': '/types/FLEX.png',
    'CTRL2': '/types/CTRL2.png',
    'DUMP': '/types/DUMP.png',
    'INFLU': '/types/INFLU.png',
    'NOVA': '/types/NOVA.png',
    'LITE': '/types/LITE.png',
    'DRUNK2': '/types/DRUNK2.png',
    'NOBUD': '/types/NOBUD.png',
    'PROBI': '/types/PROBI.png',
    'HHHH2': '/types/HHHH2.png',
}

for code, img in image_map.items():
    # Match the closing `},` of each TYPE_LIBRARY entry and add image before it
    # Pattern: finds the entry and adds image field
    pattern = rf'("{code}":\s*\{{[^}}]*?desc:`[^`]*`)\}}'
    replacement = rf'\1,\n  image: "{img}"}}'
    content = re.sub(pattern, replacement, content)

with open('/Users/foneclaw/.openclaw/workspaces/feishu-minimax-bot/sbti-clone/app/data.ts', 'w') as f:
    f.write(content)

print('done')
