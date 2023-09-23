import cv2
import numpy as np
from gtts import gTTS
from playsound import playsound

def detect_bill_color(img):
    # Convertir de BGR a HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Definir límites inferiores y superiores para los colores de los billetes
    green_lower = np.array([40, 0, 0])
    green_upper = np.array([80, 255, 255])
    blue_lower = np.array([90, 0, 0])
    blue_upper = np.array([140, 255, 255])
    red_lower = np.array([10, 0, 0])
    red_upper = np.array([30, 255, 255])
    pink_lower= np.array([130, 0, 0])
    pink_upper= np.array([180, 255, 255])
    # Crear máscaras para cada color de billete
    green_mask = cv2.inRange(hsv, green_lower, green_upper)
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    pink_mask = cv2.inRange(hsv, pink_lower, pink_upper)

    # Verificar si se ha detectado algún píxel con el color especificado
    if np.count_nonzero(green_mask) > np.count_nonzero(blue_mask) and np.count_nonzero(green_mask) > np.count_nonzero(red_mask) and np.count_nonzero(green_mask) > np.count_nonzero(pink_mask):
        text="El billete es de 10 soles."        
    elif np.count_nonzero(blue_mask) > np.count_nonzero(green_mask) and np.count_nonzero(blue_mask) > np.count_nonzero(red_mask) and np.count_nonzero(blue_mask) > np.count_nonzero(pink_mask):
        text= "El billete es de 100 soles."
    elif np.count_nonzero(red_mask) > np.count_nonzero(green_mask) and np.count_nonzero(red_mask) > np.count_nonzero(blue_mask) and np.count_nonzero(red_mask) > np.count_nonzero(pink_mask):
        text="El billete es de 20 soles."
    elif np.count_nonzero(pink_mask) > np.count_nonzero(red_mask) and np.count_nonzero(pink_mask) > np.count_nonzero(blue_mask) and np.count_nonzero(pink_mask) > np.count_nonzero(green_mask):
        text="El billete es de 50 soles"
    else:
        text="No se ha detectado un billete en la imagen."
    return text
# Carga la imagen
img = cv2.imread('billete10.jpg')
#El texto que desea convertir en audio
texto=detect_bill_color(img)
# # Crear un objeto de la clase gTTS
tts = gTTS(texto, lang='es')
# Guardar el audio como archivo de MP3
tts.save("billetes.mp3")
#Reproducir
playsound("billetes.mp3")

print(texto)
