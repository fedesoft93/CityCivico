from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def principal():
    return render_to_response("estadoDenuncia.html")