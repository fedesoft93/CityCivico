from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def tipoDenuncia():
    return render_to_response("tipoDenuncia.html")