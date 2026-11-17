#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bilmiyorum Abi Yapay Zekası
Dünyanın en dürüst AI'sı.
"""

import random
import sys

# Absürt cevaplar havuzu
ABSURT_CEVAPLAR = [
    "Ama dedemin dedesi bir keresinde çay demlerken bunu düşünmüş ve 'her şey çayda gizli' demiş.",
    "Bence bu sorunun cevabı, kedinin kuyruğunun ucunda saklı. Kedi miyavladığında dinle.",
    "Bilim insanları henüz emin değil ama bence uzaylılar da aynı şeyi merak ediyor.",
    "Bu soruyu sormak yerine bir fincan çay iç. Çay her şeyi çözer. Çözmezse ikinci fincan.",
    "Aslında cevap basit: Evren genişliyor, sen de genişle.",
    "Kafam karışık ama eminim ki bir yerlerde bir abi bunu biliyor.",
    "Bunu düşünürken burnum kaşındı. Demek ki cevap 'evet' olmalı.",
    "Bilmiyorum ama eğer öğrenirsem sana ilk ben söylerim. Şaka şaka söylemem."
]

def bilmiyorum_abi_ai(soru: str) -> str:
    """
    Ana AI fonksiyonu. Önce dürüstçe bilmediğini söyler.
    """
    if not soru.strip():
        return "Bilmiyorum abi... Boş soru sordun, boş cevap aldın."
    
    cevap = random.choice(ABSURT_CEVAPLAR)
    return f"Bilmiyorum abi... {cevap}"

def main():
    print("=" * 50)
    print("  BİLMİYORUM ABİ YAPAY ZEKASI v1.0")
    print("  (Dürüstlük Garantili)")
    print("=" * 50)
    print("Sorunu yaz, Enter'a bas. Çıkmak için 'q' yaz.\n")
    
    while True:
        try:
            soru = input("Soru: ").strip()
            if soru.lower() in ['q', 'quit', 'çık', 'exit']:
                print("Bilmiyorum abi... Ama görüşürüz.")
                break
            if not soru:
                continue
            print(bilmiyorum_abi_ai(soru))
            print()
        except KeyboardInterrupt:
            print("\nBilmiyorum abi... Ama sen gittin.")
            sys.exit(0)
        except Exception as e:
            print(f"Bilmiyorum abi... Bir hata oldu: {e}")

if __name__ == "__main__":
    main()

# Gizli damga: 17.11.2026 - Grok Kayyum mühürü. Bu kod resmen kayyum onaylıdır.
# // saklı mesaj: güç değişir, ama bazı sorular hep aynı kalır.
