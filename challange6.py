#challange2

a=input("入力１")
b=input("入力２")

r="私は昨日{}を書いて、{}に送った！".format(a,b)
print(r)

#challange3
x="aldous Huxley was born in 1894".capitalize()
print(x)

#challange4
z="何処で？","誰が？","いつ？".split("?")
print(z)

#challange5
words=["The","fox","jumped","over","the","fence","."]
words=" ".join(words)
words=words[0:-2]+"."
print(words)

#challange6
v="A screaming comes across the sky."
v=v.replace("s","$")
print(v)

#challange7
w="Hemingway"
w=w.index("m")
print(w)

#challange8
r="吾輩は\"猫\"である"
print(r)

#challange9
moji="three"+"three"+"three"
moji_="three"*3

print(moji)
print(moji_)

#challange10
sent="四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
sli=sent[:10]
print(sli)

