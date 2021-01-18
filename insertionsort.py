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
