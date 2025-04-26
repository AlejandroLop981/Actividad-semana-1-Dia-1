Cuenta = int (input ("Cuanto es el total de la cuenta?:"))

propina = int (input ("que porcentaje de propina desea dejar:  "))
if propina == 20 :
    print ("su propina es de", Cuenta/100 * 20)
elif propina == 15 :
    print ("su propina es de", Cuenta/100 * 15)
if propina == 10 :
    print ("su propina es de", Cuenta/100 * 10)