"""escalationtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts import views
from django.conf.urls.static import static
from django.conf import settings
from tickets.views import new_ticket, ticket_list, edit_ticket, delete_ticket, import_excel

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^signup/$', views.signup),
    url(r'^tickets/new/$', new_ticket),
    url(r'^tickets/list/$', ticket_list),
    url(r'^tickets/edit/(?P<id>[0-9]+)/$', edit_ticket),
    url(r'^tickets/delete/$', delete_ticket),
    url(r'^tickets/import/$', import_excel)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)