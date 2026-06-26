import os
from datetime import datetime, timezone, timedelta

BASE_URL = "https://www.gajogae-waste.com"
PHONE = "010-5836-3895"

EMAILJS_SERVICE_ID = "gajogae_waste"
EMAILJS_TEMPLATE_ID = "template_wwbariw"
EMAILJS_PUBLIC_KEY = "JKsVOKPtnWHIr2BCV"

CASE_IMAGE_COUNT = 100

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

service_slug = {
    "가정폐기물처리": "home-waste",
    "이사폐기물처리": "moving-waste",
    "폐업폐기물처리": "business-waste",
    "쓰레기집청소": "trash-cleaning",
}

type_names = ["작업후기형", "비용분석형", "상담진행형", "체크리스트형"]

service_desc = {
    "가정폐기물처리": "오래 보관된 생활용품, 낡은 가구, 고장 난 가전, 정리하기 어려운 짐을 중심으로 폐기물처리를 진행했습니다.",
    "이사폐기물처리": "이사 전후로 남은 가구, 생활폐기물, 사용하지 않는 물건들을 분류하고 반출하는 작업이었습니다.",
    "폐업폐기물처리": "폐업 현장에 남은 집기류, 선반, 사무용품, 생활폐기물을 분류하고 반출하는 방식으로 진행했습니다.",
    "쓰레기집청소": "오랜 기간 방치된 생활쓰레기와 오염된 물품을 분류하고, 폐기물 반출과 공간 정리를 함께 진행했습니다.",
}

before_problem = {
    "가정폐기물처리": "작업 전에는 생활용품과 오래된 가구가 섞여 있어 혼자 정리하기 어려운 상태였습니다.",
    "이사폐기물처리": "이사 후 남은 짐과 폐기물이 한 공간에 모여 있어 반출 동선 정리가 먼저 필요한 상황이었습니다.",
    "폐업폐기물처리": "폐업 후 남은 집기류와 폐기물이 분리되지 않은 상태라 종류별 분류가 필요한 현장이었습니다.",
    "쓰레기집청소": "생활쓰레기가 오래 방치되어 냄새와 오염이 함께 있었고, 폐기물 분류와 반출이 동시에 필요한 상황이었습니다.",
}

after_result = {
    "가정폐기물처리": "사용하지 않는 생활폐기물을 반출한 뒤 공간이 넓어지고 정리가 쉬운 상태로 마무리되었습니다.",
    "이사폐기물처리": "남은 폐기물을 정리한 뒤 이사 후 공간을 다시 사용할 수 있도록 정돈했습니다.",
    "폐업폐기물처리": "집기류와 폐기물을 정리한 뒤 다음 정리나 철거 작업이 가능하도록 현장을 마무리했습니다.",
    "쓰레기집청소": "방치된 쓰레기를 반출하고 남은 공간을 확인해 이후 청소와 정돈이 가능하도록 정리했습니다.",
}


def img_num(index, offset):
    return ((index + offset) % CASE_IMAGE_COUNT) + 1


def case_before(index, offset=0):
    return f"/images/cases/waste-before-{img_num(index, offset):03d}.jpg"


def case_after(index, offset=0):
    return f"/images/cases/waste-after-{img_num(index, offset):03d}.jpg"


def review_slug(slug, service):
    return f"{slug}-{service_slug[service]}"


def related_reviews(current_slug):
    items = []
    for region, slug, service in reviews:
        if slug == current_slug:
            continue
        items.append(f'<a href="/reviews/{review_slug(slug, service)}.html">{region} {service} 후기</a>')
        if len(items) >= 12:
            break
    return "\n".join(items)


