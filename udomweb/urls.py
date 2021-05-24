from django.urls import path, include
from . import views
# from django.views.static import serve
# from django.conf.urls import url
urlpatterns = [
    path('',  views.homepage, name="homepage"),
    path('staff/', views.staffpage, name="staffpage"),
]
