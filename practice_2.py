strr=input("enter any stringg")
count=0
dictt={}
for i in strr:
    if i not in dictt:
        count=1
    else:
        count+=1
    print(i,count)