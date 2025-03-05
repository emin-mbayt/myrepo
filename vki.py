import tkinter as tk
from tkinter import messagebox

def hesapla_vki():
    try:
        boy = float(entry_boy.get()) / 100  # cm cinsinden metreye çevirme
        kilo = float(entry_kilo.get())
        vki = kilo / (boy ** 2)
        
        # VKİ'yi sınıflandırma
        if vki < 18.5:
            durum = "Zayıf"
        elif 18.5 <= vki < 25:
            durum = "Sağlıklı"
        elif 25 <= vki < 30:
            durum = "Kilolu"
        else:
            durum = "Aşırı kilolu (Obez)"
        
        sonuc_label.config(text=f"Vücut Kitle İndeksiniz: {vki:.2f} - {durum}", font=("Arial", 12, "bold"))
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")