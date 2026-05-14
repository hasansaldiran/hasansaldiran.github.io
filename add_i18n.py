# -*- coding: utf-8 -*-
"""
add_i18n.py  —  Hasansaldiran.github.io TR/EN dil geçiş sistemi
Çalıştır: python add_i18n.py
"""

import re

INPUT  = "index.html"
OUTPUT = "index.html"

with open(INPUT, encoding="utf-8") as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# 1.  <html lang="tr">  →  <html lang="tr" id="root">
# ─────────────────────────────────────────────────────────────────────────────
html = html.replace('<html lang="tr">', '<html lang="tr" id="root">', 1)

# ─────────────────────────────────────────────────────────────────────────────
# 2.  <title> — bilingual
# ─────────────────────────────────────────────────────────────────────────────
html = html.replace(
    '<title>Hasan Saldıran — BT Sistemleri &amp; Güvenlik Uzmanı</title>',
    '<title id="page-title">Hasan Saldıran — BT Sistemleri &amp; Güvenlik Uzmanı</title>',
    1
)

# ─────────────────────────────────────────────────────────────────────────────
# 3.  CSS for language toggle button  (insert right before </style>)
# ─────────────────────────────────────────────────────────────────────────────
LANG_CSS = """
/* ── LANG TOGGLE ── */
#lang-toggle {
  font-family: var(--mono);
  font-size: 0.68rem;
  letter-spacing: 0.1em;
  padding: 0.3rem 0.7rem;
  border: 1px solid var(--border);
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  transition: all 0.2s;
  margin-left: 1.5rem;
  white-space: nowrap;
}
#lang-toggle:hover {
  border-color: var(--accent);
  color: var(--accent);
}
[data-lang-hide] { display: none !important; }
"""
html = html.replace("</style>", LANG_CSS + "\n</style>", 1)

# ─────────────────────────────────────────────────────────────────────────────
# 4.  Nav — add lang toggle button after </ul>
# ─────────────────────────────────────────────────────────────────────────────
html = html.replace(
    '</ul>\n</nav>',
    '</ul>\n  <button id="lang-toggle" onclick="toggleLang()" title="Switch language">EN</button>\n</nav>',
    1
)

# ─────────────────────────────────────────────────────────────────────────────
# 5.  All visible Turkish text — replace with i18n spans
#     Strategy: targeted find-replace for each user-visible string.
# ─────────────────────────────────────────────────────────────────────────────

def i18n(tr_text, en_text):
    """Return a span pair that toggles between TR and EN."""
    return (
        f'<span data-tr>{tr_text}</span>'
        f'<span data-en data-lang-hide>{en_text}</span>'
    )

# Helper: replace a literal string in html with i18n span pair
def rep(old, tr_text, en_text):
    global html
    new = i18n(tr_text, en_text)
    if old in html:
        html = html.replace(old, new, 1)
    else:
        print(f"[WARN] not found: {old[:60]!r}")

# ── HERO ────────────────────────────────────────────────────────────────────
rep(
    '<p class="hero-pre">BT Sistemleri &amp; Güvenlik Uzmanı</p>',
    '<p class="hero-pre">BT Sistemleri &amp; Güvenlik Uzmanı</p>',
    '<p class="hero-pre">IT Systems &amp; Security Specialist</p>'
)

rep(
    '<strong>Bilgisayar Mühendisi.</strong> Kurumsal BT altyapısını güvende tutar, risk motorları ve otomasyon sistemleri inşa eder. <span style="color:var(--accent)">Python</span>, <span style="color:var(--accent)">C#</span>, <span style="color:var(--accent)">MITRE ATT&amp;CK</span> üzerine çalışır.',
    '<strong>Bilgisayar Mühendisi.</strong> Kurumsal BT altyapısını güvende tutar, risk motorları ve otomasyon sistemleri inşa eder. <span style="color:var(--accent)">Python</span>, <span style="color:var(--accent)">C#</span>, <span style="color:var(--accent)">MITRE ATT&amp;CK</span> üzerine çalışır.',
    '<strong>Computer Engineer.</strong> Secures enterprise IT infrastructure and builds risk engines and automation systems. Works with <span style="color:var(--accent)">Python</span>, <span style="color:var(--accent)">C#</span>, <span style="color:var(--accent)">MITRE ATT&amp;CK</span>.'
)

rep(
    '<a href="#projects" class="btn btn-primary">Projeleri Gör →</a>',
    '<a href="#projects" class="btn btn-primary">Projeleri Gör →</a>',
    '<a href="#projects" class="btn btn-primary">View Projects →</a>'
)

rep(
    '<a href="#contact" class="btn">İletişim</a>',
    '<a href="#contact" class="btn">İletişim</a>',
    '<a href="#contact" class="btn">Contact</a>'
)

# Stats labels
rep('<span class="hstat-label">Yıl Deneyim</span>',
    '<span class="hstat-label">Yıl Deneyim</span>',
    '<span class="hstat-label">Years Experience</span>')

rep('<span class="hstat-label">Kullanıcı+</span>',
    '<span class="hstat-label">Kullanıcı+</span>',
    '<span class="hstat-label">Users+</span>')

rep('<span class="hstat-label">BT Varlığı+</span>',
    '<span class="hstat-label">BT Varlığı+</span>',
    '<span class="hstat-label">IT Assets+</span>')

# ── ABOUT ───────────────────────────────────────────────────────────────────
rep(
    '<h2 class="section-title">Hakkımda</h2>',
    '<h2 class="section-title">Hakkımda</h2>',
    '<h2 class="section-title">About</h2>'
)

rep(
    '<strong>Bilgisayar Mühendisliği</strong> altyapısına sahip, sistem mühendisliği kariyeri hedefleyen BT ve güvenlik uzmanıyım. Kariyerime kullanıcıyla birebir temasa geçerek, kritik sistemlerin içinden başladım — bunu kasıtlı bir tercih olarak görüyorum.',
    '<strong>Bilgisayar Mühendisliği</strong> altyapısına sahip, sistem mühendisliği kariyeri hedefleyen BT ve güvenlik uzmanıyım. Kariyerime kullanıcıyla birebir temasa geçerek, kritik sistemlerin içinden başladım — bunu kasıtlı bir tercih olarak görüyorum.',
    'I am an IT and security specialist with a <strong>Computer Engineering</strong> background, aiming for a career in systems engineering. I deliberately started my career at the front lines — in direct contact with users and critical systems.'
)

rep(
    '<span class="hl">Dünyagöz Hastaneler Grubu</span>\'nda 2.000+ kullanıcı ve 2.250+ BT varlığını kapsayan kurumsal sağlık altyapısını yönetiyorum. Sadece destek vermekle kalmayıp, kendi inisiyatifimle <span class="hl">Python</span> ile MITRE ATT&CK ve CIS Controls v8 çerçevelerine dayalı kurumsal risk yönetim sistemi geliştirdim.',
    '<span class="hl">Dünyagöz Hastaneler Grubu</span>\'nda 2.000+ kullanıcı ve 2.250+ BT varlığını kapsayan kurumsal sağlık altyapısını yönetiyorum. Sadece destek vermekle kalmayıp, kendi inisiyatifimle <span class="hl">Python</span> ile MITRE ATT&CK ve CIS Controls v8 çerçevelerine dayalı kurumsal risk yönetim sistemi geliştirdim.',
    'At <span class="hl">Dünyagöz Hastaneler Grubu</span> I manage enterprise healthcare infrastructure covering 2,000+ users and 2,250+ IT assets. Beyond support, I proactively built an enterprise risk management system in <span class="hl">Python</span> based on MITRE ATT&CK and CIS Controls v8 frameworks.'
)

rep(
    'Öncesinde <span class="hl">Çok Uluslu Müşterek Harp Merkezi Komutanlığı</span>\'nda NATO tatbikatlarına ev sahipliği yapan uluslararası askeri ortamda 500\'ü aşan çok uluslu katılımcıya gerçek zamanlı teknik destek sağladım.',
    'Öncesinde <span class="hl">Çok Uluslu Müşterek Harp Merkezi Komutanlığı</span>\'nda NATO tatbikatlarına ev sahipliği yapan uluslararası askeri ortamda 500\'ü aşan çok uluslu katılımcıya gerçek zamanlı teknik destek sağladım.',
    'Previously, at the <span class="hl">Multinational Joint Warfare Centre Command</span>, I provided real-time technical support to 500+ multinational participants in an international military environment hosting NATO exercises.'
)

