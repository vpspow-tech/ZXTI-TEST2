import re

with open('/Users/foneclaw/.openclaw/workspaces/feishu-minimax-bot/sbti-clone/app/page.tsx', 'r') as f:
    content = f.read()

# Add image map after TYPE_LIBRARY import
image_map = '''const TYPE_IMAGE_MAP: Record<string, string> = {
  GFG: '/types/GFG.png',
  MASTER: '/types/MASTER.png',
  EXCEED: '/types/EXCEED.png',
  PERF: '/types/PERF.png',
  REWORK: '/types/REWORK.png',
  BOSS2: '/types/BOSS2.png',
  FOMO: '/types/FOMO.png',
  COLORG: '/types/COLORG.png',
  ECO: '/types/ECO.png',
  THINKL: '/types/THINKL.png',
  TINDER: '/types/TINDER.png',
  WATCHL: '/types/WATCHL.png',
  SHAFT: '/types/SHAFT.png',
  COMP: '/types/COMP.png',
  SIBL: '/types/SIBL.png',
  FLEX: '/types/FLEX.png',
  CTRL2: '/types/CTRL2.png',
  DUMP: '/types/DUMP.png',
  INFLU: '/types/INFLU.png',
  NOVA: '/types/NOVA.png',
  LITE: '/types/LITE.png',
  DRUNK2: '/types/DRUNK2.png',
  NOBUD: '/types/NOBUD.png',
  PROBI: '/types/PROBI.png',
  HHHH2: '/types/HHHH2.png',
};

'''

# Insert after TYPE_LIBRARY import line
content = content.replace(
    "import {\n  questions,",
    "import {\n  questions,"
)

# Actually insert after DRUNK_TRIGGER_QUESTION_ID import
content = content.replace(
    "  DRUNK_TRIGGER_QUESTION_ID,\n} from './data';",
    "  DRUNK_TRIGGER_QUESTION_ID,\n} from './data';\n\n" + image_map
)

# Add image to finalType in computeResult
# Find: return { rawScores, levels, ranked, bestNormal, finalType, ...
# And change finalType spread to include image
content = content.replace(
    "let finalType: (typeof TYPE_LIBRARY)[string] & { distance?: number; exact?: number; similarity?: number };",
    "let finalType: (typeof TYPE_LIBRARY)[string] & { distance?: number; exact?: number; similarity?: number; image?: string };"
)

# Replace all the finalType assignments to include image
content = content.replace(
    "finalType = { ...TYPE_LIBRARY.DRUNK, distance: 0, exact: 15, similarity: 100 };",
    "finalType = { ...TYPE_LIBRARY.DRUNK, distance: 0, exact: 15, similarity: 100, image: TYPE_IMAGE_MAP.DRUNK || TYPE_IMAGE_MAP.DRUNK2 };"
)

content = content.replace(
    "finalType = { ...TYPE_LIBRARY.HHHH, distance: bestNormal.distance, exact: bestNormal.exact, similarity: bestNormal.similarity };",
    "finalType = { ...bestNormal, image: TYPE_IMAGE_MAP[bestNormal.code] };"
)

content = content.replace(
    "finalType = { ...bestNormal };",
    "finalType = { ...bestNormal, image: TYPE_IMAGE_MAP[bestNormal.code] };"
)

with open('/Users/foneclaw/.openclaw/workspaces/feishu-minimax-bot/sbti-clone/app/page.tsx', 'w') as f:
    f.write(content)

print('done')
