count = 0
total = 0
attendance = [18,20,19,15,21]

for x in attendance:
    if(x>=20):
       print(f"{x} attendance is full")
       count = count+1 
    else:
      print(f"{x}  attendance is not full")
    total = total + x  
print(count)  
print(total)    
