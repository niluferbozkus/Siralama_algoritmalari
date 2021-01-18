eleman_sayisi = int(input("Kaç tane sayı girmek istiyorsunuz? : " ))  

sayilar = []

for a in range(eleman_sayisi):  
    sayilar.append(int(input(f"Girmek istediğiniz {a+1}. sayı: "))) 
print("\nSıralamak istediğiniz sayılar: ",sayilar)


for i in range(1,eleman_sayisi):
    karsilastirma_degeri = sayilar[i]
    index = i
    
    while index > 0 and sayilar[index-1] > karsilastirma_degeri :
        sayilar[index] = sayilar[index-1]
        index -= 1
    sayilar[index] = karsilastirma_degeri
print("\nGirdiğiniz sayıların sıralanmış hali: ",sayilar)

"""
    for döngüsünde i benim kontrol ettiğim sayının indexi. i değeri her for 
döngüsüne girildiğinde 1 artıyor. Çünkü bir sonraki kontrol edeceğim sayı öncekinin 
sağındaki sayı.

    while döngüsünde kontrol ettiğim sayıyı solundakilerle karşılaştırıyorum.
index her seferinde bir azalıyor çünkü her seferinde bir soldakine bakıyorum.
sağdaki sayıyı soldaki sayıdan küçük bulana kadar devam ediyorum ve küçük bulduğum 
an döngüden çıkıpkarşılaştırdığım değeri bulduğum indexe atıyorum.
 
 Çalışma şekli:
a=[1, 3, 2, 4]
a[2]=a[1]
a[1]=2
print(a)
>>[1,2,3,4]
"""
