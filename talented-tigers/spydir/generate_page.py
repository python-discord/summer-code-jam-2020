from .models import GeneratedPage


# This is where the text will be scraped. Right now, this function only generates an info page with a title
def generate_page(page_name):
    return GeneratedPage.objects.create(page_title=page_name, page_type='INFO')
