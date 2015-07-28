from django.conf.urls import url
from django.views.generic import TemplateView

from views import *

urlpatterns = [
    # Search
    url(r'^questions/$', TemplateView.as_view(template_name="questions.html"), name="questions"),
    url(r'^results/$', search_results, name="results"),
    url(r'^results/fulllist/$', full_list, name="fulllist"),
]