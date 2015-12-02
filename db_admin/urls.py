from django.conf.urls import url, include
from django.views.generic import TemplateView

from views import *

urlpatterns = [
    url(r'denied/$', TemplateView.as_view(template_name="denied.html")),

    # Admin
    url(r'add/$', addEntry, name="admin_add"),
    url(r'delete/([0-9]+)/$', deleteEntry, name="admin_delete"),
    url(r'edit/([0-9]+)/$', editEntry, name="admin_edit"),
    url(r'list/$', listEntries, name="admin_list"),
    url(r'show/([0-9]+)/$', showEntry, name="admin_show"),

    url(r'$', listEntries),
]