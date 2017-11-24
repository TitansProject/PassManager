from django.http import HttpResponse
from django.template import loader
from firebase.firebase import FirebaseApplication
from PassManagerApp.firebase_config import FirebaseConfig


def index(request):
    firebase_config = FirebaseConfig()
    fire = FirebaseApplication(firebase_config.databaseURL)
    wifis = fire.get('/text', None)
    template = loader.get_template('PassManagerApp/index.html')
    context = {
        'wifis': wifis,
    }
    return HttpResponse(template.render(context, request))
