import os
from datetime import datetime, timezone, timedelta

BASE_URL = "https://www.gajogae-waste.com"
PHONE = "010-5836-3895"

reviews = [
    ("창원", "changwon", "쓰레기집청소"),
    ("김해", "gimhae", "가정폐기물처리"),
    ("진주", "jinju", "이사폐기물처리"),
    ("양산", "yangsan", "폐업폐기물처리"),
    ("거제", "geoje", "가정폐기물처리"),
    ("통영", "tongyeong", "쓰레기집청소"),
    ("사천", "sacheon", "이사폐기물처리"),
    ("밀양", "miryang", "폐업폐기물처리"),
    ("함안", "haman", "가정폐기물처리"),
    ("창녕", "changnyeong", "쓰레기집청소"),
    ("거창", "geochang", "폐업폐기물처리"),
    ("합천", "hapcheon", "이사폐기물처리"),
    ("하동", "hadong", "가정폐기물처리"),
    ("남해", "namhae", "폐업폐기물처리"),
    ("산청", "sancheong", "쓰레기집청소"),
    ("함양", "hamyang", "가정폐기물처리"),
    ("의령", "uiryeong", "이사폐기물처리"),

    ("부산", "busan", "가정폐기물처리"),
    ("부산 해운대구", "busan-haeundae", "이사폐기물처리"),
    ("부산 부산진구", "busan-busanjin", "폐업폐기물처리"),
    ("부산 수영구", "busan-suyeong", "쓰레기집청소"),
    ("부산 동래구", "busan-dongnae", "가정폐기물처리"),
    ("부산 남구", "busan-namgu", "폐업폐기물처리"),
    ("부산 사하구", "busan-saha", "이사폐기물처리"),
    ("부산 금정구", "busan-geumjeong", "가정폐기물처리"),
    ("부산 기장군", "busan-gijang", "폐업폐기물처리"),

    ("울산", "ulsan", "가정폐기물처리"),
    ("울산 남구", "ulsan-namgu", "폐업폐기물처리"),
    ("울산 중구", "ulsan-junggu", "이사폐기물처리"),
    ("울산 북구", "ulsan-bukgu", "쓰레기집청소"),
    ("울산 동구", "ulsan-donggu", "가정폐기물처리"),
    ("울산 울주군", "ulsan-ulju", "폐업폐기물처리"),
]

service_text = {
    "가정폐기물처리": "집 안에 오래 보관된 생활용품, 고장 난 가전, 낡은 가구와 정리하기 어려운 짐을 중심으로 폐기물처리를 진행했습니다.",
    "이사폐기물처리": "이사 전후로 남은 가구, 생활폐기물, 사용하지 않는 물건들을 정리하고 반출하는 작업을 진행했습니다.",
    "폐업폐기물처리": "폐업 현장에 남은 집기류, 선반, 사무용품, 생활폐기물을 분류하고 반출하는 방식으로 진행했습니다.",
    "쓰레기집청소": "오랜 기간 방치된 생활쓰레기와 오염된 물품을 분류하고, 폐기물 반출과 공간 정리를 함께 진행했습니다.",
}

def review_html(region, slug, service):
    review_slug = f"{slug}-{service_map(service)}"
    url = f"{BASE_URL}/reviews/{review_slug}.html"
    region_url = f"{BASE_URL}/regions/{slug}.html"
    title = f"{region} {service} 작업후기 | 가족애 폐기물처리"

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{title}</title>
  <meta name="description" content="{region} {service} 작업후기입니다. 가족애 폐기물처리는 가정폐기물, 이사폐기물, 폐업폐기물, 쓰레기집청소를 현장 상황에 맞춰 정리합니다." />
  <meta name="keywords" content="{region} {service}, {region} 폐기물처리, {region} 작업후기, {region} 가정폐기물처리, {region} 쓰레기집청소" />

  <meta property="og:type" content="article" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{region} {service} 현장 작업후기와 폐기물처리 진행 안내입니다." />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{BASE_URL}/og-image.jpg" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{region} {service} 작업후기" />
  <meta name="twitter:image" content="{BASE_URL}/og-image.jpg" />

  <link rel="canonical" href="{url}" />
  <link rel="icon" href="/favicon.ico">
  <link rel="stylesheet" href="../style.css" />
</head>

