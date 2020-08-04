from django.conf import settings
from django.http import HttpResponse

index_file_path = str(settings.REACT_APP_DIR / 'out' / 'index.html')

def index(request):
    try:
        with open(index_file_path) as f:
            return HttpResponse(f.read())
    except FileNotFoundError:
        logging.exception('Production build of app not found')
        return HttpResponse(
            status=501,
        )

