from pathlib import Path
import re

SERVICE_ID = "gajogae_waste"
TEMPLATE_ID = "template_wwbariw"
PUBLIC_KEY = "JKsVOKPtnWHIr2BCV"
PHONE = "010-5836-3895"

COMMON_JS = f'''// 가족애 폐기물처리 공통 메일 전송 코드
// EmailJS 기존 템플릿 변수 기준: {{{{title}}}, {{{{name}}}, {{{{메시지}}}}

(function () {{
  if (typeof emailjs === "undefined") {{
    console.error("EmailJS가 로드되지 않았습니다.");
    return;
  }}

  emailjs.init("{PUBLIC_KEY}");

  const form = document.getElementById("contactForm");
  if (!form) return;

  form.addEventListener("submit", function (e) {{
    e.preventDefault();

    const submitBtn = form.querySelector(".form-btn");
    if (submitBtn) {{
      submitBtn.disabled = true;
      submitBtn.textContent = "접수 중입니다...";
    }}

    const formData = new FormData(form);

    const name = formData.get("name") || "";
    const phone = formData.get("phone") || "";
    const region = formData.get("region") || "";
    const service = formData.get("service") || "";
    const message = formData.get("message") || "";

    const templateParams = {{
      title: `[가족애 폐기물처리] ${{region}} ${{service}} 상담접수`,
      name: name,
      메시지:
        `성함: ${{name}}\\n` +
        `연락처: ${{phone}}\\n` +
        `지역: ${{region}}\\n` +
        `필요 서비스: ${{service}}\\n\\n` +
        `현장 상황:\\n${{message}}`
    }};

    emailjs.send("{SERVICE_ID}", "{TEMPLATE_ID}", templateParams)
      .then(function () {{
        alert("상담 접수가 완료되었습니다. 빠르게 연락드리겠습니다.");
        form.reset();

        if (submitBtn) {{
          submitBtn.disabled = false;
          submitBtn.textContent = "상담 접수하기";
        }}
      }}, function (error) {{
        console.error("EmailJS 오류:", error);
        alert("접수 중 오류가 발생했습니다. 빠른 상담은 {PHONE}로 연락주세요.");

        if (submitBtn) {{
          submitBtn.disabled = false;
          submitBtn.textContent = "상담 접수하기";
        }}
      }});
  }});
}})();
'''

EMAIL_BLOCK_PATTERN = re.compile(
    r'<script src="https://cdn\.jsdelivr\.net/npm/@emailjs/browser@4/dist/email\.min\.js"></script>\s*'
    r'<script>[\s\S]*?emailjs\.init[\s\S]*?</script>',
    re.MULTILINE
)

REPLACEMENT = '''<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
  <script src="/common-email.js"></script>'''


def replace_email_block(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    new_text, count = EMAIL_BLOCK_PATTERN.subn(REPLACEMENT, text)

    if count:
        path.write_text(new_text, encoding="utf-8")
        print(f"수정 완료: {path} ({count}곳)")
        return True

    print(f"변경 없음: {path}")
    return False


def main():
    root = Path(".")
    changed = 0

    js_path = root / "common-email.js"
    js_path.write_text(COMMON_JS, encoding="utf-8")
    print(f"생성 완료: {js_path}")

    targets = []

    for name in ["index.html", "privacy.html", "404.html"]:
        p = root / name
        if p.exists():
            targets.append(p)

    for folder in ["regions", "reviews"]:
        d = root / folder
        if d.exists():
            targets.extend(sorted(d.glob("*.html")))

    for name in [
        "generate_regions_v2.py",
        "generate_reviews_v3.py",
        "generate_reviews_v2.py",
        "generate_regions.py",
        "generate_reviews.py",
    ]:
        p = root / name
        if p.exists():
            targets.append(p)

    for p in targets:
        try:
            if replace_email_block(p):
                changed += 1
        except UnicodeDecodeError:
            print(f"건너뜀(인코딩 문제): {p}")

    print("\\n완료")
    print(f"수정된 파일 수: {changed}")
    print("\\n다음 순서:")
    print("1) 로컬에서 index.html 상담폼 테스트")
    print("2) regions/changwon.html 상담폼 테스트")
    print("3) reviews/changwon-trash-cleaning.html 상담폼 테스트")
    print("4) git add .")
    print('5) git commit -m "가족애 폐기물 메일 변수 통일"')
    print("6) git push")


if __name__ == "__main__":
    main()
