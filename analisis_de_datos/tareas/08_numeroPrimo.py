num = int(input("Introduce un número: "))


if num < 2:
    print(f"El número {num} no es primo.")
else:
    raiz = int(num ** 0.5) + 1  
    es_primo = True  

    for i in range(2, raiz):
        if num % i == 0:  
            es_primo = False  
            break  


    if es_primo:
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")


