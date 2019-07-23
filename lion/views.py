from django.shortcuts import render #módulo do djando

# Create your views here.
def pagina_inicial(request):
    context = {"nome": "kaio", "cachorros": ["mel", "tobias", "bob", "madona", "radija"]}
    return render(request, 'index.html', context)
