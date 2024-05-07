import os
import platform
import psutil
import win32com.client
import subprocess

def get_storage_info():
    partitions = psutil.disk_partitions(all=True)
    storage_info = []

    for partition in partitions:
        if partition.device.startswith('Y:'):
            # Ignorar a unidade Y
            continue
        if 'cdrom' in partition.opts or partition.fstype == '':
            # Ignorar unidades de CD-ROM e partições sem sistema de arquivos
            continue
        partition_info = {
            'device': partition.device,
            'mountpoint': partition.mountpoint,
            'type': partition.fstype,
            'total_size': convert_bytes(psutil.disk_usage(partition.mountpoint).total),
            'free_space': convert_bytes(psutil.disk_usage(partition.mountpoint).free)
        }
        storage_info.append(partition_info)

    return storage_info

def get_processor_info():
    return platform.processor()

def get_memory_info():
    return convert_bytes(psutil.virtual_memory().total)

def get_bios_year():
    return platform.system() + ' ' + platform.release()

def get_system_info():
    return platform.platform()

def get_office_info():
    try:
        office_app = win32com.client.Dispatch("Excel.Application")
        office_version = office_app.Version
        office_app.Quit()
        return office_version
    except Exception as e:
        return "Pacote Office não encontrado."

def get_gpu_info():
    try:
        command_output = subprocess.check_output(['wmic', 'path', 'win32_videocontroller', 'get', 'name'], universal_newlines=True)
        gpu_name = [x.strip() for x in command_output.split('\n') if x.strip()][1]
        return gpu_name
    except Exception as e:
        return "Informação não disponível."

def get_network_info():
    network_info = {}
    try:
        network_info['IP Address'] = psutil.net_if_addrs()['Ethernet'][0].address
        network_info['Netmask'] = psutil.net_if_addrs()['Ethernet'][0].netmask
        network_info['Gateway'] = psutil.net_if_addrs()['Ethernet'][0].broadcast
        network_info['MAC Address'] = psutil.net_if_addrs()['Ethernet'][0].address
        network_info['Speed'] = psutil.net_if_stats()['Ethernet'].speed
        network_info['Status'] = psutil.net_if_stats()['Ethernet'].isup
    except Exception as e:
        network_info['Status'] = "Informação não disponível."
    return network_info

def get_running_processes():
    running_processes = []
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        process_info = {
            'PID': process.info['pid'],
            'Name': process.info['name'],
            'CPU Percent': process.info['cpu_percent'],
            'Memory Percent': process.info['memory_percent']
        }
        running_processes.append(process_info)
    return running_processes

def get_battery_info():
    battery_info = {}
    try:
        battery = psutil.sensors_battery()
        battery_info['Plugged'] = battery.power_plugged
        battery_info['Percentage'] = battery.percent
        battery_info['Remaining Time'] = battery.secsleft
    except Exception as e:
        battery_info['Plugged'] = "Informação não disponível."
    return battery_info

def convert_bytes(bytes):
    """
    Converte bytes para megabytes (MB) ou gigabytes (GB), dependendo do tamanho.

    Args:
        bytes (int): O tamanho em bytes.

    Returns:
        str: O tamanho formatado em MB ou GB.
    """
    if bytes >= 1024 ** 3:
        return f"{bytes / (1024 ** 3):.2f} GB"
    else:
        return f"{bytes / (1024 ** 2):.2f} MB"

def collect_machine_info():
    machine_info = {
        'Storage': get_storage_info(),
        'Processor': get_processor_info(),
        'Memory': get_memory_info(),
        'BIOS Year': get_bios_year(),
        'Operating System': get_system_info(),
        'Office Version': get_office_info(),
        'GPU': get_gpu_info(),
        'Network': get_network_info(),
        'Running Processes': get_running_processes(),
        'Battery': get_battery_info()
    }

    return machine_info

def save_machine_info(machine_name, machine_info, save_path):
    filename = os.path.join(save_path, f"{machine_name}.txt")

    with open(filename, 'w') as f:
        for category, data in machine_info.items():
            f.write(f"{category}:\n")
            if isinstance(data, list):
                for item in data:
                    for key, value in item.items():
                        f.write(f"\t{key}: {value}\n")
                    f.write('\n')
            elif isinstance(data, dict):
                for key, value in data.items():
                    f.write(f"\t{key}: {value}\n")
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
