import os

dize = "/home/alp/Desktop/dataset/1.jpg"  # Örnek bir dize
dosya_yolu = os.path.abspath(dize)  # Dizeyi mutlak bir dosya yoluna dönüştürün

if os.path.exists(dosya_yolu):
    print("Doğru bir dosya yolu:", dosya_yolu)
else:
    print("Geçersiz bir dosya yolu:", dosya_yolu)
