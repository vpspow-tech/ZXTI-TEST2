const fs = require('fs');
let content = fs.readFileSync('/Users/foneclaw/.openclaw/workspaces/feishu-minimax-bot/sbti-clone/app/data.ts', 'utf8');

const imageMap = {
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
};

for (const [code, img] of Object.entries(imageMap)) {
  // Match the type entry and add image field after desc
  const pattern = new RegExp(
    `("${code}"[\\s\\S]*?desc:[\\s\\S]*?\`[^`]+\`)`
  );
  const replacement = `$1\n  image: "${img}"`;
  content = content.replace(pattern, replacement);
}

fs.writeFileSync('/Users/foneclaw/.openclaw/workspaces/feishu-minimax-bot/sbti-clone/app/data.ts', content);
console.log('done');
