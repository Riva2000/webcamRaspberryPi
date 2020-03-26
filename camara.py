import os
import time
import sys
print ("Inicio")
print ("Capturando imagen")
os.system("fswebcam image.jpg")
time.sleep(10)

print ("terminado")
sys.exit()