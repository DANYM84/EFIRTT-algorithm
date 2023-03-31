import pytesseract
import numpy as np
import cv2 
import pathlib
import os
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist 
import nltk
import re
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.test.portuguese_en_fixt import setup_module
sw = stopwords.words('portuguese')
import heapq
import Normaliser

def NormaliserText(string):
  chars = '.,!“”'
  res = string.translate(str.maketrans('', '', chars))  

  norm = Normaliser(tokenizer='readable', capitalize_inis=True, 
                          capitalize_pns=True, capitalize_acs=True, 
                          sanitize=True)
  text_v1 = norm.normalise(res)
  text = re.sub(",","", text_v1)
  stopwords = nltk.corpus.stopwords.words('portuguese')
  virgulas = [","]
  text_v1 = ' '.join([k for k in text.split(" ") if k not in stopwords])
  text_v2 = re.sub(",","", text_v1)
  return text_v2

print(NormaliserText("aaaaaaa..a.a.a.aa,,"))