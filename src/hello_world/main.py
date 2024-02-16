import os
import sys

from rawserver import run_raw
from flaskserver import run_flask
from djangoserver import run_django
from socketifyserver import run_socketify
from fastapiserver import run_fastapi

# Engine List
RAW: str = 'RAW'
DJANGO: str = 'DJANGO'
FLASK: str = 'FLASK'
SOCKETIFY: str = 'SOCKETIFY'
FASTAPI: str = 'FASTAPI'

engine = os.environ.get("ENGINE")

if engine == None:
    try:
        engine = sys.argv[1]
    except:
        engine = RAW

print('Your engine is ', engine)

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
    main()