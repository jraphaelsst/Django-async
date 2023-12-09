import asyncio
import httpx
import time

from django.http import HttpResponse, JsonResponse

'''
def api(request):
    time.sleep(1)
    payload = {
        'message': 'Hello world!'
    }
    
    if 'task_id' in request.GET:
        payload['task_id'] = request.GET['task_id']
    
    return JsonResponse(payload)
'''


def http_call_sync():
    
    for num in range(1, 6):
        sleep(1)
        print(num)
    
    r = httpx.get('https://httpbin.org/')
    print(r)


def sync_view(request):
    
    http_call_sync()
    
    return HttpResponse('Blocking HTTP Request')


async def http_call_async():
    
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    
    async with httpx.AsyncClient() as client:
        r = await client.get('https://httpbin.org/')
        print(r)


async def async_view(request):
    
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    
    return HttpResponse('Non-blocking HTTP Request')
