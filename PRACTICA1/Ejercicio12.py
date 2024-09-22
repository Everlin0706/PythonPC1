def obtener_tipo_mime(nombre_archivo):
    # Diccionario de extensiones con sus tipos MIME correspondientes
    tipos_mime = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Convertimos el nombre de archivo a minúsculas para evitar problemas con mayúsculas/minúsculas
    nombre_archivo = nombre_archivo.lower()

    # Verificamos si el archivo tiene una extensión conocida
    for extension in tipos_mime:
        if nombre_archivo.endswith(extension):
            return tipos_mime[extension]
    
    # Si no se encuentra la extensión, se devuelve el tipo por defecto
    return "application/octet-stream"

# Solicitar el nombre de archivo al usuario
nombre_archivo = input("Introduce el nombre del archivo: ")

# Obtener y mostrar el tipo MIME correspondiente
tipo_mime = obtener_tipo_mime(nombre_archivo)
print("El tipo MIME es:", tipo_mime)
