# 🛡️ Web Attack Risk Prediction & KVKK Cost-Benefit Analysis

> Makine öğrenmesi ile web saldırı tespiti, SHAP ile açıklanabilir yapay zeka ve Türkiye KVKK mevzuatına dayalı maliyet/fayda simülasyonu.

---

## 📌 Proje Özeti

Bu projede, bir e-ticaret web uygulamasına gönderilen **61.065 HTTP request** analiz edilerek saldırı tespiti gerçekleştirilmiştir. Proje sadece teknik bir sınıflandırma problemi olarak değil, aynı zamanda **KVKK (6698 sayılı Kişisel Verilerin Korunması Kanunu)** mevzuatı kapsamında bir **işletme karar destek sistemi** olarak kurgulanmıştır.

### 🎯 Temel Hedefler
- **4 farklı veri kaynağının** anlamlı birleştirilmesi (Data Fusion)
- HTTP request'lerden **12 iş mantığına dayalı feature** türetilmesi
- Random Forest ve XGBoost ile **%94 doğrulukla** saldırı tespiti
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

## 🤖 Model Sonuçları

| Model | Accuracy | F1 Score | AUC-ROC |
|-------|----------|----------|---------|
| Random Forest | 0.9391 | 0.9279 | 0.9912 |
| **XGBoost** | **0.9406** | **0.9287** | **0.9915** |

---

## 💰 KVKK Bazlı Maliyet/Fayda Simülasyonu

### Maliyet Matrisi
| Senaryo | Birim Maliyet | Kaynak |
|---------|---------------|--------|
| False Positive (FP) | 150 TL | Normal kullanıcı bloklanması |
| False Negative (FN) | 5.000 TL | KVKK ceza riski + veri ihlali |
| True Positive (TP) | -500 TL | Saldırı engellendi (tasarruf) |

### Senaryo Karşılaştırması
| Senaryo | Toplam Maliyet |
|---------|---------------|
| Model Yok | 25.065.000 TL |
| ML Model (optimal threshold) | -2.330.650 TL |
| **Net Tasarruf** | **~27.4 Milyon TL** |

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