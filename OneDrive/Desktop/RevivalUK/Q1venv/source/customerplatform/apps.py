from django.apps import AppConfig


class CustomerplatformConfig(AppConfig):
    name = 'customerplatform'

    def ready(self):
    	import customerplatform.signals
