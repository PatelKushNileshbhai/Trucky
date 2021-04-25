from django.urls import path
from .views import *

urlpatterns = [
    path('',Profile,name='Profile'),
    
    path('register/',register_user,name="Register"),
    path('login/',login_user,name="Login"),
    path('logout/',log_out,name="logout"),

    path('change_pass/',change_pass,name="ChangePassword"),
    path('change_pass1/',change_pass1,name="ChangePassword1"),
    
    path('show_data/<str:id>/',show_data,name="show_data"),
    

    path('makeformseeker/',make_req,name="Make_Req"),

    path('provider/',Provider_page,name="Provider"),
    path('seeker/',Seeker_page,name="Seeker"),


    path('discard_pro/<int:pid>/',discard_provider,name="Discard_pro"),
    path('accepted_pro/<int:pid>/',accept_provider,name="Accepted_pro"),
    
]