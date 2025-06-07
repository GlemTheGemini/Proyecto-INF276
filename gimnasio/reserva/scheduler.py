from django.db import connection
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

def reset_capacidad_sql():
    print("Base de datos restaurada.")
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bloques_gimnasio SET capacidad_actual = 0;")
        cursor.execute("UPDATE auth_user SET tiene_reserva = FALSE;")

def start_scheduler():
    print("Iniciando scheduler...")
    scheduler = BackgroundScheduler(timezone='America/Santiago')
    scheduler.add_job(
        reset_capacidad_sql,
        CronTrigger(hour=7+4, minute=0)
    )
    if not scheduler.running:
        scheduler.start()
        print("Scheduler iniciado")
    