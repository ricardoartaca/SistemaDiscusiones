from django.conf.urls import patterns, include, url
#from .views import ExtraDataView

urlpatterns = patterns('',
	url(r'^log-out/$' , 'apps.users.views.logOut', name='logout'),
    #url(r'^extra-data/$' , ExtraDataView.as_view(), name='extra_data'),
)