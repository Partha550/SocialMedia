from django.http import HttpResponse
html = b"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Heal Check</title>
    </head>
    <body>
      <h5>System is Healthy</h5>
    </body>
    </html>
"""
class HealthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/healthcheck/':
            return HttpResponse(html)
        response = self.get_response(request)
        return response