rep(
    'Kodu bir sorun çözme aracı olarak görüyorum — uçtan uca sahiplenerek, ölçülebilir çıktılara odaklanarak.',
    'Kodu bir sorun çözme aracı olarak görüyorum — uçtan uca sahiplenerek, ölçülebilir çıktılara odaklanarak.',
    'I see code as a problem-solving tool — owning it end-to-end and focusing on measurable outcomes.'
)

# Terminal card — field names
rep(
    '<span class="t-key">"ad"</span>',
    '<span class="t-key">"ad"</span>',
    '<span class="t-key">"name"</span>'
)
rep(
    '<span class="t-key">"konum"</span>',
    '<span class="t-key">"konum"</span>',
    '<span class="t-key">"location"</span>'
)
rep(
    '<span class="t-key">"pozisyon"</span>',
    '<span class="t-key">"pozisyon"</span>',
    '<span class="t-key">"position"</span>'
)
rep(
    '<span class="t-key">"şirket"</span>',
    '<span class="t-key">"şirket"</span>',
    '<span class="t-key">"company"</span>'
)
rep(
    '<span class="t-key">"deneyim"</span>',
    '<span class="t-key">"deneyim"</span>',
    '<span class="t-key">"experience"</span>'
)
rep(
    '<span class="t-key">"uzmanlık"</span>',
    '<span class="t-key">"uzmanlık"</span>',
    '<span class="t-key">"expertise"</span>'
)
rep(
    '<span class="t-key">"hedef"</span>',
    '<span class="t-key">"hedef"</span>',
    '<span class="t-key">"goal"</span>'
)
rep(
    '<span class="t-key">"durum"</span>',
    '<span class="t-key">"durum"</span>',
    '<span class="t-key">"status"</span>'
)
rep(
    '<span class="t-str">"BT Sistemleri &amp; Güvenlik Uzmanı"</span>',
    '<span class="t-str">"BT Sistemleri &amp; Güvenlik Uzmanı"</span>',
    '<span class="t-str">"IT Systems &amp; Security Specialist"</span>'
)
rep(
    '<span class="t-str">"2+ yıl"</span>',
    '<span class="t-str">"2+ yıl"</span>',
    '<span class="t-str">"2+ years"</span>'
)
rep(
    '<span class="t-str">"Sistem Mühendisliği"</span>',
    '<span class="t-str">"Sistem Mühendisliği"</span>',
    '<span class="t-str">"Systems Engineering"</span>'
)

# ── EXPERIENCE ───────────────────────────────────────────────────────────────
rep(
    '<h2 class="section-title">Deneyim</h2>',
    '<h2 class="section-title">Deneyim</h2>',
    '<h2 class="section-title">Experience</h2>'
)

rep('<div class="exp-period">Mar 2025 — Halen</div>',
    '<div class="exp-period">Mar 2025 — Halen</div>',
    '<div class="exp-period">Mar 2025 — Present</div>')

rep('<span class="exp-type">Tam Zamanlı</span>\n        </div>\n        <div class="exp-content">\n          <div class="exp-role">Sistem Geliştirme & Kullanıcı Destek Uzmanı</div>',
    '<span class="exp-type">Tam Zamanlı</span>',
    '<span class="exp-type">Full-Time</span>')

# Dünyagöz role
rep(
    '<div class="exp-role">Sistem Geliştirme & Kullanıcı Destek Uzmanı</div>',
    '<div class="exp-role">Sistem Geliştirme &amp; Kullanıcı Destek Uzmanı</div>',
    '<div class="exp-role">System Development &amp; User Support Specialist</div>'
)

rep(
    '<p class="exp-desc">2.000+ hastane personeli ve 2.250+ BT varlığını kapsayan kurumsal sağlık altyapısında L1/L2 teknik destek ve sistem yönetimi. Pusula HBYS yönetimi, Python ile MITRE ATT&CK + CIS Controls v8 tabanlı risk motoru, kimlik kartı otomasyon sistemi ve Power BI yönetici panosu geliştirme.</p>',
    '<p class="exp-desc">2.000+ hastane personeli ve 2.250+ BT varlığını kapsayan kurumsal sağlık altyapısında L1/L2 teknik destek ve sistem yönetimi. Pusula HBYS yönetimi, Python ile MITRE ATT&CK + CIS Controls v8 tabanlı risk motoru, kimlik kartı otomasyon sistemi ve Power BI yönetici panosu geliştirme.</p>',
    '<p class="exp-desc">L1/L2 technical support and system management for enterprise healthcare infrastructure covering 2,000+ hospital staff and 2,250+ IT assets. Pusula HIS management, Python-based MITRE ATT&CK + CIS Controls v8 risk engine, ID card automation system, and Power BI executive dashboard development.</p>'
)

# ÇMHM
rep('<div class="exp-period">Mar 2024 — Şub 2025</div>',
    '<div class="exp-period">Mar 2024 — Şub 2025</div>',
    '<div class="exp-period">Mar 2024 — Feb 2025</div>')

rep(
    '<div class="exp-role">Bilgi Sistemleri Güvenlik Uzmanı</div>',
    '<div class="exp-role">Bilgi Sistemleri Güvenlik Uzmanı</div>',
    '<div class="exp-role">Information Systems Security Specialist</div>'
)

rep(
    '<p class="exp-desc">NATO tatbikatlarına ev sahipliği yapan TSK bünyesindeki uluslararası askeri merkezde 100+ sabit personel ve yılda 10–15 etkinlikte 20–500+ çok uluslu katılımcıya gerçek zamanlı teknik destek. Ağ altyapısı kurulumu, cihaz yönetimi, erişim kontrolü ve bilgi güvenliği operasyonları.</p>',
    '<p class="exp-desc">NATO tatbikatlarına ev sahipliği yapan TSK bünyesindeki uluslararası askeri merkezde 100+ sabit personel ve yılda 10–15 etkinlikte 20–500+ çok uluslu katılımcıya gerçek zamanlı teknik destek. Ağ altyapısı kurulumu, cihaz yönetimi, erişim kontrolü ve bilgi güvenliği operasyonları.</p>',
    '<p class="exp-desc">Real-time technical support for 100+ permanent staff and 20–500+ multinational participants across 10–15 annual events at an international military centre hosting NATO exercises. Network infrastructure deployment, device management, access control, and information security operations.</p>'
)

# İBB staj
rep('<div class="exp-period">Tem 2022 — Eyl 2022</div>',
    '<div class="exp-period">Tem 2022 — Eyl 2022</div>',
    '<div class="exp-period">Jul 2022 — Sep 2022</div>')

rep('<span class="exp-type">Staj</span>\n        </div>\n        <div class="exp-content">\n          <div class="exp-role">Bilgi İşlem Stajyeri</div>\n          <p class="exp-desc">Flask + NLP',
    '<div class="exp-role">Bilgi İşlem Stajyeri</div>\n          <p class="exp-desc">Flask + NLP ile İBB Beyaz Masa Chatbot prototipi ve OpenCV ile toplu taşımada araç/yolcu tespiti uygulaması geliştirdim.</p>',
    '<div class="exp-role">IT Intern</div>\n          <p class="exp-desc">Developed an İBB White Desk Chatbot prototype using Flask + NLP, and a vehicle/passenger detection application for public transit using OpenCV.</p>'
)

# Burulaş
rep('<div class="exp-period">Şub 2020 — Mar 2020</div>',
    '<div class="exp-period">Şub 2020 — Mar 2020</div>',
    '<div class="exp-period">Feb 2020 — Mar 2020</div>')

rep(
    '<div class="exp-role">Bilgi Sistemleri Stajyeri</div>\n          <p class="exp-desc">ASP.NET ile kurumsal web uygulamaları geliştirerek toplu taşıma bilgi sistemleri altyapısını destekledim.</p>',
    '<div class="exp-role">Bilgi Sistemleri Stajyeri</div>\n          <p class="exp-desc">ASP.NET ile kurumsal web uygulamaları geliştirerek toplu taşıma bilgi sistemleri altyapısını destekledim.</p>',
    '<div class="exp-role">Information Systems Intern</div>\n          <p class="exp-desc">Supported public transport information system infrastructure by developing enterprise web applications with ASP.NET.</p>'
)

# İETT
rep('<div class="exp-period">Haz 2019 — Ağu 2019</div>',
    '<div class="exp-period">Haz 2019 — Ağu 2019</div>',
    '<div class="exp-period">Jun 2019 — Aug 2019</div>')

