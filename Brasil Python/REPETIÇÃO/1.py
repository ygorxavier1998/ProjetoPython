
from EmulatorGUI import GPIO
import RPi.GPIO as GPIO
import time
import traceback

def Main():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
      
        GPIO.setup(2, GPIO.OUT, initial = GPIO.LOW) #VERMELHO
        GPIO.setup(3, GPIO.OUT, initial = GPIO.LOW) # AMARELO
        GPIO.setup(4, GPIO.OUT, initial = GPIO.LOW) # VERDE
	#--------------------------------------------#
        GPIO.setup(15, GPIO.OUT, initial = GPIO.LOW) # AMARELO
        GPIO.setup(14, GPIO.OUT, initial = GPIO.LOW) # VERDE
	    
	#--------------------------------------#
	#BOTÃO DO SEMAFORO
	    GPIO.setup(17, GPIO.IN)
        int verde = 20
        int amarelo = 3
        int vermelho = 15
        while(True):
            if(GPIO.input(17) == True):
                GPIO.output(15, GPIO.HIGH)  #VERDE ON
                time.sleep(10)  
                GPIO.output(15, GPIO.LOW)  #VERDE ON
                GPIO.output(14, GPIO.HIGH)   # VERDE OFF
                time.sleep(10)
                GPIO.output(14, GPIO.LOW)   # VERDE OFF  
            else:
                GPIO.output(4, GPIO.HIGH)  #VERDE ON
                time.sleep(verde)             #aguardar 10 segundos
                GPIO.output(4, GPIO.LOW)   # VERDE OFF
                #--------------------------------------#
                GPIO.output(3, GPIO.HIGH)  #AMARELO ON
                time.sleep(amarelo)             #aguardar 10 segundos
                GPIO.output(3, GPIO.LOW)   #AMARELO OFF
                #--------------------------------------#
                GPIO.output(2, GPIO.HIGH)  #ligar luz amarela
                time.sleep(vermelho)              #aguardar 3 segundos
                GPIO.output(2, GPIO.LOW)   #desligar luz amarela
            

    except Exception as ex:
        traceback.print_exc()
    finally:
        GPIO.cleanup() #this ensures a clean exit
        
Main()