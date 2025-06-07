from django.apps import AppConfig
import sys

class ReservaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reserva'

    def ready(self):
        if 'runserver' in sys.argv or 'shell' in sys.argv:
            from .scheduler import start_scheduler
            start_scheduler()