rep(
    '<div class="exp-role">Bilgi İşlem Stajyeri</div>\n          <p class="exp-desc">C# ve MSSQL ile stok takip otomasyon uygulaması tasarladım ve geliştirdim.</p>',
    '<div class="exp-role">Bilgi İşlem Stajyeri</div>\n          <p class="exp-desc">C# ve MSSQL ile stok takip otomasyon uygulaması tasarladım ve geliştirdim.</p>',
    '<div class="exp-role">IT Intern</div>\n          <p class="exp-desc">Designed and developed a stock tracking automation application using C# and MSSQL.</p>'
)

# Exp-type for remaining staj entries (multiple)
html = html.replace(
    '<span class="exp-type">Staj</span>',
    i18n('<span class="exp-type">Staj</span>', '<span class="exp-type">Internship</span>')
)
# Full-Time (multiple) — already done above, fix all remaining
html = html.replace(
    '<span class="exp-type">Tam Zamanlı</span>',
    i18n('<span class="exp-type">Tam Zamanlı</span>', '<span class="exp-type">Full-Time</span>')
)

# ── PROJECTS ─────────────────────────────────────────────────────────────────
rep(
    '<h2 class="section-title">Projeler</h2>',
    '<h2 class="section-title">Projeler</h2>',
    '<h2 class="section-title">Projects</h2>'
)

# Filter buttons
rep('<button class="filter-btn active" data-filter="all">Tümü</button>',
    '<button class="filter-btn active" data-filter="all">Tümü</button>',
    '<button class="filter-btn active" data-filter="all">All</button>')

rep('<button class="filter-btn" data-filter="security">Güvenlik</button>',
    '<button class="filter-btn" data-filter="security">Güvenlik</button>',
    '<button class="filter-btn" data-filter="security">Security</button>')

# Project names & descriptions
proj_replacements = [
    (
        '<div class="proj-name">BT Risk Yönetim Platformu</div>',
        '<div class="proj-name">BT Risk Yönetim Platformu</div>',
        '<div class="proj-name">IT Risk Management Platform</div>'
    ),
    (
        '<p class="proj-desc">Lansweeper + NIST NVD CVE + MITRE ATT&CK + CIS Controls v8 tabanlı kurumsal risk motoru. Z-Score anomali tespiti, Streamlit dashboard, Power BI panosu ve otomatik HTML raporlama.</p>',
        '<p class="proj-desc">Lansweeper + NIST NVD CVE + MITRE ATT&CK + CIS Controls v8 tabanlı kurumsal risk motoru. Z-Score anomali tespiti, Streamlit dashboard, Power BI panosu ve otomatik HTML raporlama.</p>',
        '<p class="proj-desc">Enterprise risk engine based on Lansweeper + NIST NVD CVE + MITRE ATT&CK + CIS Controls v8. Z-Score anomaly detection, Streamlit dashboard, Power BI panel and automated HTML reporting.</p>'
    ),
    (
        '<span class="proj-link">GitHub\'da Gör →</span>',
        '<span class="proj-link">GitHub\'da Gör →</span>',
        '<span class="proj-link">View on GitHub →</span>'
    ),
    (
        '<span class="proj-stars">★ Öne Çıkan</span>',
        '<span class="proj-stars">★ Öne Çıkan</span>',
        '<span class="proj-stars">★ Featured</span>'
    ),
    (
        '<div class="proj-name">İBB Beyaz Masa Chatbot</div>',
        '<div class="proj-name">İBB Beyaz Masa Chatbot</div>',
        '<div class="proj-name">İBB White Desk Chatbot</div>'
    ),
    (
        '<p class="proj-desc">NLTK + Keras + Flask tabanlı Türkçe intent chatbot. Vatandaş taleplerine otomatik yanıt üretmek için İBB Akıllı Şehir Müdürlüğü stajında geliştirildi.</p>',
        '<p class="proj-desc">NLTK + Keras + Flask tabanlı Türkçe intent chatbot. Vatandaş taleplerine otomatik yanıt üretmek için İBB Akıllı Şehir Müdürlüğü stajında geliştirildi.</p>',
        '<p class="proj-desc">Turkish intent chatbot built with NLTK + Keras + Flask. Developed during the İBB Smart City Directorate internship to automatically respond to citizen requests.</p>'
    ),
    (
        '<div class="proj-name">Kimlik Kartı Otomasyon Sistemi</div>',
        '<div class="proj-name">Kimlik Kartı Otomasyon Sistemi</div>',
        '<div class="proj-name">ID Card Automation System</div>'
    ),
    (
        '<p class="proj-desc">Personel kimlik kartı vesikalık yerleşim + sayfa düzeni otomasyonu. python-docx + PyMuPDF ile basım hazırlık süreçlerini otomatize eder.</p>',
        '<p class="proj-desc">Personel kimlik kartı vesikalık yerleşim + sayfa düzeni otomasyonu. python-docx + PyMuPDF ile basım hazırlık süreçlerini otomatize eder.</p>',
        '<p class="proj-desc">Automates ID card photo placement and page layout for print preparation using python-docx + PyMuPDF.</p>'
    ),
    (
        '<div class="proj-name">Vesikalık Tespit (OpenCV)</div>',
        '<div class="proj-name">Vesikalık Tespit (OpenCV)</div>',
        '<div class="proj-name">Passport Photo Detection (OpenCV)</div>'
    ),
    (
        '<p class="proj-desc">Taranan PDF/JPG\'lerden OpenCV ile yüz tespiti ve vesikalık kırpma. Kimlik kartı otomasyon sisteminin görüntü işleme modülü.</p>',
        '<p class="proj-desc">Taranan PDF/JPG\'lerden OpenCV ile yüz tespiti ve vesikalık kırpma. Kimlik kartı otomasyon sisteminin görüntü işleme modülü.</p>',
        '<p class="proj-desc">Face detection and passport photo cropping from scanned PDFs/JPGs using OpenCV. Image processing module for the ID card automation system.</p>'
    ),
    (
        '<div class="proj-name">Araç Tespiti (OpenCV)</div>',
        '<div class="proj-name">Araç Tespiti (OpenCV)</div>',
        '<div class="proj-name">Vehicle Detection (OpenCV)</div>'
    ),
    (
        '<p class="proj-desc">Önceden eğitilmiş Haar Cascade ile video üzerinde gerçek zamanlı araç tespiti. İBB stajı görüntü işleme projesi.</p>',
        '<p class="proj-desc">Önceden eğitilmiş Haar Cascade ile video üzerinde gerçek zamanlı araç tespiti. İBB stajı görüntü işleme projesi.</p>',
        '<p class="proj-desc">Real-time vehicle detection on video using a pre-trained Haar Cascade. Image processing project from the İBB internship.</p>'
    ),
    (
        '<div class="proj-name">Araç Sayma (OpenCV)</div>',
        '<div class="proj-name">Araç Sayma (OpenCV)</div>',
        '<div class="proj-name">Vehicle Counting (OpenCV)</div>'
    ),
    (
        '<p class="proj-desc">OpenCV BackgroundSubtractorMOG2 ile tek şeritte araç sayma demosu. Toplu taşıma veri analizi için geliştirildi.</p>',
        '<p class="proj-desc">OpenCV BackgroundSubtractorMOG2 ile tek şeritte araç sayma demosu. Toplu taşıma veri analizi için geliştirildi.</p>',
        '<p class="proj-desc">Single-lane vehicle counting demo using OpenCV BackgroundSubtractorMOG2. Developed for public transport data analysis.</p>'
    ),
    (
        '<div class="proj-name">Kimlik Otomasyon (Dağıtım)</div>',
        '<div class="proj-name">Kimlik Otomasyon (Dağıtım)</div>',
        '<div class="proj-name">ID Automation (Distribution)</div>'
    ),
    (
        '<p class="proj-desc">Personel vesikalık ZIP dosyalarını personel.xlsx ile eşleştirip şubelere göre otomatik dağıtan araç.</p>',
        '<p class="proj-desc">Personel vesikalık ZIP dosyalarını personel.xlsx ile eşleştirip şubelere göre otomatik dağıtan araç.</p>',
        '<p class="proj-desc">Tool that matches staff photo ZIP files with personel.xlsx and automatically distributes them by branch.</p>'
    ),
    (
        '<div class="proj-name">Kütüphane Otomasyon Sistemi</div>',
        '<div class="proj-name">Kütüphane Otomasyon Sistemi</div>',
        '<div class="proj-name">Library Automation System</div>'
    ),
    (
        '<p class="proj-desc">C# WinForms + SQL Server kütüphane otomasyonu. Kitap, üye ve ödünç yönetimi; stored procedure, trigger ve view içerir.</p>',
        '<p class="proj-desc">C# WinForms + SQL Server kütüphane otomasyonu. Kitap, üye ve ödünç yönetimi; stored procedure, trigger ve view içerir.</p>',
        '<p class="proj-desc">C# WinForms + SQL Server library automation. Book, member and loan management; includes stored procedures, triggers and views.</p>'
    ),
    (
        '<div class="proj-name">Stok Takip Sistemi</div>',
        '<div class="proj-name">Stok Takip Sistemi</div>',
        '<div class="proj-name">Inventory Tracking System</div>'
    ),
    (
        '<p class="proj-desc">C# WinForms + MS Access tabanlı ürün/müşteri/stok takip uygulaması. İETT stajı kapsamında geliştirildi.</p>',
        '<p class="proj-desc">C# WinForms + MS Access tabanlı ürün/müşteri/stok takip uygulaması. İETT stajı kapsamında geliştirildi.</p>',
        '<p class="proj-desc">Product/customer/stock tracking application based on C# WinForms + MS Access. Developed during the İETT internship.</p>'
    ),
    (
        '<div class="proj-name">Market Otomasyon Sistemi</div>',
        '<div class="proj-name">Market Otomasyon Sistemi</div>',
        '<div class="proj-name">Market Automation System</div>'
    ),
    (
        '<p class="proj-desc">VB.NET WinForms + MS Access tabanlı market otomasyonu. Ürün, satış ve stok yönetimi modülleri içerir.</p>',
        '<p class="proj-desc">VB.NET WinForms + MS Access tabanlı market otomasyonu. Ürün, satış ve stok yönetimi modülleri içerir.</p>',
        '<p class="proj-desc">Market automation based on VB.NET WinForms + MS Access. Includes product, sales, and inventory management modules.</p>'
    ),
    (
        '<div class="proj-name">İstanbul Gezi Rehberi</div>',
        '<div class="proj-name">İstanbul Gezi Rehberi</div>',
        '<div class="proj-name">Istanbul Travel Guide</div>'
    ),
    (
        '<p class="proj-desc">ASP.NET WebForms + ASP.NET Core MVC + Google Maps API ile İstanbul gezi rehberi uygulaması.</p>',
        '<p class="proj-desc">ASP.NET WebForms + ASP.NET Core MVC + Google Maps API ile İstanbul gezi rehberi uygulaması.</p>',
        '<p class="proj-desc">Istanbul travel guide application using ASP.NET WebForms + ASP.NET Core MVC + Google Maps API.</p>'
    ),
    (
        '<div class="proj-name">Astronomi Topluluğu Sitesi</div>',
        '<div class="proj-name">Astronomi Topluluğu Sitesi</div>',
        '<div class="proj-name">Astronomy Club Website</div>'
    ),
    (
        '<p class="proj-desc">Uludağ Üniversitesi Astronomi Topluluğu için gönüllü olarak geliştirilen statik web sitesi. uluastro.space arşivi.</p>',
        '<p class="proj-desc">Uludağ Üniversitesi Astronomi Topluluğu için gönüllü olarak geliştirilen statik web sitesi. uluastro.space arşivi.</p>',
        '<p class="proj-desc">Volunteer-developed static website for Uludağ University Astronomy Club. uluastro.space archive.</p>'
    ),
    (
        '<div class="proj-name">Meyve &amp; Sebze Hastalık Tespiti</div>',
        '<div class="proj-name">Meyve &amp; Sebze Hastalık Tespiti</div>',
        '<div class="proj-name">Fruit &amp; Vegetable Disease Detection</div>'
    ),
    (
        '<p class="proj-desc">MobileNetV2 ile 36 sınıf meyve/sebze tanıma; ResNet-9 ile 38 sınıf yaprak hastalık tespiti. Streamlit arayüzü · Flask REST API.</p>',
        '<p class="proj-desc">MobileNetV2 ile 36 sınıf meyve/sebze tanıma; ResNet-9 ile 38 sınıf yaprak hastalık tespiti. Streamlit arayüzü · Flask REST API.</p>',
        '<p class="proj-desc">36-class fruit/vegetable recognition with MobileNetV2; 38-class leaf disease detection with ResNet-9. Streamlit UI · Flask REST API.</p>'
    ),
    (
        '<p class="proj-desc">Türkiye piyasalarına odaklı AI destekli finansal analiz platformu. BIST, TEFAS fon tarayıcı, TCMB makro veriler, portföy yönetimi ve Gemini AI yorumları.</p>',
        '<p class="proj-desc">Türkiye piyasalarına odaklı AI destekli finansal analiz platformu. BIST, TEFAS fon tarayıcı, TCMB makro veriler, portföy yönetimi ve Gemini AI yorumları.</p>',
        '<p class="proj-desc">AI-powered financial analysis platform focused on Turkish markets. BIST, TEFAS fund scanner, TCMB macro data, portfolio management and Gemini AI insights.</p>'
    ),
]

