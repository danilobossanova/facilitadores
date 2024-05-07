import os
import platform
import psutil
import win32com.client

def get_storage_info():
    partitions = psutil.disk_partitions(all=True)
    storage_info = []

    for partition in partitions:
        if 'cdrom' in partition.opts or partition.fstype == '':
            # Ignorar unidades de CD-ROM e partições sem sistema de arquivos
            continue
        partition_info = {
            'device': partition.device,
            'mountpoint': partition.mountpoint,
            'type': partition.fstype,
            'total_size': psutil.disk_usage(partition.mountpoint).total,
            'free_space': psutil.disk_usage(partition.mountpoint).free
        }
        storage_info.append(partition_info)

    return storage_info

def get_processor_info():
    return platform.processor()

def get_memory_info():
    return psutil.virtual_memory().total

def get_bios_year():
    return platform.system() + ' ' + platform.release()

def get_office_info():
    try:
        office_app = win32com.client.Dispatch("Excel.Application")
        office_version = office_app.Version
        office_app.Quit()
        return office_version
    except Exception as e:
        return "Pacote Office não encontrado."

def collect_machine_info():
    machine_info = {
        'Storage': get_storage_info(),
        'Processor': get_processor_info(),
        'Memory': get_memory_info(),
        'BIOS Year': get_bios_year(),
        'Operating System': platform.platform(),
        'Office Version': get_office_info()
    }

    return machine_info

def save_machine_info(machine_name, machine_info, save_path):
    filename = os.path.join(save_path, f"{machine_name}.txt")

    with open(filename, 'w') as f:
        for category, data in machine_info.items():
            f.write(f"{category}:\n")
            if isinstance(data, list):
                for item in data:
                    f.write(f"\t{item}\n")
            else:
                f.write(f"\t{data}\n")

# Nome da máquina na rede
machine_name = platform.node()

# Diretório onde o arquivo será salvo
save_path = r"Y:\TI\Danilo\teste"

# Coletar informações da máquina
machine_info = collect_machine_info()

# Salvar as informações em um arquivo de texto
save_machine_info(machine_name, machine_info, save_path)

print("Informações da máquina coletadas e salvas com sucesso!")
