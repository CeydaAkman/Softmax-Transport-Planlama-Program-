import numpy as np

mahalleler = ["Karahıdır", "Bademlik", "İstasyon"]
kriterler = ["Nüfus Yoğunluğu", "Mevcut Ulaşım Altyapısı", "Maliyet Analizi", "Çevresel Etki", "Sosyal Fayda"]

veri = np.array([
    [7, 5, 6, 8, 7],
    [6, 8, 5, 7, 6],
    [5, 6, 7, 6, 8]
])

maliyetler = np.array([300, 250, 280])

def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum(axis=0, keepdims=True)

agirliklar = softmax(veri)

toplam_skorlar = agirliklar.sum(axis=1)

fayda_maliyet_orani = toplam_skorlar / maliyetler

siralama = np.argsort(fayda_maliyet_orani)[::-1]
siralama_mahalleler = [mahalleler[i] for i in siralama]

print("Mahallelerin Kriter Değerleri:")
for i, mahalle in enumerate(mahalleler):
    print(f"{mahalle}: {veri[i]}")

print("\nMahallelerin Softmax Sonucu Hesaplanan Kriter Ağırlıkları:")
for i, mahalle in enumerate(mahalleler):
    print(f"{mahalle}: {agirliklar[i]}")

print("\nMahallelerin Toplam Skorları:")
for i, mahalle in enumerate(mahalleler):
    print(f"{mahalle}: {toplam_skorlar[i]:.4f}")

print("\nMahallelerin Maliyet-Fayda Analizi Oranları:")
for i, mahalle in enumerate(mahalleler):
    print(f"{mahalle}: {fayda_maliyet_orani[i]:.6f}")

print("\nEn Uygun Güzergah:")
print(" ➝ ".join(siralama_mahalleler))