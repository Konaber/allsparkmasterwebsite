from flask import Blueprint, render_template
from utils.ssh_connection import connect, disconnect, send_command, send_shutdown
import time
from json import load

stop_valheim_server_blueprint = Blueprint(name='stop_valheim_server', import_name=__name__)


@stop_valheim_server_blueprint.route("/stop_valheim_server", methods=['POST', 'GET'])
def stop_valheim_server():
    print("stopping valheim server")

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

    connect(allspark_ip_address, valheim_user_name, valheim_user_password)

    time.sleep(1)

    send_command("./vhserver stop")

    time.sleep(1)

    disconnect()

    time.sleep(1)

    send_shutdown(allspark_ip_address, commodus_user_name, commodus_user_password)

    print("finished stopping valheim server")

    return render_template("index.html")
