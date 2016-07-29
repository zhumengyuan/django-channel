from django.conf.urls import url, include
from django.shortcuts import render_to_response


def base_view(request):
    return render_to_response('index.html', {

    })

urlpatterns = [
    # Example:
    url(r'^$', base_view),
    url(r'^channels/', include("django_channel.urls")),
]
