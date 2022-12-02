from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Kosciol.models import Ksiadz

# Create your views here.
def index(request):
    template = loader.get_template('Kosciol/index.html')
    badRequest = HttpResponse(template.render())
    badRequest.status_code = 500
    ksiadz = [Ksiadz("Juan Pablo Secundo", 37),
                Ksiadz("Sławoj-Leszek Głódż", 81),
                Ksiadz("Jacuś Kowalski", 8),
                Ksiadz("Stanisław Dziwisz", 49),
                Ksiadz("Tadeusz Wojda", 68),
                Ksiadz("Aleksander Babieńko", 9)
    ]
    context={
        'nazwa_parafii' : 'św. Aleksandra Babieńki patrona sportowców i agentów nieruchomościowych',
        'ksiadz' : ksiadz
    }
    response = render(request, 'Kosciol/index.html', context)
    return response