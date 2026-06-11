# 🛡️ Web Attack Risk Prediction & KVKK Cost-Benefit Analysis

> Makine öğrenmesi ile web saldırı tespiti, SHAP ile açıklanabilir yapay zeka ve Türkiye KVKK mevzuatına dayalı maliyet/fayda simülasyonu.

---

## 📌 Proje Özeti

Bu projede, bir e-ticaret web uygulamasına gönderilen **61.065 HTTP request** analiz edilerek saldırı tespiti gerçekleştirilmiştir. Proje sadece teknik bir sınıflandırma problemi olarak değil, aynı zamanda **KVKK (6698 sayılı Kişisel Verilerin Korunması Kanunu)** mevzuatı kapsamında bir **işletme karar destek sistemi** olarak kurgulanmıştır.

### 🎯 Temel Hedefler
- **4 farklı veri kaynağının** anlamlı birleştirilmesi (Data Fusion)
- HTTP request'lerden **12 iş mantığına dayalı feature** türetilmesi
- - Random Forest, XGBoost ve LightGBM ile **%94 doğrulukla** saldırı tespiti
- **KVKK ceza verileriyle** maliyet/fayda simülasyonu ve optimal threshold belirleme
- **SHAP** ile model kararlarının açıklanabilir hale getirilmesi
- ---

## 📊 Veri Kaynakları (4 Farklı Kaynak)

| # | Kaynak | Tür | Boyut | Açıklama |
|---|--------|-----|-------|----------|
| 1 | CSIC 2010 HTTP Dataset | Kaggle CSV | 61.065 satır | Normal ve anomalous HTTP request'leri |
| 2 | Web Application Payloads | Kaggle JSONL | 455 payload | SQLi, XSS, SSRF, RCE saldırı imzaları |
| 3 | Foospidy Payloads | GitHub | 28.569 payload | Gerçek dünya saldırı pattern koleksiyonu |
| 4 | Türkiye Siber Olay ve KVKK Veritabanı | Sentetik | 250 olay | KVKK cezaları, müşteri kaybı, maliyet verileri |

---

## 🧪 Feature Engineering (12 Feature)

| Feature | İş Mantığı |
|---------|------------|
| request_length | Uzun request'ler injection payload barındırabilir |
| special_char_count | Özel karakterler saldırı syntax'ının temelidir |
| digit_count | Sayısal değerler SQL injection belirtisi |
| uppercase_ratio | Obfuscation ve encoding manipülasyonu göstergesi |
| entropy_score | Yüksek entropi → obfuscated payload |
| encoded_char_ratio | URL encoding oranı → WAF bypass girişimi |
| parameter_count | Fazla parametre → parameter tampering |
| url_depth | Derin path → traversal saldırısı |
| url_length | URL uzunluğu anomali göstergesi |
| content_length | POST body uzunluğu |
| is_post | POST method saldırı taşıyabilir |
| is_put | PUT method dosya yükleme saldırısı |
---

## 🤖 Model Sonuçları (GridSearchCV Optimize)

| Model | Accuracy | F1 Score | AUC-ROC |
|-------|----------|----------|---------|
| Random Forest | 0.9390 | 0.9275 | 0.9913 |
| **XGBoost** | **0.9433** | **0.9321** | **0.9919** |
| LightGBM | 0.9390 | 0.9270 | 0.9913 |

---

## 💰 KVKK Bazlı Maliyet/Fayda Simülasyonu

### Maliyet Matrisi (KVKK Veritabanından Türetilmiş)
| Senaryo | Birim Maliyet | Türetim Yöntemi |
|---------|---------------|-----------------|
| False Positive (FP) | 150 TL | Normal kullanıcı bloklanması |
| False Negative (FN) | 43.677 TL | Ort. olay maliyeti (8.7M TL) x ihlale dönüşme olasılığı (%0.5) |
| True Positive (TP) | 0 TL | Mükerrer hesaplama önlendi |

### Yıllık Projeksiyon (ALE - Olay Bazlı, NIST SP 800-30)
| Senaryo | Yıllık Olay | Model Yok | ML Model | Tasarruf |
|---------|-------------|-----------|----------|---------|
| Küçük İşletme | 2 | 17.4M TL | 22.9K TL | 17.4M TL |
| Orta E-Ticaret | 5 | 43.6M TL | 57.2K TL | 43.6M TL |
| Büyük Fintech | 12 | 104.8M TL | 137.4K TL | 104.6M TL |

> ALE metodolojisi: NIST SP 800-30 Risk Assessment Framework

> KVKK 2025 ceza tavanı: 13.620.402 TL (Kaynak: KVKK Madde 18)
> ---

## 🔍 Explainable AI (SHAP)

SHAP analizi ile model kararları açıklanabilir hale getirilmiştir.

**Temel Bulgular:**
- encoded_char_ratio ve request_length en etkili feature'lar
- Yüksek entropy → saldırı olasılığı artıyor
- SHAP sonuçları siber güvenlik domain bilgisiyle tutarlı

---

## 📁 Proje Yapısı

    web_attack_risk_prediction/
    ├── data/raw/                    # 4 farklı veri kaynağı
    ├── notebooks/                   # Ana analiz notebook'u
    ├── outputs/figures/             # Üretilen grafikler
    ├── src/                         # Modüler Python kodları
    ├── requirements.txt
    └── README.md

---

## 🚀 Kurulum ve Çalıştırma

```bash
git clone https://github.com/MuhammedAsef/web_attack_risk_prediction.git
cd web_attack_risk_prediction
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/web_attack_analysis.ipynb
```

---

## 📚 Referanslar

- CSIC 2010 Dataset — Spanish National Research Council (CSIC)
- KVKK Ceza Tutarları — Kişisel Verileri Koruma Kurumu, 2025
- SHAP — Lundberg & Lee (2017), NeurIPS
- Foospidy Payloads — OWASP topluluk kaynaklı saldırı payload'ları

---

## 📄 Lisans

Bu proje MIT lisansı altında sunulmaktadır.