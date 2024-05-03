def capitalizar_palabra(palabra):
    if len(palabra) == 0:
        return palabra  
    return palabra[0].upper() + palabra[1:]

# Se imprime la palabra python con mayuscula si esta en minuscula 
palabra = "python"
resultado = capitalizar_palabra(palabra)
print(resultado)  


 

