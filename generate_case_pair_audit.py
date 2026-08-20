"""100개 전·후 세트 사진 검수용 HTML 생성."""
import os
from generate_reviews_v3 import CASE_PAIR_BLOCKLIST, valid_case_pair_numbers

OUT = "case-pair-audit.html"
BASE = "images/cases"


def main():
    cards = []
    for n in range(1, 101):
        before = f"/{BASE}/waste-before-{n:03d}.jpg"
        after = f"/{BASE}/waste-after-{n:03d}.jpg"
        blocked = n in CASE_PAIR_BLOCKLIST
        badge = "제외" if blocked else "사용"
        cards.append(
            f"""
      <article class="card{' blocked' if blocked else ''}">
        <h2>세트 {n:03d} <span>{badge}</span></h2>
        <div class="pair">
          <figure>
            <img src="{before}" alt="before {n:03d}" loading="lazy">
            <figcaption>작업 전</figcaption>
          </figure>
          <figure>
            <img src="{after}" alt="after {n:03d}" loading="lazy">
            <figcaption>작업 후</figcaption>
          </figure>
        </div>
      </article>"""
        )

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>폐기물 세트 사진 검수</title>
  <style>
    body {{ font-family: sans-serif; margin: 0; padding: 24px; background: #f5f5f5; }}
    h1 {{ margin-bottom: 8px; }}
    p {{ color: #555; }}
    .grid {{ display: grid; gap: 20px; }}
    .card {{ background: #fff; border-radius: 12px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,.08); }}
    .card.blocked {{ border: 2px solid #e53935; }}
    .card h2 span {{ font-size: 14px; color: #666; font-weight: normal; }}
    .pair {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
    img {{ width: 100%; height: auto; border-radius: 8px; background: #ddd; }}
    figcaption {{ text-align: center; margin-top: 8px; font-size: 14px; }}
    @media (max-width: 720px) {{ .pair {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
  <h1>폐기물 세트 사진 검수</h1>
  <p>전·후가 같은 현장인지, 후 사진이 정리 완료처럼 보이는지 확인하세요. 제외 목록: {sorted(CASE_PAIR_BLOCKLIST)} · 사용 가능: {len(valid_case_pair_numbers())}개</p>
  <div class="grid">
    {''.join(cards)}
  </div>
</body>
</html>
"""
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"완료: {OUT}")


if __name__ == "__main__":
    main()