for old, tr_text, en_text in proj_replacements:
    rep(old, tr_text, en_text)

# Handle multiple "GitHub'da Gör →" occurrences (replace all remaining)
html = html.replace(
    '<span class="proj-link">GitHub\'da Gör →</span>',
    i18n('<span class="proj-link">GitHub\'da Gör →</span>', '<span class="proj-link">View on GitHub →</span>')
)
html = html.replace(
    '<span class="proj-stars">★ Öne Çıkan</span>',
    i18n('<span class="proj-stars">★ Öne Çıkan</span>', '<span class="proj-stars">★ Featured</span>')
)

# ── SKILLS ───────────────────────────────────────────────────────────────────
rep(
    '<h2 class="section-title">Yetenekler</h2>',
    '<h2 class="section-title">Yetenekler</h2>',
    '<h2 class="section-title">Skills</h2>'
)

skill_groups = [
    ('Güvenlik &amp; Risk', 'Security &amp; Risk'),
    ('Geliştirme', 'Development'),
    ('Araçlar &amp; Platform', 'Tools &amp; Platform'),
    ('Yapay Zeka &amp; Veri', 'AI &amp; Data'),
    ('Sistem &amp; Altyapı', 'Systems &amp; Infrastructure'),
    ('Sertifika', 'Certifications'),
]
# Note: in the HTML they use & not &amp; inside skill-group-title
skill_groups_raw = [
    ('Güvenlik & Risk', 'Security & Risk'),
    ('Geliştirme', 'Development'),
    ('Araçlar & Platform', 'Tools & Platform'),
    ('Yapay Zeka & Veri', 'AI & Data'),
    ('Sistem & Altyapı', 'Systems & Infrastructure'),
    ('Sertifika', 'Certifications'),
]
for tr_g, en_g in skill_groups_raw:
    rep(
        f'<div class="skill-group-title">{tr_g}</div>',
        f'<div class="skill-group-title">{tr_g}</div>',
        f'<div class="skill-group-title">{en_g}</div>'
    )

skill_items_tr_en = [
    ('Risk Yönetimi', 'Risk Management'),
    ('Erişim Kontrolü', 'Access Control'),
    ('Güvenlik Operasyonları', 'Security Operations'),
    ('Anomali Tespiti', 'Anomaly Detection'),
    ('Makine Öğrenmesi', 'Machine Learning'),
    ('Veri Madenciliği', 'Data Mining'),
    ('Görüntü İşleme', 'Image Processing'),
    ('Ağ Yönetimi', 'Network Management'),
    ('Donanım Yönetimi', 'Hardware Management'),
    ('İHA1 Pilot Lisansı', 'UAS1 Pilot License'),
]
for tr_s, en_s in skill_items_tr_en:
    rep(
        f'<span class="skill-item">{tr_s}</span>',
        f'<span class="skill-item">{tr_s}</span>',
        f'<span class="skill-item">{en_s}</span>'
    )

# Planned certs
html = html.replace(
    '<span class="skill-item" style="border-color:rgba(245,158,11,0.3); color:var(--amber)">ISC2 CC (Planlı)</span>',
    i18n(
        '<span class="skill-item" style="border-color:rgba(245,158,11,0.3); color:var(--amber)">ISC2 CC (Planlı)</span>',
        '<span class="skill-item" style="border-color:rgba(245,158,11,0.3); color:var(--amber)">ISC2 CC (Planned)</span>'
    )
)
html = html.replace(
    '<span class="skill-item" style="border-color:rgba(245,158,11,0.3); color:var(--amber)">BTL1 (Planlı)</span>',
    i18n(
        '<span class="skill-item" style="border-color:rgba(245,158,11,0.3); color:var(--amber)">BTL1 (Planlı)</span>',
        '<span class="skill-item" style="border-color:rgba(245,158,11,0.3); color:var(--amber)">BTL1 (Planned)</span>'
    )
)
html = html.replace(
    '<span class="skill-item" style="border-color:rgba(245,158,11,0.3); color:var(--amber)">CompTIA Sec+ (Planlı)</span>',
    i18n(
        '<span class="skill-item" style="border-color:rgba(245,158,11,0.3); color:var(--amber)">CompTIA Sec+ (Planlı)</span>',
        '<span class="skill-item" style="border-color:rgba(245,158,11,0.3); color:var(--amber)">CompTIA Sec+ (Planned)</span>'
    )
)

