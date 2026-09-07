import sys
path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()
KEEP_MARKERS = [
    "費率每筆約 1%（買賣各收）（2026/9查證",
    "基礎 1%，等級最低 0.75%，推薦碼再 -10%（2026/9查證",
    "現貨約 0.5%，gas 平台代付（2026/9查證",
    "完全免費（2026/9查證",
    "gas 用 ETH）（2026/9查證",
]
PHRASE_A = "（2026/9查證，請以官方公告為準）"
PHRASE_B = "（數值為 2026/9 查證常見設定，請以官方公告為準）"
out = []
removed = 0
for line in lines:
    if any(m in line for m in KEEP_MARKERS):
        out.append(line)
        continue
    new = line.replace(PHRASE_B, "").replace(PHRASE_A, "")
    if new != line:
        removed += 1
    out.append(new)
with open(path, "w", encoding="utf-8") as f:
    f.writelines(out)
print("lines modified:", removed)
