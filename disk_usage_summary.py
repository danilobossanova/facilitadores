import os


def disk_usage_summary(root_folder, num_top_directories=5):
    """
    Analisa o uso do espaço em disco em diferentes diretórios e exibe um resumo dos maiores consumidores de espaço.

    Args:
        root_folder (str): O diretório raiz a ser analisado.
        num_top_directories (int): O número de principais diretórios a serem incluídos no resumo.

    Returns:
        None
    """

    print(f"Analisando o uso do espaço em disco em '{root_folder}'...")

    # Dicionário para armazenar o uso do espaço em disco para cada diretório
    disk_usage = {}

    # Percorre recursivamente o diretório raiz
    for root, dirs, files in os.walk(root_folder):
        # Remove diretórios cujos nomes começam com '.'
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        # Tenta calcular o tamanho total dos arquivos no diretório atual
        total_size = 0
        for file in files:
            try:
                total_size += os.path.getsize(os.path.join(root, file))
            except FileNotFoundError as e:
                print(f"Erro ao acessar {os.path.join(root, file)}: {e}")
                continue

        # Armazena o uso do espaço em disco para o diretório atual
        disk_usage[root] = total_size

    # Ordena os diretórios pelo uso do espaço em disco (do maior para o menor)
    sorted_directories = sorted(disk_usage.items(), key=lambda x: x[1], reverse=True)

    # Exibe o resumo dos maiores consumidores de espaço
    print("\nResumo dos maiores consumidores de espaço:")
    if sorted_directories:
        for i, (directory, size) in enumerate(sorted_directories[:num_top_directories], start=1):
            print(f"{i}. {directory} - {size / (1024 * 1024):.2f} MB")
    else:
        print("Nenhum diretório encontrado ou nenhum diretório com arquivos.")


# Diretório raiz a ser analisado (C:\Users\danilo.fernando)
root_folder = "C:\\www"

# Número de principais diretórios a serem incluídos no resumo
num_top_directories = 5

# Chama a função para analisar o uso do espaço em disco e exibir o resumo
disk_usage_summary(root_folder, num_top_directories)
