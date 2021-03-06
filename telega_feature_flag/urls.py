"""telega_feature_flag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import gargoyle

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from playground.views import index_gargoyle, index_waffle
import nexus

gargoyle.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # we need a special frontend for gargoyle ff management, it gives more
    # abilities to customize conditions who see feature and who don't
    url(r'^admin/feature-flags/', include(nexus.site.urls)),
    url(r'^g/', index_gargoyle, name='gargoyle'),

    url('^nexus/', include(nexus.site.urls)),

    url(r'^w/', index_waffle, name='waffle'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
