from pathlib import Path
import re

FILES = [Path("index.html")] + list(Path("regions").glob("*.html"))

old_pattern = re.compile(
    r'emailjs\.sendForm\(\s*["\']gajogae_waste["\']\s*,\s*["\'][^"\']+["\']\s*,\s*this\s*\)',
    re.S
)

new_code = '''emailjs.send("gajogae_waste", "template_wwbariw", {
                    title: "가족애 폐기물처리 상담접수",
                    name: this.querySelector('[name="name"]')?.value || "",
                    email: "bg.jin78@gmail.com",
                    message:
                        "접수 사이트: 가족애 폐기물처리\\n\\n" +
                        "이름: " + (this.querySelector('[name="name"]')?.value || "") + "\\n\\n" +
                        "연락처: " + (this.querySelector('[name="phone"]')?.value || "") + "\\n\\n" +
                        "지역/주소: " + (this.querySelector('[name="region"]')?.value || "") + "\\n\\n" +
                        "요청 서비스: " + (this.querySelector('[name="service"]')?.value || "") + "\\n\\n" +
                        "상담 내용:\\n" + (this.querySelector('[name="message"]')?.value || "") + "\\n\\n" +
                        "접수 페이지:\\n" + window.location.href
                })'''

count = 0

for file in FILES:
    if not file.exists():
        continue

    html = file.read_text(encoding="utf-8", errors="ignore")
    new_html = old_pattern.sub(new_code, html)

    if new_html != html:
        file.write_text(new_html, encoding="utf-8")
        print("수정:", file)
        count += 1

print(f"완료: {count}개 파일 수정")