# ── BLOG ─────────────────────────────────────────────────────────────────────
rep(
    '<h2 class="section-title">Blog</h2>',
    '<h2 class="section-title">Blog</h2>',
    '<h2 class="section-title">Blog</h2>'  # same in both languages
)

# Blog filter buttons
rep('<button class="blog-filter-btn active" data-filter="all">Tümü</button>',
    '<button class="blog-filter-btn active" data-filter="all">Tümü</button>',
    '<button class="blog-filter-btn active" data-filter="all">All</button>')

rep('<button class="blog-filter-btn" data-filter="Teknoloji">Teknoloji</button>',
    '<button class="blog-filter-btn" data-filter="Teknoloji">Teknoloji</button>',
    '<button class="blog-filter-btn" data-filter="Teknoloji">Technology</button>')

rep('<button class="blog-filter-btn" data-filter="Uzay">Uzay</button>',
    '<button class="blog-filter-btn" data-filter="Uzay">Uzay</button>',
    '<button class="blog-filter-btn" data-filter="Uzay">Space</button>')

rep('<button class="blog-filter-btn" data-filter="Bilim">Bilim</button>',
    '<button class="blog-filter-btn" data-filter="Bilim">Bilim</button>',
    '<button class="blog-filter-btn" data-filter="Bilim">Science</button>')

# Blog card dates
html = html.replace(
    '<span class="blog-date">Nisan 2021</span>',
    i18n('<span class="blog-date">Nisan 2021</span>', '<span class="blog-date">April 2021</span>')
)
html = html.replace(
    '<span class="blog-date">Mayıs 2021</span>',
    i18n('<span class="blog-date">Mayıs 2021</span>', '<span class="blog-date">May 2021</span>')
)
html = html.replace(
    '<span class="blog-date">Haziran 2021</span>',
    i18n('<span class="blog-date">Haziran 2021</span>', '<span class="blog-date">June 2021</span>')
)

# Blog card read times
html = html.replace(
    '<span class="blog-read-time">⏱ 6 dk okuma</span>',
    i18n('<span class="blog-read-time">⏱ 6 dk okuma</span>', '<span class="blog-read-time">⏱ 6 min read</span>')
)
html = html.replace(
    '<span class="blog-read-time">⏱ 8 dk okuma</span>',
    i18n('<span class="blog-read-time">⏱ 8 dk okuma</span>', '<span class="blog-read-time">⏱ 8 min read</span>')
)
html = html.replace(
    '<span class="blog-read-time">⏱ 7 dk okuma</span>',
    i18n('<span class="blog-read-time">⏱ 7 dk okuma</span>', '<span class="blog-read-time">⏱ 7 min read</span>')
)

# Blog card CTAs
html = html.replace(
    '<span class="blog-card-cta">Oku →</span>',
    i18n('<span class="blog-card-cta">Oku →</span>', '<span class="blog-card-cta">Read →</span>')
)

# Blog card titles
blog_titles = [
    ('Veri Madenciliğine Giriş', 'Introduction to Data Mining'),
    ('Veri Madenciliği: Süreç ve Metotlar', 'Data Mining: Process and Methods'),
    ('Blockchain (Blok Zinciri) Teknolojisi Nedir?', 'What Is Blockchain Technology?'),
    ('Türkiye Uzay Ajansını (TUA) Tanıyalım', 'Getting to Know the Turkish Space Agency (TUA)'),
    ('Neuralink: Beyin-Makine Arayüzü Nedir?', 'Neuralink: What Is a Brain-Machine Interface?'),
]
for tr_t, en_t in blog_titles:
    rep(
        f'<h3 class="blog-card-title">{tr_t}</h3>',
        f'<h3 class="blog-card-title">{tr_t}</h3>',
        f'<h3 class="blog-card-title">{en_t}</h3>'
    )

# Blog card excerpts
blog_excerpts = [
    (
        'Veri madenciliğinin tanımı, etimolojisi ve tarihsel gelişimi. Büyük veriden anlamlı bilgiye ulaşmanın temel kavramları.',
        'Definition, etymology, and historical development of data mining. Key concepts for deriving meaningful knowledge from big data.'
    ),
    (
        'Veri madenciliği süreci, CRISP-DM modeli, sınıflama, kümeleme ve birliktelik kuralları metotlarının kapsamlı incelemesi.',
        'Comprehensive examination of the data mining process, CRISP-DM model, classification, clustering, and association rule methods.'
    ),
    (
        'Dağıtık defter teknolojisi, kripto para birimleri ve akıllı sözleşmeler. Blockchain\'in çalışma prensibi ve kullanım alanları.',
        'Distributed ledger technology, cryptocurrencies and smart contracts. How blockchain works and its use cases.'
    ),
    (
        'Türkiye\'nin uzay hedefleri ve TUA\'nın kuruluş hikayesi. Milli uzay programı, roket projeleri ve 2023 hedefleri.',
        "Turkey's space goals and TUA's founding story. The national space program, rocket projects and 2023 targets."
    ),
    (
        'Elon Musk\'ın Neuralink projesi ve beyin-bilgisayar arayüzü teknolojisi. İnsan beynini dijital dünyaya bağlamanın bilimi.',
        "Elon Musk's Neuralink project and brain-computer interface technology. The science of connecting the human brain to the digital world."
    ),
]
for tr_e, en_e in blog_excerpts:
    rep(
        f'<p class="blog-card-excerpt">{tr_e}</p>',
        f'<p class="blog-card-excerpt">{tr_e}</p>',
        f'<p class="blog-card-excerpt">{en_e}</p>'
    )

# Blog modal headers — date strings
html = html.replace(
    '<span class="blog-date">Nisan 2021 · ⏱ 6 dk okuma</span>',
    i18n('<span class="blog-date">Nisan 2021 · ⏱ 6 dk okuma</span>', '<span class="blog-date">April 2021 · ⏱ 6 min read</span>')
)
html = html.replace(
    '<span class="blog-date">Nisan 2021 · ⏱ 8 dk okuma</span>',
    i18n('<span class="blog-date">Nisan 2021 · ⏱ 8 dk okuma</span>', '<span class="blog-date">April 2021 · ⏱ 8 min read</span>')
)
html = html.replace(
    '<span class="blog-date">Mayıs 2021 · ⏱ 7 dk okuma</span>',
    i18n('<span class="blog-date">Mayıs 2021 · ⏱ 7 dk okuma</span>', '<span class="blog-date">May 2021 · ⏱ 7 min read</span>')
)
html = html.replace(
    '<span class="blog-date">Mayıs 2021 · ⏱ 6 dk okuma</span>',
    i18n('<span class="blog-date">Mayıs 2021 · ⏱ 6 dk okuma</span>', '<span class="blog-date">May 2021 · ⏱ 6 min read</span>')
)
html = html.replace(
    '<span class="blog-date">Haziran 2021 · ⏱ 7 dk okuma</span>',
    i18n('<span class="blog-date">Haziran 2021 · ⏱ 7 dk okuma</span>', '<span class="blog-date">June 2021 · ⏱ 7 min read</span>')
)

# Blog modal titles
modal_titles = [
    ('Veri Madenciliğine Giriş', 'Introduction to Data Mining'),
    ('Veri Madenciliği: Süreç ve Metotlar', 'Data Mining: Process and Methods'),
    ('Blockchain (Blok Zinciri) Teknolojisi Nedir?', 'What Is Blockchain Technology?'),
    ('Türkiye Uzay Ajansını (TUA) Tanıyalım', 'Getting to Know the Turkish Space Agency (TUA)'),
    ('Neuralink: Beyin-Makine Arayüzü Nedir?', 'Neuralink: What Is a Brain-Machine Interface?'),
]
for tr_t, en_t in modal_titles:
    rep(
        f'<h2 class="blog-modal-title">{tr_t}</h2>',
        f'<h2 class="blog-modal-title">{tr_t}</h2>',
        f'<h2 class="blog-modal-title">{en_t}</h2>'
    )

