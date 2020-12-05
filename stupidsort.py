enum = int(input("Kaç tane sayı girmek istiyorsunuz? : "))
arr = []  
  
for i in range(0,enum):  
    a=int(input(f"Girmek istediğiniz {i+1}. sayı: "))
    arr.append(a)
#print("Sıralamak istediğiniz sayılar: ",arr)
i=0
while i>=0 and i<enum-1:
    if arr[i]>arr[i+1]:
        temp = arr[i]
        arr[i] = arr[i+1]  
        arr[i+1] = temp
        i=0     
       
    else: # arr[i]<=arr[i+1]:
        i += 1           
  
    print(arr)

