def eliminar_duplicados(lista):
    # Utilizamos dict.fromkeys() para eliminar duplicados y preservar el orden original
    return list(dict.fromkeys(lista))

# Lista original
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

# Lista sin duplicados
lista_procesada = eliminar_duplicados(lista_original)

print("Lista procesada:", lista_procesada)
