from django.shortcuts import render


def home(request):
    return render(request, 'cars/home.html', {
        'ad': request.POST.get('ad', '').upper(),
        'familiya': request.POST.get('soyad', '').upper()
    })