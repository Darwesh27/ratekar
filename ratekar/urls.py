from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from api import views

from settings import MEDIA_ROOT
import settings as conf

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ratekar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	# url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include('api.urls', namespace = 'api')),
	url(r'^.*$', views.index),
)
# ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if conf.DEBUG == True:
	urlpatterns = patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
	) + urlpatterns
else:
	urlpatterns = patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': conf.STATIC_ROOT}),
	) + urlpatterns
