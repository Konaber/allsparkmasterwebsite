from flask import Blueprint, render_template
from wakeonlan import send_magic_packet
import time
from json import load
from utils.ssh_connection import connect, disconnect, send_command

start_valheim_server_blueprint = Blueprint(name='start_valheim_server', import_name=__name__)


@start_valheim_server_blueprint.route("/start_valheim_server", methods=['POST', 'GET'])
def start_valheim_server():
    print("starting valheim server")

    try:
        with open("../configs/secret.json", "r") as json_file:
            secrets = load(json_file)

        valheim_user_name = secrets["valheim_user_name"]
        valheim_user_password = secrets["valheim_user_password"]
        allspark_mac_address = secrets["allspark_mac_address"]
        allspark_ip_address = secrets["allspark_ip_address"]

    except FileNotFoundError as err:

        print("reading .secrets.json failed")

    send_magic_packet(allspark_mac_address)

    time.sleep(60)

    connect(allspark_ip_address, valheim_user_name, valheim_user_password)

    time.sleep(1)

    send_command("./vhserver start")

    time.sleep(1)

    disconnect()

    print("finished starting valheim server")

    return render_template("index.html")
