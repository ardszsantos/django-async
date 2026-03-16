import asyncio
import time

import httpx
from django.http import HttpResponse, JsonResponse


def home_view(request):
    html = """
    <html>
    <head><title>Async Django</title></head>
    <body>
        <h1>Django Async View</h1>
        <p>
            A rota <strong>/async/</strong> executa uma view assíncrona que faz um contador de 1 a 5
            usando <code>asyncio.sleep(1)</code> e depois faz uma chamada HTTP com
            <code>httpx.AsyncClient</code> para <code>https://httpbin.org/</code>.
        </p>
        <a href="/async/">Ir para /async/</a>
    </body>
    </html>
    """
    return HttpResponse(html)


async def async_view(request):
    start = time.perf_counter()

    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)

    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)

    elapsed = time.perf_counter() - start

    return JsonResponse({
        "tempo_total_segundos": round(elapsed, 3),
        "status_httpbin": r.status_code,
    })
