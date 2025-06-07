from django.shortcuts import render,redirect
from .models import Reserva  
from django.db import connection
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def guardar_reserva(request):
    if request.method == 'POST':
        user_id = request.user.id
        username = request.user.username
        bloque = None

        # Consultamos el valor actual desde la base de datos
        with connection.cursor() as cursor:
            cursor.execute("SELECT tiene_reserva FROM auth_user WHERE id = %s", [user_id])
            resultado = cursor.fetchone()

        if resultado and not resultado[0]:  # Si no tiene reserva
            bloque = request.POST.get('bloque')

            # Aquí pones la lógica para aumentar +1 en capacidad_actual según el bloque seleccionado
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE bloques_gimnasio
                    SET capacidad_actual = capacidad_actual + 1
                    WHERE id = %s
                """, [bloque])

            # Marcar al usuario como que ya reservó
            with connection.cursor() as cursor:
                cursor.execute("UPDATE auth_user SET tiene_reserva = true WHERE id = %s", [user_id])
            

        return render(request, 'reserva_confirmed.html',{'user_id': username, 'reserva': bloque})
    
    return redirect('reserva')


def reserva_confirmed(request):
    return render(request, 'reserva_confirmed.html')


@login_required
def reserva(request):
    user_id = request.user.id
    username = request.user.username
    
    # --- 1. Consultar bloques disponibles ---
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id 
            FROM bloques_gimnasio 
            WHERE esta_lleno = false
            ORDER BY id
        """)
        resultados = cursor.fetchall()  # [(1,), (2,), ...]

    bloques = [(bloque[0], f"{(bloque[0]*2)-1}-{bloque[0]*2}") for bloque in resultados]

    # --- 2. Consultar si el usuario ya tiene reserva ---
    with connection.cursor() as cursor:
        cursor.execute("SELECT tiene_reserva FROM auth_user WHERE id = %s", [user_id])
        resultado = cursor.fetchone()

    tiene_reserva = resultado[0] if resultado else False

    # --- 3. Enviar todo al template ---
    return render(request, 'reserva.html', {
        'bloques': bloques,
        'tiene_reserva': tiene_reserva,
        'user': username,
    })




