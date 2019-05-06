#challange1
with open("self_taught.csv","r",encoding="utf-8")as f:
    print(f.read())

#challange2
qs=input("how old are you?")
with open("members_age.csv","w",encoding="utf-8")as f:
    f.write(qs)

#challange3
import csv

#tom=["Top Gun","Risly Business","Minority Report"]
#leo=["Titanic","The Revenant","Inception"]
#densel=["Training Day","Man on Fire","Flight"]
#stars=[]
#stars.append(tom)
#stars.append(leo)
#stars.append(densel)
#with open("action.csv","w",encoding="utf-8")as g:
#    movie=csv.writer(g,delimiter=",")
#    movie.writerow(stars)
    
#challange4
tom=["トップガン","バニラスカイ","マイノリティリポート"]
leo=["タイタニック","レヴェナント","インセプション"]
densel=["トレーニングデイ","マンオンファイア","フライト"]
stars=[]
stars.append(tom)
stars.append(leo)
stars.append(densel)
with open("action.csv","w",encoding="utf-8")as g:
    movie=csv.writer(g,delimiter=",")
    movie.writerow(stars)
