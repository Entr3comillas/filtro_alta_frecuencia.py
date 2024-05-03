import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen que se desea aclarar
imagen = cv2.imread('ruta/a/tu/imagen.jpg')

# Convertir la imagen a escala de grises (opcional, pero puede ser útil para mejorar imágenes en blanco y negro)
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Crear un filtro de alta frecuencia (kernel) para resaltar bordes
# El filtro siguiente es un kernel Laplaciano, que resalta bordes
filtro_laplaciano = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
])

# Aplicar el filtro a la imagen para resaltar bordes
imagen_bordes = cv2.filter2D(imagen_gris, -1, filtro_laplaciano)

# Para crear un efecto de realce, podemos sumar la imagen original y la imagen de bordes
imagen_realzada = cv2.add(imagen_gris, imagen_bordes)

# Mostrar las imágenes antes y después de la mejora
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(imagen_gris, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Aclarada")
plt.imshow(imagen_realzada, cmap='gray')
plt.axis('off')

plt.show()
