# Allspark master website: README


## Overview


## Set-Up

### Productive Environment

Run:
```
./build_and_run_container.sh
```

To make a script executable, use ```chmod +x filename.sh```.

### Other helpfull stuff

#### Fix "-bash: /bin/sh^M: bad interpreter: No such file or directory"

```
vim filename
:set fileformat=unix
:wq
```

#### Stop all container, remove them and their images

    1. docker kill $(docker ps -q)
    2. docker rm $(docker ps -a -q)
    3. docker rmi $(docker images -q)
    4. docker volume rm $(docker volume ls -q)

#### Linux dev-environment
```
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r flask/configs/requirements.txt
deactivate
```

