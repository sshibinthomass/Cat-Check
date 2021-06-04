from .models import Category
from .models import Risk


def categories(request):
    return {
        'categories': Category.objects.all()
    }

def risks(request):
    return {
        'risks': Risk.objects.all()
    }