# ── BLOG MODAL BODIES — English translations ──────────────────────────────────
# 1. Veri Madenciliğine Giriş
OLD_MODAL_1 = '''<div class="blog-modal-body"><h3>1. Giriş</h3>
<p>Merhaba! Bu yazımızda veri madenciliğine giriş yapacağız. Veri madenciliği ile ilgili bu ilk yazımızda veri madenciliğinin tanımından, etimolojisinden ve tarihsel gelişiminden bahsedeceğiz.</p>
<h3>2. Veri Madenciliği Nedir?</h3>
<p>Veri madenciliği; makine öğrenimi, istatistik ve veri tabanı sistemlerinin kesiştiği yöntemleri içeren büyük veri kümelerindeki örüntülerin keşfedilmesi sürecidir. Başka bir deyişle veri madenciliği, büyük veri yığınlarından gizli, önceden bilinmeyen ve potansiyel olarak kullanışlı bilgilerin çıkarılması işlemidir.</p>
<p>Veri Madenciliği; yığılmış, istenilen amaca yönelik faydalı bilgiler vermeyen verilerin anlamlı ve öz bilgiye dönüştürülmesi sürecidir. Veriden doğrudan bilgi elde edilebileceği gibi, elde edilen bu bilgiden de yeni bilgiler türetilebilir.</p>
<h3>3. Veri Madenciliğinin Etimolojisi</h3>
<p>"Veri madenciliği" terimi, 1983 yılında İktisadi Araştırmalar Dergisi'nde yayınlanan bir makalede iktisatçı Michael Lovell tarafından kullanılmıştır. Terimin bugünkü anlamda kullanımı 1990'ların başından itibaren yaygınlaşmıştır.</p>
<p>Akademik toplulukta büyük forumlar 1995 yılında Montreal'de AAAI sponsorluğu altında 1. Uluslararası Veri Madenciliği ve Bilgi Keşfi Çalıştayı ile başlamış, 1997'de KDD dergisi yayın hayatına girmiştir.</p>
<h3>4. Veri Madenciliğinin Tarihsel Gelişimi</h3>
<p>Bilgisayarlar ilk olarak 1950'li yıllarda sayım için kullanılmaya başlamıştır. 1960'larda veri tabanları geliştirildi. 1980'lerde ilişkisel veri tabanları ve SQL hayata geçirildi. 1990'larda veri ambarlaması ve veri madenciliği iş dünyası tarafından benimsendi. 2000'li yıllarda web madenciliği, metin madenciliği ve sosyal ağ analizi gibi yeni alt dallar ortaya çıktı.</p>
<h3>5. Sonuç</h3>
<p>Veri madenciliği, günümüz dijital çağında giderek artan önemiyle hem akademik hem de endüstriyel alanda vazgeçilmez bir disiplin haline gelmiştir. Bir sonraki yazımızda veri madenciliği sürecini, metotlarını ve uygulama alanlarını inceleyeceğiz.</p></div>'''

EN_MODAL_1 = '''<div class="blog-modal-body" data-tr><h3>1. Introduction</h3>
<p>Hello! In this post we introduce data mining. We cover the definition, etymology, and historical development of data mining.</p>
<h3>2. What Is Data Mining?</h3>
<p>Data mining is the process of discovering patterns in large datasets using methods at the intersection of machine learning, statistics, and database systems. In other words, it is the extraction of hidden, previously unknown, and potentially useful information from large volumes of data.</p>
<p>Data mining transforms accumulated raw data — that doesn't directly yield useful insights — into meaningful, concise knowledge. Knowledge can be derived directly from data, and further knowledge can be generated from that derived knowledge.</p>
<h3>3. Etymology of Data Mining</h3>
<p>The term "data mining" was used by economist Michael Lovell in a 1983 article published in the Review of Economics and Statistics. Its modern meaning became widespread from the early 1990s.</p>
<p>Major academic forums began in 1995 with the 1st International Workshop on Knowledge Discovery in Databases, held in Montreal under AAAI sponsorship. The KDD journal launched in 1997.</p>
<h3>4. Historical Development</h3>
<p>Computers were first used for census purposes in the 1950s. Databases were developed in the 1960s; relational databases and SQL appeared in the 1980s. In the 1990s, data warehousing and data mining were adopted by industry. The 2000s brought new sub-fields such as web mining, text mining, and social network analysis.</p>
<h3>5. Conclusion</h3>
<p>With its ever-growing importance in today's digital age, data mining has become an indispensable discipline in both academia and industry. In the next post we will examine the data mining process, its methods, and application areas.</p></div>'''

html = html.replace(OLD_MODAL_1, EN_MODAL_1, 1)

# 2. Veri Madenciliği Süreç ve Metotlar
OLD_MODAL_2 = '''<div class="blog-modal-body"><h3>1. Giriş</h3>
<p>Bu içeriğimizde daha önce kelime anlamına ve tarihine değindiğimiz veri madenciliğinin süreci, metotları, uygulama alanları ve karşılaşılan problemleri inceleyeceğiz.</p>
<h3>2. Veri Madenciliği Süreci</h3>
<p>Veri madenciliği birkaç aşamadan oluşan bir süreçtir. Endüstri standardı CRISP-DM (Cross-Industry Standard Process for Data Mining) modeli bu sürecin çerçevesini belirlemiştir.</p>
<p>Veri madenciliği sürecinde izlenen adımlar:</p>
<ul><li>Problemlerin tanımlanması</li><li>Verilerin hazırlanması</li><li>Modelin kurulması ve değerlendirilmesi</li><li>Modelin kullanılması</li><li>Modelin izlenmesi</li></ul>
<h3>3. Veri Madenciliği Metotları</h3>
<p>Veri madenciliği modelleri işlevlerine göre 3 grupta toplanır:</p>
<ul><li><strong>Sınıflama (Classification) ve Regresyon:</strong> Tahmin edici modeller grubuna girer. Hedef değişkenin süreksiz (ayrık) veya sürekli olmasına göre ikiye ayrılır.</li><li><strong>Kümeleme (Clustering):</strong> Tanımlayıcı modeller grubuna girer. Benzer özellikteki verileri gruplar.</li><li><strong>Birliktelik Kuralları (Association Rules):</strong> Veriler arasındaki ilişkileri ortaya çıkarır. Market sepeti analizi klasik bir örneğidir.</li></ul>
<h3>4. Uygulama Alanları</h3>
<p>Veri madenciliği; sağlık sektörü, telekomünikasyon, finans (bankacılık, borsa), pazarlama, sigortacılık, astronomi, biyoloji ve tıp gibi pek çok alanda kullanılmaktadır.</p>
<h3>5. Karşılaşılan Problemler</h3>
<p>Büyük veri ortamlarında artık veri, belirsizlik, boş veri, dinamik veri ve eksik veri gibi sorunlarla karşılaşılır. Bu sorunların doğru yönetimi, başarılı bir veri madenciliği çalışmasının temel koşullarından biridir.</p></div>'''

EN_MODAL_2 = '''<div class="blog-modal-body" data-tr><h3>1. Introduction</h3>
<p>In this post we examine the process, methods, application areas, and challenges of data mining — topics we briefly introduced in the previous article.</p>
<h3>2. The Data Mining Process</h3>
<p>Data mining is a multi-stage process. The industry-standard CRISP-DM (Cross-Industry Standard Process for Data Mining) model defines its framework.</p>
<p>Steps followed in the data mining process:</p>
<ul><li>Problem definition</li><li>Data preparation</li><li>Model building and evaluation</li><li>Model deployment</li><li>Model monitoring</li></ul>
<h3>3. Data Mining Methods</h3>
<p>Data mining models are grouped into 3 categories by function:</p>
<ul><li><strong>Classification and Regression:</strong> Belong to predictive models. Split into two depending on whether the target variable is discrete or continuous.</li><li><strong>Clustering:</strong> Belong to descriptive models. Groups data with similar characteristics.</li><li><strong>Association Rules:</strong> Reveal relationships between data. Market basket analysis is a classic example.</li></ul>
<h3>4. Application Areas</h3>
<p>Data mining is used in many fields including healthcare, telecommunications, finance (banking, stock markets), marketing, insurance, astronomy, biology, and medicine.</p>
<h3>5. Common Challenges</h3>
<p>In big data environments, challenges such as redundant data, ambiguity, missing values, dynamic data, and incomplete data are encountered. Proper management of these issues is one of the key requirements of a successful data mining project.</p></div>'''

