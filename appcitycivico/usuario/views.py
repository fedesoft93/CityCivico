from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def usuario(request):
    return render_to_response("usuario.html")