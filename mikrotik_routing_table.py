import paramiko
from dotenv import load_dotenv
import os

# Загружаем переменные среды из файла .env
load_dotenv()

# Получаем переменные из файла .env
router_ip = os.getenv("MIKROTIK_IP")
router_port = int(os.getenv("MIKROTIK_PORT"))
router_username = os.getenv("MIKROTIK_USERNAME")
router_password = os.getenv("MIKROTIK_PASSWORD")

# Создаем SSH-соединение
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(router_ip, port=router_port, username=router_username, password=router_password)

    # Отправляем команду и получаем результат
    stdin, stdout, stderr = ssh.exec_command('/ip/route/print terse')
    output = stdout.read().decode('utf-8')

    # Выводим информацию о таблице маршрутизации
    print("Routing Table:")
    print(output)

except Exception as e:
    print(f'Error: {e}')

finally:
    # Закрываем соединение
    ssh.close()
