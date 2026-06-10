import os
import random

BASE_URL = "https://www.gajogae-waste.com"
PHONE = "010-5836-3895"

EMAILJS_SERVICE_ID = "gajogae_waste"
EMAILJS_TEMPLATE_ID = "template_wwbariw"
EMAILJS_PUBLIC_KEY = "JKsVOKPtnWHIr2BCV"

regions = [
    {"name": "부산", "slug": "busan", "group": "부산"},
    {"name": "부산 중구", "slug": "busan-junggu", "group": "부산"},
    {"name": "부산 서구", "slug": "busan-seogu", "group": "부산"},
    {"name": "부산 동구", "slug": "busan-donggu", "group": "부산"},
    {"name": "부산 영도구", "slug": "busan-yeongdo", "group": "부산"},
    {"name": "부산 부산진구", "slug": "busan-busanjin", "group": "부산"},
    {"name": "부산 동래구", "slug": "busan-dongnae", "group": "부산"},
    {"name": "부산 남구", "slug": "busan-namgu", "group": "부산"},
    {"name": "부산 북구", "slug": "busan-bukgu", "group": "부산"},
    {"name": "부산 해운대구", "slug": "busan-haeundae", "group": "부산"},
    {"name": "부산 사하구", "slug": "busan-saha", "group": "부산"},
    {"name": "부산 금정구", "slug": "busan-geumjeong", "group": "부산"},
    {"name": "부산 강서구", "slug": "busan-gangseo", "group": "부산"},
    {"name": "부산 연제구", "slug": "busan-yeonje", "group": "부산"},
    {"name": "부산 수영구", "slug": "busan-suyeong", "group": "부산"},
    {"name": "부산 사상구", "slug": "busan-sasang", "group": "부산"},
    {"name": "부산 기장군", "slug": "busan-gijang", "group": "부산"},

    {"name": "울산", "slug": "ulsan", "group": "울산"},
    {"name": "울산 중구", "slug": "ulsan-junggu", "group": "울산"},
    {"name": "울산 남구", "slug": "ulsan-namgu", "group": "울산"},
    {"name": "울산 동구", "slug": "ulsan-donggu", "group": "울산"},
    {"name": "울산 북구", "slug": "ulsan-bukgu", "group": "울산"},
    {"name": "울산 울주군", "slug": "ulsan-ulju", "group": "울산"},

    {"name": "경남", "slug": "gyeongnam", "group": "경남"},
    {"name": "창원", "slug": "changwon", "group": "경남"},
    {"name": "김해", "slug": "gimhae", "group": "경남"},
    {"name": "진주", "slug": "jinju", "group": "경남"},
    {"name": "양산", "slug": "yangsan", "group": "경남"},
    {"name": "거제", "slug": "geoje", "group": "경남"},
    {"name": "통영", "slug": "tongyeong", "group": "경남"},
    {"name": "사천", "slug": "sacheon", "group": "경남"},
    {"name": "밀양", "slug": "miryang", "group": "경남"},
    {"name": "경남 고성", "slug": "goseong", "group": "경남"},
    {"name": "함안", "slug": "haman", "group": "경남"},
    {"name": "창녕", "slug": "changnyeong", "group": "경남"},
    {"name": "거창", "slug": "geochang", "group": "경남"},
    {"name": "합천", "slug": "hapcheon", "group": "경남"},
    {"name": "하동", "slug": "hadong", "group": "경남"},
    {"name": "남해", "slug": "namhae", "group": "경남"},
    {"name": "산청", "slug": "sancheong", "group": "경남"},
    {"name": "함양", "slug": "hamyang", "group": "경남"},
    {"name": "의령", "slug": "uiryeong", "group": "경남"},
]

