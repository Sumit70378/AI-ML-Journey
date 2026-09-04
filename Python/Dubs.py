list = [4,4,5,7,2,1,2,9]

for i in range(0,len(list)):
    for j in range(i+1,len(list)-1):
        if(list[i]==list[j]):
            list.remove(list[j])

print(list)           
    