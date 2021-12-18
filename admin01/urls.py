from django.urls import path,include
from .import views


app_name='admin01'
urlpatterns = [
    
    path('index/',views.index,name='index'),
    path('upload_Vlink/',views.upload_Vlink,name='upload_Vlink'),
    path('upload_heading/',views.upload_heading,name='upload_heading'),
    path('update_link/',views.update_link,name='update_link'),
    path('add_team/',views.add_team,name='add_team'),
    #path('add_over/',views.add_over,name='add_over'),
    path('show_team/<int:id>/',views.show_team,name='show_team'),
    path('update_team/',views.update_team,name='update_team'),
    path('score_card/',views.score_card,name='score_card'),
    path('welcome_header/',views.welcome_header,name='welcome_header'),
    path('del_team/<int:id>/',views.del_team,name='del_team'),
    #path('showover/',views.showover,name='showover')

    

]
