with open('input.txt','r') as f:
    l=list(eval(f.readline()))

print("lista initiala este ",l)
x=sorted(l)
print("lista in ordine crescatoare: ", x)
x.sort(reverse=True)
print("lista in ordine descrescatoare: ",x)
print("nr de elemente din lista: ",len(l))
print("elementul maxim: ",max(l))
print("elementul minim:",min(l))
print("elementul 111 la coadă : ",l+[111])
l[2]=222
print("elemtul 222 pe poziția a doua : ",l)
