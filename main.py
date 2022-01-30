import subprocess
iplist=["127.0.0.1","8.8.8.8"]
for ip in iplist:
    p = subprocess.Popen('ping '+ip,stdout=subprocess.PIPE)
    # the stdout=subprocess.PIPE will hide the output of the ping command
    p.wait()
    if p.poll():
        print (ip+" is down")
    else:
        print (ip+" is up")
# You end with a log of all the ip addresses