file_name = "some_file.txt"
log = "results.txt"

#создадим файл с рандомным IP адресами:
with open (file_name, 'w') as f:
    f.writelines(["191.191.191.191\n", "192.192.192.192\n", "193.193.193.193\n", "127.0.0.1"])

#из этого же файла прочитаем IP адреса
with open (file_name, 'r') as ff:
    data = ff.read().split('\n')
    print (data)
    print(type(data))



    import subprocess
    import datetime

while True:
    for ip in data:
        p = subprocess.Popen('ping ' + ip, stdout=subprocess.PIPE)
        # the stdout=subprocess.PIPE will hide the output of the ping command
        p.wait()
        if p.poll():
            with open (log, 'a') as dd:
                dd.write(ip + " is down " + str(datetime.datetime.now()) + '\n')

        else:
            print(ip + " is up")

        # пока что у меня выходит однократная проверка доступности айпишников с записью в файл лога недоступных. но вот далее:
        # 1. не понимаю как сделать проверку регулярной, с периодичностью например в минуту?
        # 2. как сделать проверку изменения состояния недоступного айпи, если он вдруг стал доступным. не понимаю что и где проверять.