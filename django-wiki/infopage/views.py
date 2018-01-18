from django.shortcuts import redirect, render



def information(request):
    return render(request, 'info.html')
