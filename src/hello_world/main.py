import os
from rawserver import run_raw
from flaskserver import run_flask
from djangoserver import run_django
from socketifyserver import run_socketify

# Engine List
RAW: str = 'raw'
DJANGO: str = 'django'
FLASK: str = 'flask'
SOCKETIFY: str = 'socketify'
FAST_API: str = 'fast_api'

# comment this line below code before building the docker image :
os.environ["ENGINE"] = SOCKETIFY

engine = os.environ.get("ENGINE")

def main():
    print('Engine: ', engine)
    if engine == RAW:
        run_raw()
    elif engine == FLASK:
        run_flask()
    elif engine == DJANGO:
        run_django()
    elif engine == SOCKETIFY:
        run_socketify()
    else:
        run_raw()

if __name__ == '__main__':
    main()