<body>
  <header class="hero region-hero">
    <div class="hero-inner">
      <p class="badge">작업후기</p>
      <h1>{region} {service} 작업후기</h1>
      <p class="hero-text">
        현장 상황에 맞춰 폐기물 분류, 반출, 정리까지 단계별로 진행한 사례입니다.
      </p>
      <a href="tel:{PHONE}" class="main-btn">상담전화 {PHONE}</a>
    </div>
  </header>

  <main>
    <section class="section intro">
      <h2>{region} {service} 현장 정리 사례</h2>
      <p>
        이번 현장은 {region} 지역에서 문의가 들어온 {service} 작업입니다.
        현장 확인 후 폐기물의 양, 건물 구조, 반출 동선, 엘리베이터 유무를 확인하고 작업 범위를 안내드렸습니다.
      </p>

      <p>
        {service_text[service]}
      </p>

      <p>
        폐기물처리 비용은 <strong>1톤 트럭 1대 기준 25만원부터</strong>이며,
        실제 비용은 폐기물의 양, 층수, 엘리베이터 유무, 작업 공간의 넓이 등에 따라 달라질 수 있습니다.
      </p>
    </section>

    <section class="section cards">
      <h2>{region} {service} 작업 과정</h2>

      <div class="card-wrap">
        <div class="card">
          <h3>현장 확인</h3>
          <p>사진과 주소를 통해 폐기물 양, 건물 형태, 반출 동선을 먼저 확인했습니다.</p>
        </div>

        <div class="card">
          <h3>폐기물 분류</h3>
          <p>생활폐기물, 가구류, 집기류 등 종류별로 분류해 반출이 가능하도록 정리했습니다.</p>
        </div>

        <div class="card">
          <h3>운반 처리</h3>
          <p>정리된 폐기물을 안전하게 반출하고 차량에 적재해 처리 절차를 진행했습니다.</p>
        </div>

        <div class="card">
          <h3>마무리 확인</h3>
          <p>작업 후 남은 물품과 현장 상태를 확인하고 깔끔하게 마무리했습니다.</p>
        </div>
      </div>
    </section>

    <section class="section price">
      <h2>{region} 폐기물처리 비용에 영향을 주는 요소</h2>
      <div class="price-box">
        <p class="price-main">1톤 트럭 1대 기준 <strong>25만원부터</strong></p>
        <ul>
          <li>폐기물의 양</li>
          <li>건물의 형태와 층수</li>
          <li>엘리베이터 유무</li>
          <li>작업 공간의 넓이</li>
          <li>차량 진입 가능 여부</li>
          <li>폐기물 종류와 분류 난이도</li>
        </ul>
      </div>
    </section>

    <section class="section area">
      <h2>{region} 폐기물처리 관련 페이지</h2>
      <p>아래 페이지에서 지역별 폐기물처리 안내를 함께 확인하실 수 있습니다.</p>

      <div class="region-box">
        <a href="/regions/{slug}.html">{region} 폐기물처리 안내</a>
        <a href="/">가족애 폐기물처리 메인</a>
        <a href="/reviews/index.html">폐기물처리 작업후기 전체보기</a>
      </div>
    </section>

    <section class="section faq">
      <h2>{region} {service} 자주 묻는 질문</h2>

      <div class="faq-item">
        <h3>{region} {service} 비용은 얼마부터인가요?</h3>
        <p>1톤 트럭 1대 기준 25만원부터이며, 폐기물 양과 현장 상황에 따라 달라질 수 있습니다.</p>
      </div>

      <div class="faq-item">
        <h3>사진만 보내도 상담이 가능한가요?</h3>
        <p>가능합니다. 폐기물 사진, 지역, 층수, 엘리베이터 유무를 알려주시면 상담이 수월합니다.</p>
      </div>

      <div class="faq-item">
        <h3>{region} 지역도 빠른 상담이 가능한가요?</h3>
        <p>네. {region} 및 인근 지역 폐기물처리 상담이 가능합니다.</p>
      </div>
    </section>

    <section class="cta">
      <h2>{region} 폐기물처리 상담이 필요하신가요?</h2>
      <p>{service}, 가정폐기물처리, 폐업폐기물처리, 쓰레기집청소 상담 가능합니다.</p>
      <a href="tel:{PHONE}">{PHONE} 바로 전화하기</a>
    </section>
  </main>

  <footer>
    <p>가족애 폐기물처리</p>
    <p>{region} {service} · 폐기물처리 작업후기</p>
    <p><a href="/privacy.html">개인정보처리방침</a></p>
  </footer>
