file_name = "some_file.txt"
log = "results.txt"

#создадим файл с рандомным IP адресами:
with open (file_name, 'w') as f:
    f.writelines(["8.8.8.8\n", "192.192.192.192\n", "193.193.193.193\n", "127.0.0.2"])

#из этого же файла прочитаем IP адреса
with open (file_name, 'r') as ff:
    data = ff.read().split('\n')
    print (data)
    print(type(data))

ip_dict = dict.fromkeys(data, 0) #заявляем, что по умолчанию все статусы доступны

print(ip_dict) #посмотрим, что в словаре

import subprocess
import datetime

while True:
    for IPs in ip_dict.keys():
     status = subprocess.Popen(["ping", "-c", "1", IPs.strip()],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
    stdout, stderr = status.communicate()


    if ip_dict[IPs] != status.returncode:
        with open(log, 'w') as dd:
            dd.write(IPs +" status change time: "+ str(datetime.datetime.now()) + '\n')
            ip_dict[IPs] = status.returncode
    else:
            pass