def type_content(region, service, type_index):
    if type_index == 0:
        return f"""
        <div class="review-summary-box">
          <p>이번 현장은 <strong>{region} {service}</strong> 문의로 접수된 작업입니다. 사진으로 현장 상태를 먼저 확인한 뒤 폐기물의 양, 건물 구조, 반출 동선, 층수와 엘리베이터 유무를 기준으로 작업 범위를 안내드렸습니다.</p>
          <p>{service_desc[service]}</p>
        </div>
        """
    if type_index == 1:
        return f"""
        <div class="review-summary-box">
          <p><strong>{region} {service}</strong> 비용은 단순히 폐기물 양만 보고 결정하기 어렵습니다. 같은 1톤 분량이라도 층수, 엘리베이터 유무, 차량 진입 가능 여부, 분류 난이도에 따라 작업 시간과 인력이 달라집니다.</p>
          <p>이번 현장도 사진 상담 후 반출 동선을 먼저 확인했고, 정리 범위를 나눈 뒤 작업 순서를 잡아 비용이 과하게 늘어나지 않도록 진행했습니다.</p>
        </div>
        """
    if type_index == 2:
        return f"""
        <div class="review-summary-box">
          <p>처음 상담에서는 {region} 현장의 폐기물 양을 정확히 알기 어려워 사진을 먼저 요청드렸습니다. 이후 주소, 건물 형태, 엘리베이터 유무, 차량 접근 가능 여부를 확인한 뒤 {service} 작업 일정을 조율했습니다.</p>
          <p>상담 단계에서 가능한 부분과 현장에서 추가 확인이 필요한 부분을 나누어 안내드려 작업 당일 혼선이 없도록 준비했습니다.</p>
        </div>
        """
    return f"""
        <div class="review-summary-box">
          <p>{region}에서 {service}를 준비할 때는 폐기물 양, 층수, 엘리베이터 유무, 주차 가능 여부를 먼저 확인하는 것이 좋습니다. 이 정보가 있으면 상담과 비용 안내가 훨씬 빠르게 진행됩니다.</p>
          <p>이번 현장도 사진과 기본 정보를 먼저 확인한 뒤, 작업 전 분류가 필요한 물품과 바로 반출 가능한 물품을 나누어 정리했습니다.</p>
        </div>
        """


def review_html(region, slug, service, index):
    type_index = index % 4
    type_name = type_names[type_index]
    rslug = review_slug(slug, service)
    url = f"{BASE_URL}/reviews/{rslug}.html"
    title = f"{region} {service} 작업후기 | 가족애 폐기물처리"
    desc = f"{region} {service} {type_name}입니다. 작업 전후 사진, 현장 상황, 폐기물처리 비용 기준, 상담 방법을 확인하실 수 있습니다."

    before1 = case_before(index, 0)
    before2 = case_before(index, 23)
    middle1 = case_before(index, 47)
    middle2 = case_after(index, 9)
    after1 = case_after(index, 17)
    after2 = case_after(index, 41)

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <link rel="icon" href="/favicon.ico">
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="keywords" content="{region} {service}, {region} 폐기물처리, {region} 작업후기, {region} 가정폐기물처리, {region} 쓰레기집청소, {region} 폐업폐기물처리" />

  <meta property="og:type" content="article" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:site_name" content="가족애 폐기물처리" />
  <meta property="og:image" content="{BASE_URL}/og-image.jpg" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <meta name="twitter:image" content="{BASE_URL}/og-image.jpg" />

  <link rel="canonical" href="{url}" />
  <link rel="stylesheet" href="../style.css" />

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{desc}",
    "image": "{BASE_URL}/og-image.jpg",
    "author": {{"@type": "Organization", "name": "가족애 폐기물처리"}},
    "publisher": {{"@type": "Organization", "name": "가족애 폐기물처리"}},
    "mainEntityOfPage": {{"@type": "WebPage", "@id": "{url}"}}
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "{region} {service} 비용은 얼마부터인가요?",
        "acceptedAnswer": {{"@type": "Answer", "text": "폐기물처리 비용은 1톤 트럭 1대 기준 25만원부터이며, 폐기물의 양, 층수, 엘리베이터 유무, 작업 공간의 넓이에 따라 달라질 수 있습니다."}}
      }},
      {{
        "@type": "Question",
        "name": "{region} 지역도 사진 상담이 가능한가요?",
        "acceptedAnswer": {{"@type": "Answer", "text": "네. 폐기물 사진, 지역, 층수, 엘리베이터 유무를 알려주시면 상담이 가능합니다."}}
      }}
    ]
  }}
  </script>
</head>

