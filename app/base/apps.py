from django.apps import AppConfig

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.base'
    verbose_name = 'Башкы Бет'

    def ready(self):
        import app.base.translation 