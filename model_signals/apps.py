from django.apps import AppConfig


class ModelSignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'model_signals'

    def ready(self):
        import model_signals.signals
        