from django.shortcuts import render,redirect
from .models import Reserva  

# Create your views here.
def reserva(request):
    return render(request, 'reserva.html')



def guardar_reserva(request):
    if request.method == 'POST':
        bloque = request.POST.get('bloque')
        if bloque:
            Reserva.objects.create(bloque=bloque)
        return redirect("reserva")  # Redirige a una página después de guardar
