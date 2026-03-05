a= int(input("Digite a letra A da formula: "))
b= int(input("Digite a letra B da formula: "))
c= int(input("Digite a letra C da formula: "))

delta = b*2-4*a*c
print ("O Valor de Delta é:",delta)

bhaskara_positivo= -b + delta / 2*a
bhaskara_negativo= -b - delta / 2*a
print("o valor da Bhaskara é x1: {} e o valor de x2: {} ".format(bhaskara_positivo,bhaskara_negativo))