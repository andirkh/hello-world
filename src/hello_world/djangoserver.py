from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.core.management import execute_from_command_line

def home(request):
    return HttpResponse("Hello, World from Django!")

def configure_django():
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=__name__,
    )

urlpatterns = [
    path('', home, name='home'),
]

def run_django():
    configure_django()
    execute_from_command_line(["manage.py", "runserver"])