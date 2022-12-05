from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
     path('',views.home),
      path('frontpage/',views.frontpage ,name="frontpage"),
    path('frontpage/frontpage/',views.frontpage ,name="frontpage"),

]