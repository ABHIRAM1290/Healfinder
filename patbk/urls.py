from django.urls import path
from patbk import views

urlpatterns = [
    path("",views.index),
    path("patientreg",views.booking),
    path("hs_login",views.hospitallog),#hospital login page
    path("hs_reg",views.hospitalreg),#hospital registration page
    path("doc_reg",views.docreg),
    path("admin",views.admin_login),
    path("logout",views.logout),
    path("confrm",views.confirm_bk)
]
