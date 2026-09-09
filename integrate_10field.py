import re, os

BASE = "/home/crazy/meme-lol"
FRAGS = os.environ.get("FRAGS_DIR")
assert FRAGS, "set FRAGS_DIR env var"

path = os.path.join(BASE, "index.html")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

before_len = len(content)
before_hex = len(re.findall(r'#[0-9a-fA-F]{6}\b', content))

sections = ["calc", "onramp", "cases", "wallet", "faq"]
missing = []

for key in sections:
    marker = f"<!-- CONTENT:{key} -->"
    n = content.count(marker)
    if n != 1:
        raise SystemExit(f"FATAL: marker for '{key}' found {n} times (expected 1). A1 skeleton not ready or naming mismatch.")
    frag_path = os.path.join(FRAGS, f"{key}.html")
    if os.path.exists(frag_path):
        with open(frag_path, "r", encoding="utf-8") as f:
            frag = f.read()
    else:
        missing.append(key)
        frag = '<div class="card card--flat" data-level="both"><p>內容整理中，稍後補上。</p></div>'
    content = content.replace(marker, frag, 1)

after_len = len(content)
after_hex = len(re.findall(r'#[0-9a-fA-F]{6}\b', content))

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"before_len={before_len} after_len={after_len} delta={after_len-before_len}")
print(f"before_hex_colors={before_hex} after_hex_colors={after_hex}")
print(f"missing_frags={missing}")
print("integrate OK")
