import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def connect(strIp, strUsername, strPassword):
    retValue = False
    try:
        ssh.connect(strIp, username=strUsername, password=strPassword, timeout=10)
        retValue = True
    except:
        print("ERROR: SSH exception, is the Allspark awake?")
        retValue = False
    return retValue

def disconnect():
    ssh.close()

def send_command(strCommand):
    stdin, stdout, stderr = ssh.exec_command(strCommand)
    exit_status = stdout.channel.recv_exit_status()
    if exit_status == 0:
        print("Success")
    else:
        print("Error")
        stdoutLines = stdout.readlines()
        output = ""
        for line in stdoutLines:
            output=output+line
        print(output)
    return stdout

def send_shutdown(strIp, strUsername, strPassword):
    connect(strIp, strUsername, strPassword)

    stdin, stdout, stderr = ssh.exec_command('sudo shutdown -P now', get_pty=True)
    time.sleep(1)
    stdin.write(strPassword)
    stdin.write("\n")
    time.sleep(1)
    stdin.flush()

    ssh.close()
