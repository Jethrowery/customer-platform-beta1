from django.apps import AppConfig


class UsermodelConfig(AppConfig):
    name = 'usermodel'

    def ready(self):
    	import usermodel.signals
