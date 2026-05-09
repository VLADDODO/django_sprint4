from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Конфигурация вспомогательного приложения Core."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Ядро'
