import os
from rawserver import run_raw
from flaskserver import run_flask

# Engine List
RAW: str = 'raw'
DJANGO: str = 'django'
FLASK: str = 'flask'
SOCKETIFY: str = 'socketify'
FAST_API: str = 'fast_api'

# comment this line below code before building the docker image :
os.environ["ENGINE"] = FLASK

engine = os.environ.get("ENGINE")

def main():
    print('Engine: ', engine)
    if engine == RAW:
        run_raw()
    elif engine == FLASK:
        run_flask()
    else:
        run_raw()

if __name__ == '__main__':
    main()