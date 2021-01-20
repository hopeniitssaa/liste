a=[1,2,3,4,5,-1,-2,-3,-4,-5]
print('Lista 1=',a)
b=sorted(a)
print('Lista in ordine crescatoare=',b)
a.sort(reverse=True)
print('Lista in ordine crescatoare=',a)
print('Lungimea listei=',len(a))
print('MAX=',max(a))
print('MIN=',min(a))
a=[1,2,3,4,5,-1,-2,-3,-4,-5]
print('Lista 4 noua=',a+[111])
a.insert(2,222)
print('Lista 5 noua=',a)
