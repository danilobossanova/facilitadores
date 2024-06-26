import os
import shutil
import tempfile

def organize_files(folder_path):
    """
    Organiza os arquivos na pasta especificada e realiza outras operações de limpeza.

    Args:
        folder_path (str): O caminho da pasta que contém os arquivos a serem organizados.

    Returns:
        None
    """

    # Lista todos os arquivos no diretório especificado
    files = os.listdir(folder_path)

    # Mapeamento de tipos de arquivos para suas respectivas pastas
    file_types = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.JPG'],
        'Documentos': ['.pdf', '.doc', '.docx', '.txt'],
        'Planilhas': ['.xls', '.xlsx', '.csv'],
        'Apresentações': ['.ppt', '.pptx'],
        'Programas': ['.exe', '.dmg', '.deb','.msi', '.pkg'],
        'Videos': ['.mp4'],
        'Jwpub': ['.jwpub'],
        'Zip': ['.zip','.rar'],
        'Jar': ['.jar','.js','.reg','.pem'],
        'iReport': ['.jrxml','.xml'],
        'Apk': ['.apk'],
        'ttf': ['.ttf'],
        'log': ['.log'],
        'Outros': []  # Arquivos que não se encaixam em nenhuma das categorias acima
    }

    # Cria as pastas apenas para os tipos de arquivos que existem na pasta de origem
    existing_folders = set()
    for file in files:
        file_extension = os.path.splitext(file)[1]
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                existing_folders.add(folder)

    # Move os arquivos para suas respectivas pastas
    for file in files:
        file_extension = os.path.splitext(file)[1]
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                src_path = os.path.join(folder_path, file)
                dest_folder_path = os.path.join(folder_path, folder)
                dest_path = os.path.join(dest_folder_path, file)
                try:
                    # Verifica se a pasta de destino já existe
                    if folder in existing_folders and not os.path.exists(dest_folder_path):
                        os.makedirs(dest_folder_path)  # Cria a pasta de destino, se não existir

                    # Verifica se o arquivo ainda existe antes de tentar movê-lo
                    if os.path.exists(src_path):
                        shutil.move(src_path, dest_path)
                        print(f"Arquivo {file} movido para {folder}.")
                    else:
                        print(f"Arquivo {file} não encontrado. Não foi possível movê-lo.")
                except Exception as e:
                    print(f"Falha ao mover arquivo {file}: {e}")

    # Lista arquivos grandes e seus tamanhos
    print("\nArquivos grandes:")
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            # Define o limite de tamanho para considerar um arquivo grande (em bytes)
            size_limit = 10 * 1024 * 1024  # 10 MB
            if file_size > size_limit:
                print(f"Arquivo: {file_path} | Tamanho: {file_size / (1024 * 1024):.2f} MB")

    # Limpa arquivos temporários e lixo eletrônico
    print("\nLimpando arquivos temporários e lixo eletrônico...")
    temp_dirs = [tempfile.gettempdir()]
    for temp_dir in temp_dirs:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Arquivo temporário removido: {file_path}")
                except Exception as e:
                    print(f"Falha ao remover arquivo temporário: {file_path} - {e}")

# Lista de diretórios para organizar
folders_to_organize = [
    "C:\\Users\\danilo.fernando\\Documents",
    "C:\\Users\\danilo.fernando\\Pictures",
    "C:\\Users\\danilo.fernando\\OneDrive",
    "C:\\Users\\danilo.fernando\\Downloads"
]

# Chama a função para organizar os arquivos em cada diretório
for folder in folders_to_organize:
    print(f"\nOrganizando arquivos em: {folder}")
    organize_files(folder)
