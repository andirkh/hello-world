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

### additional, docker :
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
RAW: str = 'raw'
DJANGO: str = 'django'
FLASK: str = 'flask'
SOCKETIFY: str = 'socketify'
FAST_API: str = 'fast_api'
```

run via docker image di container via desktop/terminal