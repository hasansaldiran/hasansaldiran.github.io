# hasansaldiran.github.io

Kişisel portföy sitesi: **Hasan Saldıran**, Bilgisayar Mühendisi (IT Solutions Engineer · Otomasyon & Yapay Zekâ).

**Canlı site:** [hasansaldiran.github.io](https://hasansaldiran.github.io)

## İçerik

- Hakkımda, deneyim, projeler, yetenekler, blog ve iletişim bölümleri
- Proje filtreleri: Otomasyon, Yapay Zekâ & Veri, Python, C#, HTML, Güvenlik
- Türkçe / İngilizce dil geçişi (seçim tarayıcıda hatırlanır)
- Koyu temalı, mobil uyumlu terminal tarzı arayüz
- SEO: meta etiketleri, Open Graph / Twitter kartı, JSON-LD (`Person`), `canonical`, `sitemap.xml`, `robots.txt`

## Teknoloji

- Saf HTML, CSS ve JavaScript (derleme adımı yok); tüm site tek dosyada: `index.html`
- Google Fonts: JetBrains Mono ve Outfit
- Google Analytics (gtag)
- GitHub Pages ile yayın

## Yerelde çalıştırma

```bash
python -m http.server 8000
# http://localhost:8000
```

## İçerik nasıl güncellenir

- **Türkçe metin** doğrudan `index.html` içindedir; sayfanın varsayılan dili Türkçedir.
- **İngilizce metin**, dosyanın sonundaki `TRANSLATIONS` tablosundadır. Her satır `[CSS seçici, Türkçe metin, İngilizce metin]` biçimindedir. Dil değişince Türkçe içerik sayfadan okunur, tablodaki ikinci değer yalnızca referanstır.
- Seçicilerde `:nth-child(n)` kullanıldığı için kart, yetenek grubu veya deneyim sırası değişirse ilgili satırların numaraları da güncellenmelidir.
- **Yeni proje:** `.projects-grid` içine bir `project-card` ekleyin. `data-lang` dil filtresini, `data-tags` (`security`, `ai`, `automation`) konu filtresini belirler. Projenin İngilizce satırlarını tabloya eklemeyi unutmayın.
- Yayından önce `sitemap.xml` içindeki `lastmod` tarihini güncelleyin.

## Dosyalar

| Dosya | Açıklama |
|---|---|
| `index.html` | Sitenin tamamı (HTML, CSS, JS, TR/EN çeviri tablosu) |
| `sitemap.xml`, `robots.txt` | Arama motorları için |
| `google5521f65cc8585d07.html` | Google Search Console doğrulama dosyası (silmeyin) |

## İletişim

- LinkedIn: [linkedin.com/in/hasansaldiran](https://www.linkedin.com/in/hasansaldiran/)
- GitHub: [github.com/hasansaldiran](https://github.com/hasansaldiran)
- E-posta: hasansaldirann@gmail.com