def create_internal_links(current_slug):
    groups = {
        "부산 지역 폐기물처리": [],
        "경남 지역 폐기물처리": [],
        "울산 지역 폐기물처리": []
    }

    for r in regions:
        if r["slug"] == current_slug:
            continue

        label = r["name"].replace("부산 ", "").replace("울산 ", "")

        if r["group"] == "부산":
            groups["부산 지역 폐기물처리"].append(
                f'<a href="/regions/{r["slug"]}.html">{label}</a>'
            )
        elif r["group"] == "경남":
            groups["경남 지역 폐기물처리"].append(
                f'<a href="/regions/{r["slug"]}.html">{label}</a>'
            )
        elif r["group"] == "울산":
            groups["울산 지역 폐기물처리"].append(
                f'<a href="/regions/{r["slug"]}.html">{label}</a>'
            )

    html = """
    <section class="section area">
      <h2>부산·경남·울산 폐기물처리 지역 바로가기</h2>
      <p>
        가족애 폐기물처리는 부산, 경남, 울산 전지역 폐기물처리 상담이 가능합니다.
        가까운 지역 페이지를 함께 확인해보세요.
      </p>

      <div class="area-groups">
    """

    for title, links in groups.items():
        html += f"""
        <div class="area-group">
          <h3>{title}</h3>
          <div class="region-box">
            {''.join(links)}
          </div>
        </div>
        """

    html += """
      </div>
    </section>
    """

    return html

title_patterns = [
    "{name} 폐기물처리 | 가정폐기물·쓰레기집청소·폐업폐기물 처리",
    "{name} 가정폐기물처리 | 가족애 폐기물처리 상담 안내",
    "{name} 쓰레기집청소 폐기물처리 | 1톤 트럭 기준 비용 안내",
    "{name} 폐업폐기물처리 | 이사폐기물·생활폐기물 정리",
]

intro_patterns = [
    "{name}에서 집 안에 쌓인 생활폐기물, 이사폐기물, 폐업 현장의 집기류, 쓰레기집청소가 필요한 공간까지 상황에 맞춰 정리합니다.",
    "{name} 폐기물처리는 가정에서 나온 생활폐기물부터 이사 후 남은 짐, 폐업 후 집기류, 방치된 쓰레기 정리까지 현장 상황에 맞춰 진행합니다.",
    "{name} 지역에서 혼자 처리하기 어려운 폐기물, 오래된 가구와 생활용품, 폐업 현장 정리, 쓰레기집청소가 필요할 때 상담 가능합니다.",
    "{name} 폐기물처리는 폐기물 양과 건물 구조, 반출 동선, 엘리베이터 유무 등을 확인한 뒤 현장에 맞는 방식으로 정리합니다.",
]

h2_patterns = [
    "{name} 폐기물처리 전문 안내",
    "{name} 가정폐기물처리와 생활폐기물 정리",
    "{name} 쓰레기집청소와 폐기물 반출 안내",
    "{name} 폐업폐기물처리 및 이사폐기물 정리",
]

service_intro_patterns = [
    "{name} 지역에서 자주 문의되는 폐기물처리 서비스를 정리했습니다.",
    "{name} 현장에서 많이 요청되는 주요 작업 항목입니다.",
    "{name} 폐기물처리 상담 시 아래와 같은 작업을 함께 안내드립니다.",
]

faq_cost_patterns = [
    "{name} 폐기물처리 비용은 1톤 트럭 1대 기준 25만원부터입니다. 폐기물의 양, 층수, 엘리베이터 유무, 작업 공간의 넓이에 따라 실제 비용은 달라질 수 있습니다.",
    "{name} 폐기물처리는 기본적으로 1톤 트럭 1대 기준 25만원부터 안내됩니다. 다만 건물 구조, 반출 거리, 폐기물 종류에 따라 비용이 달라질 수 있습니다.",
    "{name} 지역 폐기물처리 비용은 1톤 트럭 기준 25만원부터이며, 현장 사진과 폐기물 양을 확인한 뒤 자세히 안내드립니다.",
]

def pick(items, seed_text):
    random.seed(seed_text)
    return random.choice(items)


