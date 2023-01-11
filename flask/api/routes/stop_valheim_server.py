from flask import Blueprint, render_template
import paramiko
import time
from json import load

stop_valheim_server_blueprint = Blueprint(name='stop_valheim_server', import_name=__name__)


@stop_valheim_server_blueprint.route("/stop_valheim_server", methods=['POST', 'GET'])
def stop_valheim_server():
    print("stopping valheim server")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        with open("../configs/secret.json", "r") as json_file:
            secrets = load(json_file)

        valheim_user_name = secrets["valheim_user_name"]
        valheim_user_password = secrets["valheim_user_password"]
        commodus_user_name = secrets["commodus_user_name"]
        commodus_user_password = secrets["commodus_user_password"]
        allspark_ip_address = secrets["allspark_ip_address"]

    except FileNotFoundError as err:

        print("reading .secrets.json failed")

    ssh.connect(allspark_ip_address, username=valheim_user_name, password=valheim_user_password, timeout=10)

    time.sleep(1)

    ssh.exec_command("./vhserver stop")

    time.sleep(1)

    ssh.close()

    time.sleep(1)

    ssh.connect(allspark_ip_address, username=commodus_user_name, password=commodus_user_password, timeout=10)

    stdin, stdout, stderr = ssh.exec_command('sudo shutdown -P now', get_pty=True)
    time.sleep(1)
    stdin.write(strCommodusPw)
    stdin.write("\n")
    time.sleep(1)
    stdin.flush()

    time.sleep(1)

    ssh.close()

    return render_template("index.html")
