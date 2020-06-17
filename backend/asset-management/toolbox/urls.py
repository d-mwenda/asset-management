# ideally this app has no urls. those here are to test diff components and aspects of the project
from django.conf.urls import url

# asm imports
from toolbox.views import Test

urlpatterns = [
    url(r'^$', Test.as_view()),
]
