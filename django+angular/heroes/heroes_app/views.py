from django.http import JsonResponse
from django.views import View

class Hero(View):
    def get(self, request):
        return JsonResponse({'status': 'ok'})