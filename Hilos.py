import threading
import time

class Hilo(threading.Thread):
    def run(self) -> None:
        print(f'Inicio {self.getName()}')
        time.sleep(1)
        print(f'Terminado: {self.getName()}')

if __name__ == '__main__':
    for i in range(4):
        hilo = Hilo(name=f'Hilo {i+1}')
        hilo.start()  #INVOCA LA FUNCION RUN
        time.sleep(.1)
    hilo.run()