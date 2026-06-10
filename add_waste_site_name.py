from pathlib import Path
import re

FILES = [Path("index.html")] + list(Path("regions").glob("*.html"))

HIDDEN = '<input type="hidden" name="site_name" value="가족애 폐기물처리">'

count = 0

for file_path in FILES:
    html = file_path.read_text(encoding="utf-8", errors="ignore")

    if 'name="site_name"' in html:
        continue

    html_new = re.sub(
        r'(<form[^>]*>)',
        r'\1\n' + HIDDEN,
        html,
        count=1,
        flags=re.S
    )

    if html_new != html:
        file_path.write_text(html_new, encoding="utf-8")
        print("수정:", file_path)
        count += 1

print(f"완료: {count}개 파일 수정")