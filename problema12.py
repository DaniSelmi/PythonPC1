#.gif -- image/gif
#.jpg -- image/jpg
#.jpeg -- image/jpeg
#.png -- image/png
#.pdf -- application/pdf
#.txt -- text/plain
#.zip -- application/zip

diccionario = {"gif":"image/gif",
               "jpg":"image/jpg",
               "jpeg":"image/jpeg",
               "png":"image/png",
               "pdf":"application/pdf",
               "txt":"text/plain",
               "zip":"application/zip"
               }

print(diccionario)

respuesta = input("Nombre del archivo: ")
respuesta = respuesta.lower().strip()

nombre, sufijo = respuesta.split('.')

if sufijo.lower() in diccionario.keys:
    x = diccionario.get(sufijo)
    print(x)
else:
    print("application/octet-steam")


