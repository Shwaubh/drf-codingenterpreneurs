import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    params = request.GET  # url query params
    print(params)
    body = request.body  # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)  # loads take a json like string -> python dict object
    except:
        pass
    data['params'] = request.GET
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
