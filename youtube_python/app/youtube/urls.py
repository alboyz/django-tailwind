from django.urls import path
from.  import views

urlpatterns = [
    path('', views.homepage, name="index"),
    path('index/',views.HomeView.as_view())
]