import winsound

def play_system_sound():
    # Código do som do sistema para erro de dispositivo
    winsound.Beep(1000, 500)  # Frequência e duração do som

# Chamando a função para reproduzir o som do sistema
play_system_sound()
