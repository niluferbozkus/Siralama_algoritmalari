enum = int(input("Kaç tane sayı girmek istiyorsunuz? : " ))  

arr = []
new_arr=[]

for a in range(0,enum):  
    arr.append(int(input(f"Girmek istediğiniz {a+1}. sayı: "))) 
print("Sıralamak istediğiniz sayılar: ",arr)


for i in range(1,enum):

    comp = arr[i]
    loc = i
    
    while loc>0 and arr[loc-1]> comp:
        arr[loc]=arr[loc-1]
        loc -= 1
    arr[loc] = comp
print("Girdiğiniz sayıların sıralanmış hali: ",arr)
