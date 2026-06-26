
from pathlib import Path
import re

FORM_REPLACEMENT = '''<form class="contact-form" id="contactForm">
          <input type="hidden" name="title" id="mailTitle">
          <input type="hidden" name="message" id="mailMessage">
          <input type="hidden" name="메시지" id="mailMessageKr">'''

HTML_SCRIPT = '''<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
  <script>
    emailjs.init("JKsVOKPtnWHIr2BCV");

    const contactForm = document.getElementById("contactForm");

    if (contactForm) {
      contactForm.addEventListener("submit", function(e) {
        e.preventDefault();

        const submitBtn = this.querySelector(".form-btn");
        submitBtn.disabled = true;
        submitBtn.textContent = "접수 중입니다...";

        const formData = new FormData(this);

        const name = formData.get("name") || "";
        const phone = formData.get("phone") || "";
        const region = formData.get("region") || "";
        const service = formData.get("service") || "";
        const message = formData.get("raw_message") || "";

        const finalTitle = `[가족애 폐기물처리] ${region} ${service} 상담접수`;

        const finalMessage =
          `성함: ${name}\\n` +
          `연락처: ${phone}\\n` +
          `지역: ${region}\\n` +
          `필요 서비스: ${service}\\n\\n` +
          `현장 상황\\n` +
          `--------------------------------\\n` +
          `${message}`;

        document.getElementById("mailTitle").value = finalTitle;
        document.getElementById("mailMessage").value = finalMessage;
        document.getElementById("mailMessageKr").value = finalMessage;

        emailjs.sendForm("gajogae_waste", "template_wwbariw", this)
          .then(function() {
            alert("상담 접수가 완료되었습니다. 빠르게 연락드리겠습니다.");
            contactForm.reset();
            submitBtn.disabled = false;
            submitBtn.textContent = "상담 접수하기";
          }, function(error) {
            console.log("EmailJS Error:", error);
            alert("접수 중 오류가 발생했습니다. 빠른 상담은 010-5836-3895로 연락주세요.");
            submitBtn.disabled = false;
            submitBtn.textContent = "상담 접수하기";
          });
      });
    }
  </script>'''

PY_SCRIPT = '''<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
  <script>
    emailjs.init("{EMAILJS_PUBLIC_KEY}");

    const contactForm = document.getElementById("contactForm");

    if (contactForm) {{
      contactForm.addEventListener("submit", function(e) {{
        e.preventDefault();

        const submitBtn = this.querySelector(".form-btn");
        submitBtn.disabled = true;
        submitBtn.textContent = "접수 중입니다...";

        const formData = new FormData(this);

        const name = formData.get("name") || "";
        const phone = formData.get("phone") || "";
        const region = formData.get("region") || "";
        const service = formData.get("service") || "";
        const message = formData.get("raw_message") || "";

        const finalTitle = `[가족애 폐기물처리] ${{region}} ${{service}} 상담접수`;

        const finalMessage =
          `성함: ${{name}}\\n` +
          `연락처: ${{phone}}\\n` +
          `지역: ${{region}}\\n` +
          `필요 서비스: ${{service}}\\n\\n` +
          `현장 상황\\n` +
          `--------------------------------\\n` +
          `${{message}}`;

        document.getElementById("mailTitle").value = finalTitle;
        document.getElementById("mailMessage").value = finalMessage;
        document.getElementById("mailMessageKr").value = finalMessage;

        emailjs.sendForm("{EMAILJS_SERVICE_ID}", "{EMAILJS_TEMPLATE_ID}", this)
          .then(function() {{
            alert("상담 접수가 완료되었습니다. 빠르게 연락드리겠습니다.");
            contactForm.reset();
            submitBtn.disabled = false;
            submitBtn.textContent = "상담 접수하기";
          }}, function(error) {{
            console.log("EmailJS Error:", error);
            alert("접수 중 오류가 발생했습니다. 빠른 상담은 {PHONE}로 연락주세요.");
            submitBtn.disabled = false;
            submitBtn.textContent = "상담 접수하기";
          }});
      }});
    }}
  </script>'''

SCRIPT_PATTERN = re.compile(
    r'<script src="https://cdn\.jsdelivr\.net/npm/@emailjs/browser@4/dist/email\.min\.js"></script>\s*'
    r'<script>[\s\S]*?</script>',
    re.MULTILINE
)

FORM_PATTERN = re.compile(
    r'<form class="contact-form" id="contactForm">\s*'
    r'(?:<input type="hidden" name="title" id="mailTitle">\s*)?'
    r'(?:<input type="hidden" name="message" id="mailMessage">\s*)?'
    r'(?:<input type="hidden" name="메시지" id="mailMessageKr">\s*)?'
    r'(?:<input type="hidden" name="메시지" id="mailMessage">\s*)?',
    re.MULTILINE
)

def patch_text(text: str, is_py: bool) -> str:
    text = FORM_PATTERN.sub(FORM_REPLACEMENT, text)
    text = text.replace('name="message"', 'name="raw_message"')
    text = text.replace('name="raw_raw_message"', 'name="raw_message"')
    script = PY_SCRIPT if is_py else HTML_SCRIPT
    text = SCRIPT_PATTERN.sub(script, text)
    return text

def main():
    root = Path(".")
    targets = []

    for name in ["index.html"]:
        p = root / name
        if p.exists():
            targets.append(p)

    for folder in ["regions", "reviews"]:
        d = root / folder
        if d.exists():
            targets.extend(sorted(d.glob("*.html")))

    for name in ["generate_regions_v2.py", "generate_reviews_v3.py"]:
        p = root / name
        if p.exists():
            targets.append(p)

    changed = 0
    for p in targets:
        old = p.read_text(encoding="utf-8")
        new = patch_text(old, p.suffix == ".py")
        if old != new:
            p.write_text(new, encoding="utf-8")
            changed += 1
            print(f"수정 완료: {p}")
        else:
            print(f"변경 없음: {p}")

    print()
    print(f"완료: {changed}개 파일 수정")
    print("다음 순서:")
    print("1) python generate_regions_v2.py")
    print("2) python generate_reviews_v3.py")
    print("3) 메일 테스트")
    print("4) git add .")
    print('5) git commit -m "메일 본문 변수 통일"')
    print("6) git push")

if __name__ == "__main__":
    main()
