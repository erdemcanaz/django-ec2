from django.utils import timezone as django_timezone
from django.http import JsonResponse, HttpResponse

def get_material_datasheet_api(request):
    return JsonResponse({'status': "hello world!"})
    