</body>
</html>
"""

def service_map(service):
    return {
        "가정폐기물처리": "home-waste",
        "이사폐기물처리": "moving-waste",
        "폐업폐기물처리": "business-waste",
        "쓰레기집청소": "trash-cleaning",
    }[service]

def create_reviews_index():
    items = ""
    for region, slug, service in reviews:
        review_slug = f"{slug}-{service_map(service)}"
        items += f'<a href="/reviews/{review_slug}.html">{region} {service} 작업후기</a>\n'

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>폐기물처리 작업후기 | 가족애 폐기물처리</title>
  <meta name="description" content="부산·경남·울산 폐기물처리 작업후기 모음입니다. 가정폐기물처리, 이사폐기물처리, 폐업폐기물처리, 쓰레기집청소 사례를 확인하세요." />
  <link rel="canonical" href="{BASE_URL}/reviews/index.html" />
  <link rel="icon" href="/favicon.ico">
  <link rel="stylesheet" href="../style.css" />
</head>

<body>
  <header class="hero region-hero">
    <div class="hero-inner">
      <p class="badge">작업후기 모음</p>
      <h1>폐기물처리 작업후기</h1>
      <p class="hero-text">부산·경남·울산 지역별 폐기물처리 사례를 확인하세요.</p>
      <a href="tel:{PHONE}" class="main-btn">상담전화 {PHONE}</a>
    </div>
  </header>

  <main>
    <section class="section area">
      <h2>지역별 폐기물처리 작업후기</h2>
      <p>가정폐기물처리, 이사폐기물처리, 폐업폐기물처리, 쓰레기집청소 작업 사례입니다.</p>
      <div class="region-box">
        {items}
      </div>
    </section>
  </main>

  <footer>
    <p>가족애 폐기물처리</p>
    <p><a href="/">메인페이지</a> · <a href="/privacy.html">개인정보처리방침</a></p>
  </footer>
</body>
</html>
"""
    with open("reviews/index.html", "w", encoding="utf-8") as f:
        f.write(html)

def update_sitemap():
    urls = [f"{BASE_URL}/"]
    urls.append(f"{BASE_URL}/reviews/index.html")

    for region, slug, service in reviews:
        urls.append(f"{BASE_URL}/reviews/{slug}-{service_map(service)}.html")

    if os.path.exists("sitemap.xml"):
        with open("sitemap.xml", "r", encoding="utf-8") as f:
            old = f.read()
        for line in old.splitlines():
            if "<loc>" in line:
                url = line.replace("<loc>", "").replace("</loc>", "").strip()
                if url not in urls:
                    urls.append(url)

    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for url in urls:
        sitemap += f"""  <url>
    <loc>{url}</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
"""

    sitemap += "</urlset>\n"

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)

def update_rss():
    kst = timezone(timedelta(hours=9))
    now = datetime.now(kst).strftime("%a, %d %b %Y %H:%M:%S +0900")

    items = ""
    for region, slug, service in reviews[:20]:
        review_slug = f"{slug}-{service_map(service)}"
        items += f"""
    <item>
      <title>{region} {service} 작업후기</title>
      <link>{BASE_URL}/reviews/{review_slug}.html</link>
      <description>{region} {service} 폐기물처리 작업후기입니다.</description>
      <pubDate>{now}</pubDate>
    </item>
"""

    rss = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
  <channel>
    <title>가족애 폐기물처리 작업후기</title>
    <link>{BASE_URL}/reviews/index.html</link>
    <description>부산·경남·울산 폐기물처리 작업후기 모음</description>
    <language>ko</language>
    {items}
  </channel>
</rss>
"""
    with open("rss.xml", "w", encoding="utf-8") as f:
        f.write(rss)

def main():
    os.makedirs("reviews", exist_ok=True)

    for region, slug, service in reviews:
        review_slug = f"{slug}-{service_map(service)}"
        path = f"reviews/{review_slug}.html"
        with open(path, "w", encoding="utf-8") as f:
            f.write(review_html(region, slug, service))

    create_reviews_index()
    update_sitemap()
    update_rss()

    print(f"완료: 작업후기 {len(reviews)}개 생성")
    print("완료: reviews/index.html 생성")
    print("완료: sitemap.xml 업데이트")
    print("완료: rss.xml 업데이트")

if __name__ == "__main__":
    main()