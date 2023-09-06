from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Pak Bsdaijasldjasljsepe',
        'class': 'PBPdasdas A'
    }

    return render(request, "main.html", context)