from django.urls import path
from Dashboards import views

urlpatterns =[
    path('',views.home, name='home'),
    path('prediction/',views.prediction_view,name='prediction_view'),
    path('livescore/',views.livescore, name='livescore'),
    path('Analysis/',views.analysis, name='analysis'),
]