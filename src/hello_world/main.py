import os
from rawserver import run_raw
from flaskserver import run_flask
from djangoserver import run_django
from socketifyserver import run_socketify
from fastapiserver import run_fastapi

# Engine List
RAW: str = 'raw'
DJANGO: str = 'django'
FLASK: str = 'flask'
SOCKETIFY: str = 'socketify'
FASTAPI: str = 'fastapi'

# comment this line below code before building the docker image :
os.environ["ENGINE"] = DJANGO

engine = os.environ.get("ENGINE")

def main():
    if engine == RAW:
        run_raw()
    elif engine == FLASK:
        run_flask()
    elif engine == DJANGO:
        run_django()
    elif engine == SOCKETIFY:
        run_socketify()
    elif engine == FASTAPI:
        run_fastapi()
    else:
        run_raw()

if __name__ == '__main__':
    print('Your engine is ', engine)
    main()