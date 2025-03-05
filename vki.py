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

# Ana pencere
root = tk.Tk()
root.title("VKİ Hesaplayıcı")
root.geometry("325x300")  # Sabit pencere boyutu
root.resizable(False, False)  # Pencereyi yeniden boyutlandırmayı engelliyoruz

# Ana pencere için margin ekliyoruz
root.grid_rowconfigure(0, weight=1, minsize=20)  # Üst margin
root.grid_rowconfigure(1, weight=1, minsize=20)  # Aradaki margin
root.grid_rowconfigure(2, weight=1, minsize=20)  # Butonun altı margin
root.grid_rowconfigure(3, weight=1, minsize=20)  # Sonuç margin

# Boy etiketi ve giriş kutusu
tk.Label(root, text="Boy (cm):").grid(row=0, column=0, padx=20, pady=5, sticky="w")
entry_boy = tk.Entry(root, width=20, font=("Arial", 12))
entry_boy.grid(row=0, column=1, padx=20, pady=5)

# Kilo etiketi ve giriş kutusu
tk.Label(root, text="Kilo (kg):").grid(row=1, column=0, padx=20, pady=5, sticky="w")
entry_kilo = tk.Entry(root, width=20, font=("Arial", 12))
entry_kilo.grid(row=1, column=1, padx=20, pady=5)

# Hesapla butonunu pencerenin solundan sağına kadar yapıyoruz
btn_hesapla = tk.Button(root, text="Hesapla", command=hesapla_vki, height=2, font=("Arial", 14))
btn_hesapla.grid(row=2, columnspan=2, pady=20, sticky="ew", padx=20)

# Sonuç etiketini oluştur
sonuc_label = tk.Label(root, text="", fg="blue", font=("Arial", 12, "bold"))
sonuc_label.grid(row=3, columnspan=2, pady=10)

# Sonuç mesajını ortalamak
sonuc_label.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

root.mainloop()
