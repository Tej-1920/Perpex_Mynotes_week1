from django.apps import AppConfig


class NoteModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'note_model'

def ready(self):
    import note_model.signals
