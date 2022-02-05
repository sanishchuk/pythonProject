file_name = "some_file.txt"
log = "results.txt"

#создадим файл с рандомным IP адресами:
with open (file_name, 'w') as f:
    f.writelines(["8.8.8.8\n", "192.192.192.192\n", "193.193.193.193\n", "127.0.0.1"])

#из этого же файла прочитаем IP адреса
with open (file_name, 'r') as ff:
    data = ff.read().split('\n')
    print (data)
    print(type(data))

    import os

import subprocess


while True:

    for line in data:
    response = subprocess.Popen(["ping", "-c", "1", line.strip()],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
    stdout, stderr = response.communicate()
    # print(stdout)
    # print(stderr)

    if (response.returncode == 0):
        status = line.rstrip() + " is Reachable"
    else:
        status = line.rstrip() + " is Not reachable"
    print(status)