<body>
  <header class="site-header">
    <nav class="site-nav">
      <a href="/" class="site-logo">가족애 폐기물처리</a>
      <div class="site-menu">
        <a href="/">메인</a>
        <a href="/#services">서비스</a>
        <a href="/#photos">작업사진</a>
        <a href="/#region">지역안내</a>
        <a href="/reviews/index.html">작업후기</a>
        <a href="#contact">상담접수</a>
      </div>
    </nav>
  </header>

  <header class="hero region-hero">
    <div class="hero-inner">
      <p class="badge">{region} {type_name}</p>
      <h1>{region} {service} 작업후기</h1>
      <p class="hero-text">
        작업 전 확인부터 분류, 반출, 마무리까지<br />
        실제 현장 흐름에 맞춰 정리한 폐기물처리 사례입니다.
      </p>
      <a href="tel:{PHONE}" class="main-btn">상담전화 {PHONE}</a>
    </div>
  </header>

  <main>
    <section class="section review-summary">
      <p class="section-label">현장요약</p>
      <h2>{region} {service} 현장 상황</h2>
      {type_content(region, service, type_index)}
    </section>

    <section class="section review-before-after">
      <p class="section-label">작업사진</p>
      <h2>{region} {service} 작업 전·중·후 사진</h2>
      <p class="section-desc">작업 전 상태, 분류 과정, 작업 후 정리 완료 모습을 함께 확인할 수 있도록 구성했습니다.</p>

      <div class="before-after-grid">
        <figure>
          <img src="{before1}" alt="{region} {service} 작업 전 폐기물 현장 사진 1" loading="lazy">
          <figcaption>작업 전 현장 상태</figcaption>
        </figure>
        <figure>
          <img src="{before2}" alt="{region} {service} 작업 전 폐기물 현장 사진 2" loading="lazy">
          <figcaption>분류 전 폐기물 상태</figcaption>
        </figure>
        <figure>
          <img src="{middle1}" alt="{region} {service} 폐기물 분류 과정 사진 1" loading="lazy">
          <figcaption>폐기물 분류 과정</figcaption>
        </figure>
        <figure>
          <img src="{middle2}" alt="{region} {service} 폐기물 반출 과정 사진 2" loading="lazy">
          <figcaption>반출 및 정리 과정</figcaption>
        </figure>
        <figure>
          <img src="{after1}" alt="{region} {service} 작업 후 정리 완료 사진 1" loading="lazy">
          <figcaption>작업 후 정리 완료</figcaption>
        </figure>
        <figure>
          <img src="{after2}" alt="{region} {service} 작업 후 정리 완료 사진 2" loading="lazy">
          <figcaption>마무리 확인</figcaption>
        </figure>
      </div>
    </section>

    <section class="section review-story">
      <p class="section-label">작업내용</p>
      <h2>{region} 현장 작업 내용</h2>

      <div class="story-grid">
        <div class="story-card">
          <span>01</span>
          <h3>작업 전 상태</h3>
          <p>{before_problem[service]}</p>
        </div>
        <div class="story-card">
          <span>02</span>
          <h3>분류와 반출</h3>
          <p>폐기물 종류를 먼저 구분하고, 큰 가구와 생활폐기물을 순서대로 정리했습니다. 반출 동선에 맞춰 작업 순서를 잡아 현장 부담을 줄였습니다.</p>
        </div>
        <div class="story-card">
          <span>03</span>
          <h3>작업 후 변화</h3>
          <p>{after_result[service]}</p>
        </div>
      </div>
    </section>

    <section class="section price">
      <h2>{region} {service} 비용 안내</h2>
      <div class="price-box">
        <p class="price-main">1톤 트럭 1대 기준 <strong>25만원부터</strong></p>
        <p>같은 {service} 작업이라도 폐기물의 양, 건물 형태, 층수, 엘리베이터 유무, 작업 공간의 넓이와 차량 진입 가능 여부에 따라 비용은 달라질 수 있습니다.</p>
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

    <section class="section seo-link-section">
      <p class="section-label">내부링크</p>
      <h2>{region} 폐기물처리 관련 링크</h2>
      <p>현재 후기와 관련된 지역 페이지와 다른 작업후기를 함께 확인하실 수 있습니다.</p>

      <div class="backlink-box">
        <a href="/regions/{slug}.html">{region} 폐기물처리 안내</a>
        <a href="/reviews/index.html">작업후기 전체보기</a>
        <a href="/">가족애 폐기물처리 메인</a>
        {related_reviews(slug)}
      </div>
    </section>

    <section class="section contact-form-section" id="contact">
      <div class="contact-layout">
        <div class="contact-info-box">
          <p class="section-label">상담접수</p>
          <h2>{region} {service} 상담 접수</h2>
          <p>사진, 주소, 폐기물 양을 남겨주시면 현장 확인 후 연락드립니다.</p>
          <strong class="contact-phone">{PHONE}</strong>
          <ul>
            <li>✓ 가정폐기물 · 이사폐기물</li>
            <li>✓ 쓰레기집청소 · 빈집정리</li>
            <li>✓ 폐업폐기물 · 사무실 집기정리</li>
          </ul>
        </div>

        <form class="contact-form" id="contactForm"><input type="hidden" name="raw_message" id="mailMessage">
          <input type="hidden" name="메시지" id="mailMessageKr"><div class="form-row">
            <label for="name">성함</label>
            <input type="text" id="name" name="name" placeholder="성함을 입력해주세요" required>
          </div>
          <div class="form-row">
            <label for="phone">연락처</label>
            <input type="tel" id="phone" name="phone" placeholder="010-0000-0000" required>
          </div>
          <div class="form-row">
            <label for="region">지역</label>
            <input type="text" id="region" name="region" value="{region}" required>
          </div>
          <div class="form-row">
            <label for="service">필요 서비스</label>
            <select id="service" name="service" required>
              <option value="{service}" selected>{service}</option>
              <option value="가정폐기물처리">가정폐기물처리</option>
              <option value="이사폐기물처리">이사폐기물처리</option>
              <option value="폐업폐기물처리">폐업폐기물처리</option>
              <option value="쓰레기집청소">쓰레기집청소</option>
              <option value="기타 폐기물처리">기타 폐기물처리</option>
            </select>
          </div>
          <div class="form-row full">
            <label for="message">현장 상황</label>
            <textarea id="message" name="raw_message" rows="5" placeholder="폐기물 양, 층수, 엘리베이터 유무, 사진 전달 가능 여부 등을 적어주세요."></textarea>
          </div>

          <div class="privacy-box">
            <div class="privacy-title">개인정보 수집 및 이용 동의</div>
            <div class="privacy-content">
              <p>가족애 폐기물처리는 상담 접수 및 문의 응대를 위해 아래와 같이 개인정보를 수집·이용합니다.</p>
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
        </form>
      </div>
    </section>

    <section class="section faq">
      <h2>{region} {service} 자주 묻는 질문</h2>
      <div class="faq-item">
        <h3>{region} {service} 비용은 얼마부터인가요?</h3>
        <p>폐기물처리 비용은 1톤 트럭 1대 기준 25만원부터입니다. 폐기물의 양과 현장 상황에 따라 실제 비용은 달라질 수 있습니다.</p>
      </div>
      <div class="faq-item">
        <h3>사진만 보내도 상담이 가능한가요?</h3>
        <p>가능합니다. 폐기물 사진, 지역, 층수, 엘리베이터 유무를 알려주시면 작업 가능 여부와 대략적인 범위 안내가 가능합니다.</p>
      </div>
      <div class="faq-item">
        <h3>{region} 지역도 빠른 상담이 가능한가요?</h3>
        <p>네. {region} 및 인근 지역 폐기물처리 상담이 가능합니다. 빠른 상담은 {PHONE}로 연락주시면 됩니다.</p>
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