html = html.replace(OLD_MODAL_2, EN_MODAL_2, 1)

# 3. Blockchain
OLD_MODAL_3 = '''<div class="blog-modal-body"><h3>1. Giriş</h3>
<p>Merhaba! Bu yazımızda son yıllarda finans dünyasında ve teknoloji gündeminde sıkça duyulan Blockchain (Blok Zinciri) teknolojisini ele alacağız.</p>
<h3>2. Blockchain Nedir?</h3>
<p>Blockchain, verilerin birbirine kriptografik olarak bağlı bloklar halinde saklandığı, merkezi bir otoriteye ihtiyaç duymayan dağıtık bir defter teknolojisidir. Her blok, bir önceki bloğun hash değerini içerdiğinden zincirin herhangi bir halkasını değiştirmek son derece güçtür.</p>
<p>Temel özellikleri şöyle sıralayabiliriz: merkezi olmayan yapı (decentralization), değişmezlik (immutability), şeffaflık (transparency) ve güvenlik (security).</p>
<h3>3. Nasıl Çalışır?</h3>
<p>Bir işlem gerçekleştiğinde ağdaki tüm katılımcılara duyurulur. Madenciler (miners) bu işlemi doğrulamak için rekabet eder. Doğrulanan işlem bir blok oluşturur ve zincire eklenir. Bu süreç "Proof of Work" veya "Proof of Stake" gibi konsensüs mekanizmaları ile güvence altına alınır.</p>
<h3>4. Kullanım Alanları</h3>
<p>Blockchain teknolojisi yalnızca kripto para birimleriyle sınırlı değildir. Akıllı sözleşmeler (Smart Contracts), tedarik zinciri yönetimi, sağlık kayıtları, dijital kimlik doğrulama, oylama sistemleri ve NFT'ler bu teknolojinin uygulama alanları arasında yer almaktadır.</p>
<h3>5. Bitcoin ve Ethereum</h3>
<p>Bitcoin, 2009 yılında Satoshi Nakamoto tarafından tanıtılan ilk blockchain uygulamasıdır. Ethereum ise 2015'te Vitalik Buterin tarafından geliştirilen ve akıllı sözleşmeleri destekleyen ikinci nesil bir blockchain platformudur.</p>
<h3>6. Sonuç</h3>
<p>Blockchain teknolojisi, güven sorununu merkezi bir aracıya ihtiyaç duymadan çözen devrimci bir yaklaşım sunmaktadır. Önümüzdeki yıllarda pek çok sektörde köklü dönüşümlere yol açması beklenmektedir.</p></div>'''

EN_MODAL_3 = '''<div class="blog-modal-body" data-tr><h3>1. Introduction</h3>
<p>In this post we explore Blockchain technology, which has been a frequent topic in the financial world and the tech agenda in recent years.</p>
<h3>2. What Is Blockchain?</h3>
<p>Blockchain is a distributed ledger technology in which data is stored in cryptographically linked blocks, with no need for a central authority. Because each block contains the hash of the previous block, altering any link in the chain is extremely difficult.</p>
<p>Its core properties are: decentralization, immutability, transparency, and security.</p>
<h3>3. How Does It Work?</h3>
<p>When a transaction occurs, it is broadcast to all participants in the network. Miners compete to validate the transaction. The validated transaction forms a block and is added to the chain. This process is secured by consensus mechanisms such as "Proof of Work" or "Proof of Stake".</p>
<h3>4. Use Cases</h3>
<p>Blockchain technology is not limited to cryptocurrencies. Smart Contracts, supply chain management, health records, digital identity verification, voting systems, and NFTs are among its application areas.</p>
<h3>5. Bitcoin and Ethereum</h3>
<p>Bitcoin, introduced by Satoshi Nakamoto in 2009, is the first blockchain application. Ethereum, developed by Vitalik Buterin in 2015, is a second-generation blockchain platform that supports smart contracts.</p>
<h3>6. Conclusion</h3>
<p>Blockchain technology offers a revolutionary approach to solving the trust problem without the need for a central intermediary. It is expected to drive fundamental transformations across many industries in the years ahead.</p></div>'''

html = html.replace(OLD_MODAL_3, EN_MODAL_3, 1)

# 4. TUA
OLD_MODAL_4 = '''<div class="blog-modal-body"><h3>1. Giriş</h3>
<p>Merhaba! Bu yazımızda Türkiye'nin uzay alanındaki en önemli kurumsal adımlarından biri olan Türkiye Uzay Ajansı'nı (TUA) tanıyacağız.</p>
<h3>2. TUA Nedir?</h3>
<p>Türkiye Uzay Ajansı (TUA), Türkiye'nin ulusal uzay politikalarını belirlemek, uzay alanındaki çalışmaları koordine etmek ve uluslararası iş birliklerini yürütmek amacıyla 2018 yılında kurulmuştur. Cumhurbaşkanlığına bağlı olarak faaliyet gösteren TUA, Türkiye'nin uzay vizyonunu hayata geçirmekle görevlidir.</p>
<h3>3. Türkiye'nin Uzay Hedefleri</h3>
<p>Türkiye'nin 2023 yılı için belirlediği uzay hedefleri arasında en önemlisi Ay'a kontrollü iniş yapmaktır. Bu hedef doğrultusunda yerli ve milli roket geliştirme çalışmaları sürdürülmektedir.</p>
<p>Diğer önemli hedefler şunlardır: yerli uydu teknolojilerinin geliştirilmesi, uzay üssü kurulması için yer seçimi çalışmaları ve uluslararası uzay iş birliklerinin güçlendirilmesi.</p>
<h3>4. TUA'nın Faaliyetleri</h3>
<p>TUA, üniversiteler ve savunma sanayii kuruluşlarıyla iş birliği yaparak uzay teknolojileri alanında Ar-Ge çalışmalarını desteklemektedir. Ayrıca genç yetenekleri uzay bilimine kazandırmak amacıyla çeşitli eğitim ve farkındalık programları düzenlemektedir.</p>
<h3>5. ROKETSAN ve Uzay</h3>
<p>Türkiye'nin roket teknolojisindeki en güçlü aktörü ROKETSAN, TUA ile koordineli olarak yerli roket motorları geliştirmektedir. Bu çalışmalar Türkiye'nin bağımsız uzay erişim kapasitesini güçlendirecektir.</p>
<h3>6. Sonuç</h3>
<p>TUA'nın kuruluşu, Türkiye'nin uzay alanındaki kararlılığının somut bir göstergesidir. Teknoloji bağımsızlığı hedefiyle yürütülen bu çalışmalar, gelecek nesillere ilham vermeye devam edecektir.</p></div>'''

EN_MODAL_4 = '''<div class="blog-modal-body" data-tr><h3>1. Introduction</h3>
<p>In this post we explore the Turkish Space Agency (TUA — Türkiye Uzay Ajansı), one of Turkey's most significant institutional steps in the field of space.</p>
<h3>2. What Is TUA?</h3>
<p>The Turkish Space Agency (TUA) was established in 2018 to define Turkey's national space policies, coordinate space-related activities, and manage international partnerships. Operating under the Presidency, TUA is tasked with realizing Turkey's space vision.</p>
<h3>3. Turkey's Space Goals</h3>
<p>The most important of Turkey's space targets set for 2023 is a controlled lunar landing. Towards this goal, domestic rocket development work continues.</p>
<p>Other key targets include: development of domestic satellite technologies, site selection studies for a space base, and strengthening international space cooperation.</p>
<h3>4. TUA's Activities</h3>
<p>TUA supports R&D activities in space technologies by collaborating with universities and defence industry organisations. It also organises various training and awareness programmes to attract young talent into space science.</p>
<h3>5. ROKETSAN and Space</h3>
<p>ROKETSAN, Turkey's most powerful player in rocket technology, is developing domestic rocket engines in coordination with TUA. This work will strengthen Turkey's independent space access capacity.</p>
<h3>6. Conclusion</h3>
<p>The establishment of TUA is a concrete demonstration of Turkey's determination in the space domain. This work, carried out with the goal of technological independence, will continue to inspire future generations.</p></div>'''

html = html.replace(OLD_MODAL_4, EN_MODAL_4, 1)

