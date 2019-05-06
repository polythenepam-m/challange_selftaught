#challange1
movie=["ウォーキングデッド","アントラージュ","ザ・ソプラノイズ","ヴァンパイア・ダイアリーズ"]
#for show in movie:
#    print(show)
    
#challange2
#for i in range(25,51):
#    print(i)
    
#challange3
#i=0
#for show in movie:
#    new=movie[i]
#    i+=1
#    print(show,i)

#challange4
number=[5,9]
while True:
    
    a=input("Type a number")
    if a=="q":
        break
    try:
        a=int(a)
    except ValueError:
        print("Please type a number or Q to exit")
    if a in number:
        print("right")
    else:
        print("false")

#challange5
list1=[8,19,148,4]
list2=[9,1,33,83]
multiply=[]
for i in list1:
    for j in list2:
        multiply.append(i*j)
print(multiply)



    
    
    
    
