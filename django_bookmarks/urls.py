from django.conf.urls.defaults import *
from bookmarks.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   	(r'^$', main_page)
 
)
