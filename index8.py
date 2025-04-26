Peso = float (input ("introduce tu peso"))
Altura = float (input ("introduce tu altura"))
altura2 = Altura*2 
imc = Peso/altura2

if imc <= 18.5 :
    print ("tienes bajo peso")
elif imc >= 18.6 and imc <= 24.9 :
    print ("tienes peso normal")
if imc >= 25 and imc <= 29.9 :
    print ("tienes sobrepeso")
elif imc >= 30 :
    print ("tienes obesidad") 