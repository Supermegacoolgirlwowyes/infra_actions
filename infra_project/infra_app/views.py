from django.http import HttpResponse


def index(request):
    return HttpResponse('Аллилуйя! У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
