numere=int(input('Introduceti un numar : '))
nr=list(str(numere))
print('Afisarea listei:',nr) #determinati cifrele unui numar
suma=0
for element in range(0,len(nr)):
    suma=suma+int(nr[element])
print('Suma este ',suma)    