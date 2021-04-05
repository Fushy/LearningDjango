from django.conf.urls import url

from store import views

# Les chemins à partir de la page http://127.0.0.1:8000/store/
urlpatterns = [
    url(r'^$', views.listing),  # "/store" will call the method "index" in "views.py"
]
