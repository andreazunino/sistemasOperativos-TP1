""" importo de la libreria el módulo threading que hace posible la programación con hilos"""
import threading
import time

"""Defino la funcion que cuente hasta 5 en el thread"""
""" A todos los hilos se les asigna, automáticamente, un nombre en el momento de la creación que se puede conocer con el método getName()"""
"""el thread espera 4 segundos"""             
def contar():
    contador = 0
    while contador<5:
        contador+=1
        print('Hilo:', 
              threading.currentThread().getName(), 'Contador:', contador)
        time.sleep(4)
    
   

threads = list()
"""construyo 2 hilos y llamo al metodo start"""
for i in range(2):
    t = threading.Thread(target=contar)
    threads.append(t)
    t.start()