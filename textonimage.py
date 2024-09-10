from PIL import Image, ImageDraw, ImageFont
import markdown
import gc

# Abre la imagen
imagen = Image.open('C:\\Users\\luisd\\Downloads\\grid-3227320_12801.jpg')

# Crea un objeto para dibujar en la imagen
draw = ImageDraw.Draw(imagen)

# Define el texto y la fuente
# Define los colores para las diferentes partes del código
color_palabras_clave = (0, 0, 255)  # Azul
color_funcion = (255, 0, 0)  # Rojo
color_cadena = (0, 128, 0)  # Verde
color_normal = (0, 0, 0)  # Negro para texto normal

# Define el código en C y su sintaxis coloreada
texto = [
    (color_palabras_clave, "int "),  # palabra clave
    (color_funcion, "main"),  # función
    (color_normal, "(){\n    "),
    (color_palabras_clave, "printf"),  # función
    (color_normal, "("),
    (color_cadena, '"Hello, World!"'),  # cadena
    (color_normal, ");\n    "),
    (color_palabras_clave, "return "),  # palabra clave
    (color_normal, "0;\n}\n")
]

fuente = ImageFont.truetype("C:\\Windows\\Fonts\\cour.ttf", 30)  # Fuente "Courier" con tamaño 30

# Define la posición del texto
#posicion = (100, 200)
# Posición inicial del texto
posicion_x, posicion_y = 100, 200

# Define el color del texto
#color = (0, 0, 0)  # negro

# Agrega el texto a la imagen
# Dibuja el texto parte por parte
for color, parte_texto in texto:
    # Dibuja el texto
    draw.text((posicion_x, posicion_y), parte_texto, font=fuente, fill=color)
    
    # Obtén el tamaño del texto
    bbox = draw.textbbox((posicion_x, posicion_y), parte_texto, font=fuente)
    text_width = bbox[2] - bbox[0]  # Ancho del texto
    text_height = bbox[3] - bbox[1]  # Alto del texto

    # Ajusta la posición horizontal para cada parte del texto
    posicion_x += text_width
    
    # Si hay un salto de línea en el código, ajusta la posición vertical y resetea la horizontal
    if "\n" in parte_texto:
        posicion_y += text_height
        posicion_x = 150  # Vuelve al margen izquierdo

# Guarda la imagen modificada
imagen.save('imagen_modificada_coloreada.jpg')

# Limpia objetos innecesarios
del draw  # Elimina el objeto de dibujo
del fuente  # Elimina la referencia a la fuente

# Cierra la imagen explícitamente
imagen.close()

# Forzar la recolección de basura
gc.collect()

print("Memoria limpiada y proceso completado.")