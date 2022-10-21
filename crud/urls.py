from django.urls import path

from crud import views

app_name = 'crud'

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/',views.post_detail, name= 'post_detail'),
    path('archive/', views.post_archive, name='post_archive'),

]