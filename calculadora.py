seleccion =int (input("digite la opercacion que quiere hacer  1 suma // 2 resta // 3 multiplicacion // 4 divicion "))

if seleccion == 1:
    print("suma")
    num1=float (input("digite el primer numero"))
    num2=float (input("digite el segundo numero"))
    resul= num1 + num2 
    print ("la suma es:",resul)
    
elif seleccion == 2:
    print("resta")
    num1=float (input("digite el primer numero"))
    num2=float (input("digite el segundo numero"))
    resul= num1 - num2 
    print ("la resta es:" ,resul)
elif seleccion == 3:
    print("multiplicacion")
    num1=float (input("digite el primer numero"))
    num2=float (input("digite el segundo numero"))
    resul= num1 * num2 
    print ("la multiplicacion es:",resul)
    
elif seleccion == 4:
    print("divicion")
    num1=float (input("digite el primer numero"))
    num2=float (input("digite el segundo numero"))
    resul= num1 / num2 
    print ("la divicion es:",resul)