# 5. Neuralink
OLD_MODAL_5 = '''<div class="blog-modal-body"><h3>1. Giriş</h3>
<p>Bu yazımızda son yıllarda adından sıkça söz ettiren Elon Musk'ın kurucusu olduğu Neuralink şirketini ve beyin-makine arayüzü (Brain-Machine Interface / BMI) teknolojisini ele alacağız.</p>
<h3>2. Neuralink Nedir?</h3>
<p>Neuralink, 2016 yılında Elon Musk ve bir grup nörobilimci tarafından kurulan bir nörotek şirketidir. Şirketin temel amacı, insan beynine implante edilebilecek yüksek bant genişlikli beyin-bilgisayar arayüzleri geliştirmektir.</p>
<h3>3. Beyin-Makine Arayüzü (BMI) Nedir?</h3>
<p>Beyin-makine arayüzü (BMI), beyin sinyallerini okuyarak bunları bilgisayar komutlarına dönüştüren bir teknolojik sistemdir. İki temel türü vardır: invazif (beyne implante edilen) ve non-invazif (EEG başlığı gibi dışarıdan takılan) sistemler.</p>
<h3>4. Neuralink Nasıl Çalışır?</h3>
<p>Neuralink cihazı, beyne yerleştirilen ultra ince iplikçikler (threads) aracılığıyla nöronların elektriksel aktivitesini kaydeder. Bu iplikçikler insan saçının yaklaşık 1/4'ü kadar incedir. Toplanan veriler kablosuz olarak dış cihazlara aktarılır.</p>
<p>Şirket, 2020 yılında "Link" adını verdiği ilk cihazını tanıttı. Bir madeni para büyüklüğündeki bu cihaz, kafatası kemiğine yerleştirilerek beyin aktivitesini kaydedebilmektedir.</p>
<h3>5. Uygulama Alanları</h3>
<p>Kısa vadede Neuralink'in hedeflediği uygulamalar şunlardır: felçli hastaların bilgisayar ve akıllı telefon kontrolü, hafıza bozukluklarının tedavisi, görme engellilere yapay görme sağlanması ve nörolojik hastalıkların tedavisi.</p>
<p>Uzun vadede ise insan zekasının yapay zeka ile entegrasyonu (Musk'ın "AI ile simbiyoz" vizyonu) ve bellek yükleme/indirme gibi spekülatif hedefler de gündemdedir.</p>
<h3>6. Etik Tartışmalar</h3>
<p>Bu teknoloji beraberinde ciddi etik soruları da getirmektedir: Beyin verilerinin gizliliği nasıl korunacak? Zengin-yoksul arasındaki bilişsel uçurum derinleşecek mi? İnsan kimliğinin sınırları nerede başlar ve nerede biter?</p>
<h3>7. Sonuç</h3>
<p>Neuralink ve beyin-makine arayüzü teknolojisi, insanlık tarihinin en dönüştürücü icatlarından biri olma potansiyeli taşımaktadır. Tıbbi uygulamalardan başlayarak zamanla insan-bilgisayar etkileşimini kökten değiştirecek bu teknoloji, hem heyecan verici hem de dikkatli bir yaklaşım gerektiren bir alan olmaya devam etmektedir.</p></div>'''

EN_MODAL_5 = '''<div class="blog-modal-body" data-tr><h3>1. Introduction</h3>
<p>In this post we look at Neuralink, the company founded by Elon Musk, and brain-machine interface (BMI) technology — a topic that has gained significant attention in recent years.</p>
<h3>2. What Is Neuralink?</h3>
<p>Neuralink is a neurotech company founded in 2016 by Elon Musk and a group of neuroscientists. Its core goal is to develop high-bandwidth brain-computer interfaces that can be implanted in the human brain.</p>
<h3>3. What Is a Brain-Machine Interface (BMI)?</h3>
<p>A brain-machine interface (BMI) is a technological system that reads brain signals and converts them into computer commands. There are two main types: invasive (implanted in the brain) and non-invasive (worn externally, like an EEG headset).</p>
<h3>4. How Does Neuralink Work?</h3>
<p>The Neuralink device records the electrical activity of neurons through ultra-thin threads placed in the brain — approximately 1/4 the thickness of a human hair. The collected data is transmitted wirelessly to external devices.</p>
<p>In 2020 the company unveiled its first device, called "Link". About the size of a coin, it is placed in the skull bone and can record brain activity.</p>
<h3>5. Application Areas</h3>
<p>Short-term targets for Neuralink include: enabling paralysed patients to control computers and smartphones, treating memory disorders, providing artificial vision for the visually impaired, and treating neurological diseases.</p>
<p>Long-term speculative goals include integration of human intelligence with artificial intelligence (Musk's vision of "AI symbiosis") and memory upload/download.</p>
<h3>6. Ethical Debates</h3>
<p>This technology raises serious ethical questions: How will the privacy of brain data be protected? Will the cognitive gap between rich and poor deepen? Where do the boundaries of human identity begin and end?</p>
<h3>7. Conclusion</h3>
<p>Neuralink and brain-machine interface technology have the potential to be among the most transformative inventions in human history. Starting with medical applications and gradually reshaping human-computer interaction, this technology remains both exciting and a field that demands a careful approach.</p></div>'''

html = html.replace(OLD_MODAL_5, EN_MODAL_5, 1)

# ── CONTACT ──────────────────────────────────────────────────────────────────
rep(
    '<p class="contact-eyebrow reveal">Bana ulaş</p>',
    '<p class="contact-eyebrow reveal">Bana ulaş</p>',
    '<p class="contact-eyebrow reveal">Get in touch</p>'
)
rep(
    '<h2 class="contact-title reveal">Birlikte<br>çalışalım.</h2>',
    '<h2 class="contact-title reveal">Birlikte<br>çalışalım.</h2>',
    "<h2 class=\"contact-title reveal\">Let's<br>work together.</h2>"
)
rep(
    '<p class="contact-sub reveal">Yeni fırsatlara, projelere ve iş birliklerine açığım. Mesaj atmaktan çekinme.</p>',
    '<p class="contact-sub reveal">Yeni fırsatlara, projelere ve iş birliklerine açığım. Mesaj atmaktan çekinme.</p>',
    "<p class=\"contact-sub reveal\">I'm open to new opportunities, projects, and collaborations. Don't hesitate to reach out.</p>"
)

# ── FOOTER ───────────────────────────────────────────────────────────────────
# Footer stays same (name + URL)

# ── SCROLL TO TOP BUTTON ─────────────────────────────────────────────────────
rep(
    'aria-label="Yukarı çık"',
    'aria-label="Yukarı çık"',
    'aria-label="Back to top"'
)

# ── HAMBURGER aria-label ──────────────────────────────────────────────────────
rep(
    'aria-label="Menüyü aç"',
    'aria-label="Menüyü aç"',
    'aria-label="Open menu"'
)

# ─────────────────────────────────────────────────────────────────────────────
# 6.  Inject JavaScript i18n engine before </body>
# ─────────────────────────────────────────────────────────────────────────────
I18N_JS = """
<script>
// ── TR/EN Language Toggle ──────────────────────────────────────────────────
(function() {
  // Detect language from URL param or localStorage
  var params = new URLSearchParams(window.location.search);
  var stored = localStorage.getItem('lang');
  var lang = params.get('lang') || stored || 'tr';
  if (lang !== 'tr' && lang !== 'en') lang = 'tr';

  function applyLang(l) {
    document.documentElement.lang = l;
    // Update page title
    var titles = {
      tr: 'Hasan Saldıran — BT Sistemleri & Güvenlik Uzmanı',
      en: 'Hasan Saldiran — IT Systems & Security Specialist'
    };
    var titleEl = document.getElementById('page-title');
    if (titleEl) titleEl.textContent = titles[l];

    // Show/hide spans
    document.querySelectorAll('[data-tr]').forEach(function(el) {
      el.style.display = (l === 'tr') ? '' : 'none';
    });
    document.querySelectorAll('[data-en]').forEach(function(el) {
      el.style.display = (l === 'en') ? '' : 'none';
    });

    // Update button label
    var btn = document.getElementById('lang-toggle');
    if (btn) btn.textContent = (l === 'tr') ? 'EN' : 'TR';

    localStorage.setItem('lang', l);
  }

  window.toggleLang = function() {
    var current = localStorage.getItem('lang') || 'tr';
    var next = (current === 'tr') ? 'en' : 'tr';
    applyLang(next);
  };

  // Apply on load
  applyLang(lang);
})();
</script>
"""

html = html.replace("</body>", I18N_JS + "\n</body>", 1)

# ─────────────────────────────────────────────────────────────────────────────
# 7.  Write output
# ─────────────────────────────────────────────────────────────────────────────
with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Done! {OUTPUT} yazıldı.")
print(f"Toplam karakter: {len(html)}")
