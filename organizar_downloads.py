"""
Script para organizar arquivos na pasta Downloads, classificando-os em subpastas por tipo de arquivo,
listando arquivos grandes e limpando arquivos temporários e lixo eletrônico.

Usage:
    Execute este script para organizar os arquivos na pasta Downloads.
    Certifique-se de ter Python instalado e configurado no PATH do sistema.

Author: Danilo Fernando <danilo.bossanova@hotmail.com>
Date: 07/05/2024
"""
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
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documentos': ['.pdf', '.doc', '.docx', '.txt'],
        'Planilhas': ['.xls', '.xlsx', '.csv'],
        'Apresentações': ['.ppt', '.pptx'],
        'Programas': ['.exe', '.dmg', '.deb'],
        'Outros': []  # Arquivos que não se encaixam em nenhuma das categorias acima
    }

    # Cria as pastas se elas ainda não existirem
    for folder in file_types:
        folder_path = os.path.join(folder_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move os arquivos para suas respectivas pastas
    for file in files:
        file_extension = os.path.splitext(file)[1]
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                src_path = os.path.join(folder_path, file)
                dest_path = os.path.join(folder_path, folder, file)
                try:
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


# Caminho da pasta "Downloads"
folder_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# Chama a função para organizar os arquivos na pasta "Downloads"
organize_files(folder_path)