def html_template(region):
    name = region["name"]
    slug = region["slug"]
    url = f"{BASE_URL}/regions/{slug}.html"

    title = pick(title_patterns, slug + "title").format(name=name)
    intro = pick(intro_patterns, slug + "intro").format(name=name)
    h2_intro = pick(h2_patterns, slug + "h2").format(name=name)
    service_intro = pick(service_intro_patterns, slug + "service").format(name=name)
    faq_cost = pick(faq_cost_patterns, slug + "faq").format(name=name)
    internal_links = create_internal_links(slug)

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <link rel="icon" href="/favicon.ico">
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{title}</title>
  <meta name="description" content="{name} 폐기물처리 전문 가족애 폐기물처리입니다. {name} 가정폐기물처리, 이사폐기물처리, 폐업폐기물처리, 쓰레기집청소 상담 가능합니다. 1톤 트럭 1대 기준 25만원부터 안내드립니다." />
  <meta name="keywords" content="{name} 폐기물처리, {name} 가정폐기물처리, {name} 쓰레기집청소, {name} 폐업폐기물처리, {name} 이사폐기물처리, {name} 생활폐기물처리" />
  <meta name="author" content="가족애 폐기물처리" />

  <meta property="og:type" content="article" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{name} 가정폐기물처리, 쓰레기집청소, 폐업폐기물처리, 이사폐기물처리 상담 가능합니다." />
  <meta property="og:url" content="{url}" />
  <meta property="og:site_name" content="가족애 폐기물처리" />
  <meta property="og:image" content="{BASE_URL}/og-image.jpg" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{name} 폐기물처리 상담 가능합니다." />
  <meta name="twitter:image" content="{BASE_URL}/og-image.jpg" />

  <link rel="canonical" href="{url}" />
  <link rel="stylesheet" href="../style.css" />

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{name} 폐기물처리 전문 가족애 폐기물처리",
    "description": "{name} 가정폐기물처리, 이사폐기물처리, 폐업폐기물처리, 쓰레기집청소 및 폐기물처리 비용 안내",
    "author": {{
      "@type": "Organization",
      "name": "가족애 폐기물처리"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "가족애 폐기물처리"
    }},
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "{url}"
    }}
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "{name} 폐기물처리 비용은 얼마부터인가요?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{faq_cost}"
        }}
      }},
      {{
        "@type": "Question",
        "name": "{name}에서 쓰레기집청소도 가능한가요?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "네. {name} 지역 쓰레기집청소, 생활폐기물 정리, 폐기물 반출 상담이 가능합니다."
        }}
      }},
      {{
        "@type": "Question",
        "name": "{name} 폐업폐기물처리도 가능한가요?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "네. {name} 사무실, 식당, 매장 폐업 후 남은 집기류와 폐기물 처리가 가능합니다."
        }}
      }}
    ]
  }}
  </script>
</head>

