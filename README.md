# Softmax Transport Planlama Programı:
Bu program, toplu taşıma hattı planlamasında mahallelerin uygunluğunu değerlendirmek için Softmax fonksiyonunu kullanan bir Python programıdır. Program, her mahalle için 5 farklı kriteri (nüfus yoğunluğu, mevcut ulaşım altyapısı, maliyet analizi, çevresel etki ve sosyal fayda) ve maliyet faktörünü de değerlendirerek en uygun mahalleyi belirler.
Bu program, toplu taşıma planlamasında mahallelerin uygunluk değerlendirmesini yaparak karar verme sürecini destekleyen bir araç sunar.
# Softmax Fonksiyonu:
Softmax fonksiyonu, bir dizi sayıyı üstel (exponential) fonksiyon yardımıyla normalize eden bir matematiksel işlemdir. Bu fonksiyon, her bir giriş değerinin üstel değerini hesaplar ve ardından tüm üstel değerlerin toplamına bölerek her girdinin olasılık skorunu üretir. Böylece, giriş değerleri arasındaki ilişkiler korunarak, her bir değerin toplam içindeki göreceli ağırlığı belirlenir. Softmax fonksiyonu, özellikle sınıflandırma ve karar destek sistemlerinde yaygın olarak kullanılır. Bu programda, mahallelerin kriter skorlarını normalize etmek ve karşılaştırılabilir hale getirmek için Softmax fonksiyonundan yararlanılmaktadır.
# Kullanım Adımları:
1. Projeyi bilgisayarınıza indirin veya GitHub'dan klonlayın.
2. Python yüklü olduğundan emin olun.
3. Terminal veya komut istemcisinde SoftmaxTransport.py komutunu çalıştırın.
4. Sonuç olarak her mahalle için kriter değerleri, hesaplana kriter ağırlıkları, maliyet-fayda oranları ve en uygun güzergah ekrana yazdırılır.
5. En yüksek skordan en düşük skora doğru mahalleler sıralanarak en uygun güzergah oluşturulur.
# Programın İşleyişi:
1. NumPy kütüphanesi içe aktarılır.
2. Mahalleler, kriterler ve maliyet bilgileri tanımlanır.
3. Mahalleler için kriter puanları bir NumPy dizisi olarak oluşturulur.
4. Softmax fonksiyonu tanımlanır ve kriter puanları normalize edilir.
5. Mahallelerin toplam skorları hesaplanır.
6. Mahallelerin maliyet-fayda oranları hesaplanarak en avantajlı mahalle belirlenir.
7. Sonuçlar ekrana yazdırılır ve en uygun güzergah seçilir.
# Kod Yapısı:
Veri Tanımlaması: Mahalleler, kriterler ve maliyet bilgileri tanımlanır.

Softmax Fonksiyonu: Kriter puanları normalize edilir.

Ağırlık Hesaplama: Mahalleler için Softmax sonucu hesaplanan kriter ağırlıkları belirlenir.

Toplam Skor Hesaplama: Her mahalle için toplam skor hesaplanır.

Maliyet-Fayda Oranı: Toplam skoru maliyet değerine bölerek fayda-maliyet oranı hesaplanır.

En Uygun Güzergah Seçimi: Yüksek skordan düşük skora doğru mahalleler sıralanarak en uygun güzergah belirlenir.
# Kullanılan Teknolojiler:
Programlama Dili: program Python programlama dili ile yazılmıştır.

Matematiksel Hesaplamalar: NumPy kütüphanesi ile Softmax hesaplamaları ve maliyet-fayda analizi gerçekleştirilmiştir.
# Ekran Çıktısı:
![image](https://github.com/user-attachments/assets/946bf2f2-e94d-4b93-b748-fa3672f5ddd7)

