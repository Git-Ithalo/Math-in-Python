def delta(a,b,c):
    conta = b*2-4*a*c
    return conta


a= int(input("Digite a letra A da formula: "))
b= int(input("Digite a letra B da formula: "))
c= int(input("Digite a letra C da formula: "))

valor = delta(a,b,c)
print (valor)

def bhaskara(a, b, delta ):
    bhaskara_p = -b+delta/2*a
    bhaskara_n = -b-delta/2*a
    return bhaskara_p, bhaskara_n


bh3=bhaskara(a, b, valor )
print(bh3)
