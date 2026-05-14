from django.http import JsonResponse


def home_page(request):
    return JsonResponse(
        {'message': 'ok'}
    )