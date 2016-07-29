import time
import json
from .helper import get_messages, send_message
from django.http import HttpResponse


def channel_pull(request, name):
    limit = int(request.GET.get("limit", 30))
    timeout = float(request.GET.get("timeouot", 30))
    timestamp = float(request.GET.get("timestamp", time.time()))
    messages = get_messages(name, timestamp, limit, timeout)
    return HttpResponse(
        content=json.dumps(messages),
        content_type='application/json'
    )


def channel_send(request, name):
    ttl = float(request.POST.get("ttl"))
    content = request.POST.get("content")
    send_message(name, data={"ttl": ttl, "content": content})
    return HttpResponse(status=204, content_type='application/json')
