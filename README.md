# Cara pakai

### install Nix
link download nixpkgs https://nixos.org/download (tdk perlu NixOS)

### masuk ke nix-shell
```bash
nix-shell
```
nanti dia akan download dependencies yg ada di shell.nix. saya cuma masukin git, python 3.11, pip dan pdm

### run python code
```bash
pdm run start
```

or specify your engine
```bash
pdm run start DJANGO
# list: RAW, DJANGO, SOCKETIFY, FASTAPI, FLASK
```

### additional, docker (not recommended way) :
build docker image 
```bash
docker build -t hello-world .
```
or
```bash
pdm run build
```

remove :
```python
os.environ["ENGINE"] = XXX
```

fill the ENVIRONMENT VARIABLE in Docker before you run the container. Here's the list of the variable :
```python
RAW: str = 'RAW'
DJANGO: str = 'DJANGO'
FLASK: str = 'FLASK'
SOCKETIFY: str = 'SOCKETIFY'
FASTAPI: str = 'FASTAPI'
```

run via docker image di container via desktop/terminal