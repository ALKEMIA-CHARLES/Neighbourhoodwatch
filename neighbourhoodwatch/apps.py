from django.apps import AppConfig


class NeighbourhoodwatchConfig(AppConfig):
    name = 'neighbourhoodwatch'



    def ready(self):
        import neighbourhoodwatch.signals