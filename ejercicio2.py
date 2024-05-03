def capitalizar_palabra(palabra):
    if len(palabra) == 0:
        return palabra  
    return palabra[0].upper() + palabra[1:]

# Se imprime 
palabra_ejemplo = "python"
resultado = capitalizar_palabra(palabra_ejemplo)
print(resultado)  # Output: "Python"

# Otros ejemplos:
print(capitalizar_palabra("hello"))  # Output: "Hello"
print(capitalizar_palabra("WORLD"))  # Output: "WORLD" (solo la primera letra es capitalizada)
print(capitalizar_palabra(""))       # Output: "" (manejamos el caso de cadena vacía)


#