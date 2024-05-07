import ctypes
import time

def change_screen_color(color):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, color, 0)

def main():
    print("Alterando temporariamente a cor da tela...")
    try:
        # Define uma cor de tela temporária (vermelho)
        color = "C:\\Users\\danilo.fernando\\Pictures\\Times\\52065dfe-a53a-4614-9206-292871e43765.jpg"
        change_screen_color(color)
        time.sleep(3)  # Mantém a cor alterada por 3 segundos
    finally:
        # Restaura a cor original da tela
        # Você precisará definir o caminho para o papel de parede original do seu sistema
        original_wallpaper = "\\\\192.168.41.254\\netlogon\\wallpaper.jpg"
        change_screen_color(original_wallpaper)
        print("Cor da tela restaurada.")

if __name__ == "__main__":
    main()
