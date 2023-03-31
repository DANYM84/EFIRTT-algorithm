#========================= IMPORTS ================================#
import pytesseract
import numpy as np
import cv2 
#import cv2_imshow
import pathlib
import os
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist 
import nltk
import re
#nltk.download('punkt')
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.test.portuguese_en_fixt import setup_module
sw = stopwords.words('portuguese')
import heapq
import openai                                               
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
#========================= IMPORTS ================================#
#==================================================================#
# define o caminho da pasta onde a imagem está
folder_path = "D:/apipython/images"
# obter o nome do arquivo da imagem
filename = "image1.webp"
# juntar o caminho completo da imagem usando o caminho da pasta e o nome do arquivo
image_path = os.path.join(folder_path, filename)
img = cv2.imread(image_path , 0)
window_name = 'image'
cv2.imshow(window_name , img) #Mostrar Imagem
cv2.waitKey(0)
cv2.destroyAllWindows()
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
texto = pytesseract.image_to_string(img)
print(texto)


def captureIMG(path_file):
    #================== Capture input img to _img_ variable ====================#
    for filename in os.listdir(path_file):
        if filename.endswith(".jpg" or ".webp" or ".jpeg" or ".png"):
            img_path = os.path.join(path_file, filename)
            img = cv2.imread(img_path ,0) #Use 0 for gray images and 1 for normal images
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    #===========================================================================#
    #============== Capture input _img_ and transform to string ================#
            list_strings = []       
            text = pytesseract.image_to_string(img)
            list_strings.append(text)
            print(list_strings)
            
captureIMG("D:/apipython/images")