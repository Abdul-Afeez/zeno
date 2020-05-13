from csvapp.models import Log


class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.method == 'GET':
            host = request.get_host()
            method = request.method
            request_information = '{host} {method}'.format(host=host, method=method)
            log = Log(request=request_information)
            log.save()
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
