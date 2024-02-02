def PulgadasCentimetros(pulgadas):
    return 2.54 * pulgadas

pulgadasUser = PulgadasCentimetros(float(input("Introduce tus pulgadas a converir: ")))
print(f"Estas son las pulgadas: {pulgadasUser}")