from .models import Film, Director

def films_renderer(request):
    return {
       'films': Film.objects.all(), 'directors': Director.objects.all()
    }