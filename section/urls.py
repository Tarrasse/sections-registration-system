from . import views
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.log_out, name='logout'),
    url(r'^signup$', views.sign_up, name='signup'),
    url(r'^all$', views.all_sections, name='all_sections'),
    url(r'^register$', views.register, name='register'),
    url(r'^$', views.sections, name='sections'),
    url(r'^test$', views.test),
]