<body>
  <header class="hero region-hero">
    <div class="hero-inner">
      <p class="badge">{name} 폐기물처리 상담</p>
      <h1>{name} 폐기물처리</h1>
      <p class="hero-text">
        {name} 가정폐기물처리, 쓰레기집청소, 폐업폐기물처리, 이사폐기물처리까지<br />
        현장 상황에 맞춰 신속하고 깔끔하게 정리합니다.
      </p>
      <a href="tel:{PHONE}" class="main-btn">상담전화 {PHONE}</a>
    </div>
  </header>

  <main>
    <section class="section intro">
      <h2>{h2_intro}</h2>

      <p>{intro}</p>

      <p>
        폐기물처리 비용은 <strong>1톤 트럭 1대 기준 25만원부터</strong>이며,
      </p>

      <p>
        폐기물의 양, 건물의 형태, 층수, 엘리베이터 유무,
        작업 공간의 넓이에 따라 달라질 수 있습니다.
      </p>
    </section>

    <section class="section cards">
      <h2>{name} 주요 폐기물처리 서비스</h2>
      <p>{service_intro}</p>

      <div class="card-wrap">
        <div class="card">
          <h3>{name} 가정폐기물처리</h3>
          <p>집 안에 쌓인 오래된 가구, 생활용품, 정리하기 어려운 물건을 현장 상황에 맞게 처리합니다.</p>
        </div>

        <div class="card">
          <h3>{name} 쓰레기집청소</h3>
          <p>방치된 생활쓰레기, 악취, 오염 공간 정리와 폐기물 반출까지 함께 상담 가능합니다.</p>
        </div>

        <div class="card">
          <h3>{name} 폐업폐기물처리</h3>
          <p>사무실, 식당, 매장 폐업 후 남은 집기류와 불필요한 물품을 정리합니다.</p>
        </div>

        <div class="card">
          <h3>{name} 이사폐기물처리</h3>
          <p>이사 전후 버려야 할 가구, 가전, 생활폐기물을 빠르게 정리합니다.</p>
        </div>
      </div>
    </section>

    <section class="section price">
      <h2>{name} 폐기물처리 비용 안내</h2>

      <div class="price-box">
        <p class="price-main">1톤 트럭 1대 기준 <strong>25만원부터</strong></p>
        <p>
          {name} 폐기물처리 비용은 폐기물의 양과 현장 환경에 따라 달라질 수 있습니다.
          같은 분량이라도 건물 구조나 반출 동선에 따라 작업 시간과 인력이 달라질 수 있습니다.
        </p>

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

    <section class="section process">
      <h2>{name} 폐기물처리 진행 과정</h2>
      <p class="process-desc">
        상담부터 현장 확인, 폐기물 분류와 처리까지 단계별로 체계적으로 진행합니다.
      </p>

      <div class="process-grid">
        <div class="process-card">
          <div class="step-number">01</div>
          <div class="step-icon">☎</div>
          <h3>상담 접수</h3>
          <p>전화 또는 문자로 {name} 지역과 폐기물 종류를 확인합니다.</p>
        </div>

        <div class="process-card">
          <div class="step-number">02</div>
          <div class="step-icon">▣</div>
          <h3>현장 확인</h3>
          <p>사진, 주소, 건물 구조와 작업 환경을 확인합니다.</p>
        </div>

        <div class="process-card">
          <div class="step-number">03</div>
          <div class="step-icon">₩</div>
          <h3>비용 안내</h3>
          <p>폐기물 양, 층수, 엘리베이터 유무에 따라 비용을 안내합니다.</p>
        </div>

        <div class="process-card">
          <div class="step-number">04</div>
          <div class="step-icon">✓</div>
          <h3>분류 정리</h3>
          <p>폐기물을 종류별로 분류하고 반출 가능하도록 정리합니다.</p>
        </div>

        <div class="process-card">
          <div class="step-number">05</div>
          <div class="step-icon">🚚</div>
          <h3>운반 처리</h3>
          <p>정리된 폐기물을 안전하게 운반하고 처리합니다.</p>
        </div>

        <div class="process-card">
          <div class="step-number">06</div>
          <div class="step-icon">◎</div>
          <h3>마무리 확인</h3>
          <p>작업 후 현장을 확인하고 깔끔하게 마무리합니다.</p>
        </div>
      </div>
    </section>

    <section class="section contact-form-section">
      <h2>{name} 폐기물처리 상담 접수</h2>
      <p class="form-desc">
        지역, 폐기물 종류, 현장 상황을 남겨주시면 확인 후 빠르게 연락드리겠습니다.
      </p>

      <form class="contact-form" id="contactForm">
        <div class="form-row">
          <label for="name">성함</label>
          <input type="text" id="name" name="name" placeholder="성함을 입력해주세요" required>
        </div>

        <div class="form-row">
          <label for="phone">연락처</label>
          <input type="tel" id="phone" name="phone" placeholder="010-0000-0000" required>
        </div>

        <div class="form-row">
          <label for="region">지역</label>
          <input type="text" id="region" name="region" value="{name}" required>
        </div>

        <div class="form-row">
          <label for="service">필요 서비스</label>
          <select id="service" name="service" required>
            <option value="">서비스를 선택해주세요</option>
            <option value="가정폐기물처리">가정폐기물처리</option>
            <option value="이사폐기물처리">이사폐기물처리</option>
            <option value="폐업폐기물처리">폐업폐기물처리</option>
            <option value="쓰레기집청소">쓰레기집청소</option>
            <option value="기타 폐기물처리">기타 폐기물처리</option>
          </select>
        </div>

        <div class="form-row full">
          <label for="message">현장 상황</label>
          <textarea id="message" name="message" rows="5" placeholder="폐기물 양, 건물 층수, 엘리베이터 유무, 사진 전달 가능 여부 등을 적어주세요."></textarea>
        </div>

        <div class="privacy-box">
          <div class="privacy-title">개인정보 수집 및 이용 동의</div>

          <div class="privacy-content">
            <p>
              가족애 폐기물처리는 상담 접수 및 문의 응대를 위해 아래와 같이 개인정보를 수집·이용합니다.
            </p>
            <ul>
              <li>수집항목 : 성함, 연락처, 지역, 상담내용</li>
              <li>이용목적 : 상담 문의 확인 및 연락</li>
              <li>보유기간 : 상담 완료 후 최대 1년</li>
              <li>동의를 거부할 권리가 있으며 거부 시 상담 접수가 제한될 수 있습니다.</li>
            </ul>
          </div>

          <label class="privacy-check">
            <input type="checkbox" required>
            개인정보 수집 및 이용에 동의합니다.
          </label>
        </div>

        <button type="submit" class="form-btn">상담 접수하기</button>

        <p class="form-notice">
          빠른 상담은 <strong>{PHONE}</strong>로 전화 또는 문자 주시면 됩니다.
        </p>
      </form>
    </section>

        {internal_links}
    <section class="section faq">
      <h2>{name} 폐기물처리 자주 묻는 질문</h2>

      <div class="faq-item">
        <h3>{name} 폐기물처리 비용은 얼마부터인가요?</h3>
        <p>{faq_cost}</p>
      </div>

      <div class="faq-item">
        <h3>{name} 쓰레기집청소와 폐기물처리를 같이 할 수 있나요?</h3>
        <p>
          가능합니다. 쓰레기 정리, 폐기물 반출, 현장 정돈까지 상황에 맞게 진행합니다.
        </p>
      </div>

      <div class="faq-item">
        <h3>{name} 폐업폐기물처리도 가능한가요?</h3>
        <p>
          가능합니다. 사무실, 식당, 매장 폐업 후 남은 집기류와 불필요한 물품 정리가 가능합니다.
        </p>
      </div>

      <div class="faq-item">
        <h3>상담은 어떻게 하나요?</h3>
        <p>
          전화 또는 문자로 지역, 폐기물 종류, 현장 사진을 보내주시면 빠르게 안내 가능합니다.
          상담 문의는 {PHONE}로 연락 주시면 됩니다.
        </p>
      </div>
    </section>

    <section class="cta">
      <h2>{name} 폐기물처리 상담이 필요하신가요?</h2>
      <p>{name} 가정폐기물처리, 쓰레기집청소, 폐업폐기물처리 상담 가능합니다.</p>
      <a href="tel:{PHONE}">{PHONE} 바로 전화하기</a>
    </section>
  </main>

  <footer>
    <p>가족애 폐기물처리</p>
    <p>{name} 폐기물처리 · 가정폐기물처리 · 쓰레기집청소 · 폐업폐기물처리 · 이사폐기물처리</p>
    <p><a href="/privacy.html">개인정보처리방침</a></p>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
  <script>
    emailjs.init("{EMAILJS_PUBLIC_KEY}");

    document.getElementById("contactForm").addEventListener("submit", function(e) {{
      e.preventDefault();

      const submitBtn = this.querySelector(".form-btn");
      submitBtn.disabled = true;
      submitBtn.textContent = "접수 중입니다...";

      emailjs.sendForm("{EMAILJS_SERVICE_ID}", "{EMAILJS_TEMPLATE_ID}", this)
        .then(function() {{
          alert("상담 접수가 완료되었습니다. 빠르게 연락드리겠습니다.");
          document.getElementById("contactForm").reset();
          submitBtn.disabled = false;
          submitBtn.textContent = "상담 접수하기";
        }}, function(error) {{
          alert("접수 중 오류가 발생했습니다. 빠른 상담은 {PHONE}로 연락주세요.");
          submitBtn.disabled = false;
          submitBtn.textContent = "상담 접수하기";
        }});
    }});
  </script>
</body>
</html>
"""


def create_sitemap():
    urls = [f"{BASE_URL}/"]
    urls += [f"{BASE_URL}/regions/{r['slug']}.html" for r in regions]

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


def create_robots():
    robots = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(robots)


def main():
    os.makedirs("regions", exist_ok=True)

    for region in regions:
        path = os.path.join("regions", f"{region['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html_template(region))

    create_sitemap()
    create_robots()

    print(f"완료: SEO 랜덤화 지역 페이지 {len(regions)}개 생성")
    print("완료: EmailJS 상담폼 적용")
    print("완료: sitemap.xml 생성")
    print("완료: robots.txt 생성")


if __name__ == "__main__":
    main()