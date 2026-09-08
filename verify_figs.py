import re, sys
path = sys.argv[1] if len(sys.argv) > 1 else "index.html"
content = open(path, encoding="utf-8").read()
svgs = re.findall(r'<svg[\s\S]*?</svg>', content)
print(f"共 {len(svgs)} 個 <svg>（預期8）")
ok = True
for i, s in enumerate(svgs):
    has_role = 'role="img"' in s
    has_title = '<title' in s
    has_hardcoded = bool(re.search(r'#[0-9A-Fa-f]{6}', s))
    has_viewbox = 'viewBox=' in s
    if not (has_role and has_title and has_viewbox) or has_hardcoded:
        ok = False
        print(f"svg[{i}] FAIL: role={has_role} title={has_title} viewBox={has_viewbox} hardcoded_hex={has_hardcoded}")
print("PASS" if ok and len(svgs) == 8 else "FAIL")
