import re

with open('/Users/foneclaw/.openclaw/workspaces/feishu-minimax-bot/sbti-clone/app/data.ts', 'r') as f:
    content = f.read()

# Add image field to TypeEntry interface
content = content.replace(
    'export interface TypeEntry {\n  code: string;',
    'export interface TypeEntry {\n  code: string;\n  image?: string;'
)

with open('/Users/foneclaw/.openclaw/workspaces/feishu-minimax-bot/sbti-clone/app/data.ts', 'w') as f:
    f.write(content)

print('done - added image field to TypeEntry')
