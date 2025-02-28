def convertidor_hex(red,green,blue):
    list_rgb = [red,green,blue]
    valores = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    for i,color in enumerate(list_rgb):
        entero_color = color//16
        residuo_color = color%16
        list_rgb[i] = valores[entero_color] + valores[residuo_color]
    return list_rgb[0]+list_rgb[1]+list_rgb[2]

hex = convertidor_hex(red =201,green = 252, blue = 12)
print(hex)