import wmi
import time
import random

def change_brightness(brightness):
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)

def main():
    print("Alterando temporariamente o brilho da tela do seu monitor...")
    initial_brightness = 50  # Brilho inicial (entre 0 e 100)
    try:
        change_brightness(random.randint(0, 100))  # Altera o brilho para um valor aleatório
        time.sleep(3)  # Mantém o brilho alterado por 3 segundos
    finally:
        # Restaura o brilho inicial
        change_brightness(initial_brightness)
        print("Brilho da tela restaurado.")

if __name__ == "__main__":
    main()
