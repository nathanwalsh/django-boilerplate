from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.template.response import TemplateResponse
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots.txt$',
        lambda request: TemplateResponse(
            request,
            template='robots.txt',
            context={'allow_robots': settings.ALLOW_ROBOTS},
            content_type='text/plain',
        )
    ),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