<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>

<script>
(function () {{
  emailjs.init("{EMAILJS_PUBLIC_KEY}");

  document.addEventListener("DOMContentLoaded", function () {{
    const form = document.getElementById("contactForm");
    if (!form) return;

    form.addEventListener("submit", function (e) {{
      e.preventDefault();

      const btn = form.querySelector(".form-btn");
      const originalText = btn.textContent;

      btn.disabled = true;
      btn.textContent = "접수 중입니다...";

      const name = form.querySelector('[name="name"]')?.value || "";
      const phone = form.querySelector('[name="phone"]')?.value || "";
      const region = form.querySelector('[name="region"]')?.value || "";
      const service = form.querySelector('[name="service"]')?.value || "";

      const content =
        form.querySelector("textarea")?.value ||
        form.querySelector('[name="message"]')?.value ||
        form.querySelector('[name="raw_message"]')?.value ||
        form.querySelector('[name="내용"]')?.value ||
        form.querySelector('[name="문의내용"]')?.value ||
        "";

      const messageText = [
        "접수 사이트: 가족애 폐기물처리",
        "",
        "이름: " + name,
        "",
        "연락처: " + phone,
        "",
        "지역: " + region,
        "",
        "요청 서비스: " + service,
        "",
        "상담 내용:",
        content,
        "",
        "접수 페이지:",
        window.location.href
      ].join("\\n");

      const params = {{
        title: "[가족애 폐기물처리] " + region + " " + service + " 상담접수",
        site_name: "가족애 폐기물처리",
        name: name,
        email: "bg.jin78@gmail.com",
        message: messageText
      }};

      emailjs.send("{EMAILJS_SERVICE_ID}", "{EMAILJS_TEMPLATE_ID}", params)
        .then(function () {{
          alert("상담 접수가 완료되었습니다.");
          form.reset();
        }})
        .catch(function (error) {{
          console.error(error);
          alert("전송 중 오류가 발생했습니다.");
        }})
        .finally(function () {{
          btn.disabled = false;
          btn.textContent = originalText;
        }});
    }});
  }});
}})();
</script>
</script>
</body>
</html>
"""


def create_reviews_index():
    items = ""
    for region, slug, service in reviews:
        items += f'<a href="/reviews/{review_slug(slug, service)}.html">{region} {service} 작업후기</a>\n'

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <link rel="icon" href="/favicon.ico">
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>폐기물처리 작업후기 | 가족애 폐기물처리</title>
  <meta name="description" content="부산·경남·울산 폐기물처리 작업후기 모음입니다. 가정폐기물처리, 이사폐기물처리, 폐업폐기물처리, 쓰레기집청소 사례를 확인하세요." />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="폐기물처리 작업후기 | 가족애 폐기물처리" />
  <meta property="og:description" content="부산·경남·울산 지역별 폐기물처리 작업후기 모음입니다." />
  <meta property="og:url" content="{BASE_URL}/reviews/index.html" />
  <meta property="og:image" content="{BASE_URL}/og-image.jpg" />
  <link rel="canonical" href="{BASE_URL}/reviews/index.html" />
  <link rel="stylesheet" href="../style.css" />
</head>
<body>
  <header class="site-header">
    <nav class="site-nav">
      <a href="/" class="site-logo">가족애 폐기물처리</a>
      <div class="site-menu">
        <a href="/">메인</a>
        <a href="/#services">서비스</a>
        <a href="/#region">지역안내</a>
        <a href="/reviews/index.html">작업후기</a>
        <a href="tel:{PHONE}">상담전화</a>
      </div>
    </nav>
  </header>
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


def read_existing_sitemap_urls():
    urls = []
    if os.path.exists("sitemap.xml"):
        with open("sitemap.xml", "r", encoding="utf-8") as f:
            old = f.read()
        for line in old.splitlines():
            if "<loc>" in line:
                url = line.replace("<loc>", "").replace("</loc>", "").strip()
                if url and url not in urls:
                    urls.append(url)
    return urls


def update_sitemap():
    urls = read_existing_sitemap_urls()
    review_urls = [f"{BASE_URL}/reviews/index.html"]
    review_urls += [f"{BASE_URL}/reviews/{review_slug(slug, service)}.html" for region, slug, service in reviews]
    for url in review_urls:
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
        items += f"""
    <item>
      <title>{region} {service} 작업후기</title>
      <link>{BASE_URL}/reviews/{review_slug(slug, service)}.html</link>
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
    os.makedirs("images/main", exist_ok=True)
    os.makedirs("images/cases", exist_ok=True)

    for index, (region, slug, service) in enumerate(reviews):
        path = f"reviews/{review_slug(slug, service)}.html"
        with open(path, "w", encoding="utf-8") as f:
            f.write(review_html(region, slug, service, index))

    create_reviews_index()
    update_sitemap()
    update_rss()

    print(f"완료: 작업후기 {len(reviews)}개 생성")
    print("완료: 4가지 후기 유형 랜덤화 적용")
    print("완료: 작업 전/중/후 사진 6장 적용")
    print("완료: 상담폼 / 내부링크 / sitemap / rss 적용")


if __name__ == "__main__":
    main()
