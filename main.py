"""
Web Attack Risk Prediction & KVKK Cost-Benefit Analysis
========================================================
Bu proje, web uygulamalarına yönelik siber saldırıların tespiti için
makine öğrenmesi modelleri geliştirmekte ve modelin iş değerini
KVKK mevzuatı çerçevesinde kanıtlamaktadır.

Kullanım:
    python main.py           → Proje özeti ve veri kontrolü
    jupyter notebook         → Ana analiz notebook'u

Detaylı analiz için: notebooks/web_attack_analysis.ipynb
"""

import os
import sys


def check_data_sources():
    """Veri kaynaklarının varlığını kontrol eder."""
    data_path = "data/raw"
    required_files = {
        "csic_database.csv": "Kaynak 1: CSIC 2010 HTTP Dataset",
        "WEB_APPLICATION_PAYLOADS.jsonl": "Kaynak 2: Web Application Payloads",
        "turkey_cyber_incidents.csv": "Kaynak 4: Türkiye KVKK Veritabanı",
    }
    required_dirs = {
        "other": "Kaynak 3: Foospidy Payload Koleksiyonları"
    }

    print("=" * 60)
    print("VERİ KAYNAKLARI KONTROLÜ")
    print("=" * 60)

    all_ok = True
    for filename, desc in required_files.items():
        path = os.path.join(data_path, filename)
        status = "✅" if os.path.exists(path) else "❌"
        if not os.path.exists(path):
            all_ok = False
        print(f"  {status} {desc}")
        print(f"      → {path}")

    for dirname, desc in required_dirs.items():
        path = os.path.join(data_path, dirname)
        status = "✅" if os.path.isdir(path) else "❌"
        if not os.path.isdir(path):
            all_ok = False
        print(f"  {status} {desc}")
        print(f"      → {path}")

    return all_ok


def check_dependencies():
    """Gerekli kütüphanelerin kurulu olup olmadığını kontrol eder."""
    print("\n" + "=" * 60)
    print("BAĞIMLILIK KONTROLÜ")
    print("=" * 60)

    packages = {
        "pandas": "Veri işleme",
        "numpy": "Sayısal hesaplama",
        "matplotlib": "Görselleştirme",
        "seaborn": "İstatistiksel görselleştirme",
        "sklearn": "Makine öğrenmesi",
        "xgboost": "Gradient boosting",
        "shap": "Açıklanabilir yapay zeka",
        "lightgbm": "Gradient boosting (LightGBM)",
    }

    all_ok = True
    for pkg, desc in packages.items():
        try:
            __import__(pkg)
            print(f"  ✅ {pkg} — {desc}")
        except ImportError:
            print(f"  ❌ {pkg} — {desc} (KURULU DEĞİL)")
            all_ok = False

    if not all_ok:
        print("\n  Eksik paketleri kurmak için: pip install -r requirements.txt")

    return all_ok


def main():
    print("\n" + "=" * 60)
    print("🛡️  WEB ATTACK RISK PREDICTION")
    print("   KVKK Cost-Benefit Analysis")
    print("=" * 60)
    print()

    data_ok = check_data_sources()
    deps_ok = check_dependencies()

    print("\n" + "=" * 60)
    print("PROJE DURUMU")
    print("=" * 60)

    if data_ok and deps_ok:
        print("  ✅ Her şey hazır!")
        print("  → Analiz için: notebooks/web_attack_analysis.ipynb")
    else:
        print("  ⚠️  Eksikler var, yukarıdaki kontrolleri inceleyin.")

    print()


if __name__ == "__main__":
    main()