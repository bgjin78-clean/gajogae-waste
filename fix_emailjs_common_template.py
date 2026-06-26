from pathlib import Path

FILES = [
    "index.html",
    "generate_regions_v2.py",
    "generate_reviews_v3.py",
]

OLD = "emailjs.sendForm("
NEW = "emailjs.send("

for file in FILES:

    p = Path(file)

    if not p.exists():
        print(f"건너뜀 : {file}")
        continue

    text = p.read_text(encoding="utf-8")

    if OLD in text:
        text = text.replace(OLD, NEW)

        p.write_text(text, encoding="utf-8")

        print(f"수정 완료 : {file}")

    else:
        print(f"이미 수정됨 : {file}")

print("\n완료")