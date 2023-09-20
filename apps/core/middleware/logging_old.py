# This is the best practice to import your settings
# It will import settings of the current running setting file.
from django.conf import settings
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from apps.core.logging import Logging


logging = Logging(str(settings.BASE_DIR / "logs" / "req_res_log.txt"))


def simple_logging_middleware(get_response):
    def middleware(request):
        # TODO: Log during request
        http_method = request.method
        host_port = request.get_host()
        url = request.get_full_path()
        content_type = request.content_type
        user_agent = request.headers["user_agent"]
        msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent}"

        logging.info(msg)

        response = get_response(request)
        # TODO: Log during response

        # TODO: Investigate the response and decide on what to log.

        print("Called during response")

        return response

    return middleware


class ViewExecutionTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # TODO: pre-process
        start_time = timezone.now()

        response = self.get_response(request)

        # TODO: post-process
        total_time = timezone.now() - start_time

        http_method = request.method
        host_port = request.get_host()
        url = request.get_full_path()
        logging.info(
            f"Execution Time: {total_time} >> {http_method} | {host_port}{url}"
        )

        return response


class ViewExecutionTime2Middleware(MiddlewareMixin):
    def process_request(self, request):
        # TODO: pre-process
        # Since the request is passed to the process_response, we can just patch it in there
        request.start_time = timezone.now()

    def process_response(self, request, response):
        # TODO: post-process
        total_time = timezone.now() - request.start_time

        # re-use what we saw in the simple logging
        http_method = request.method
        host_port = request.get_host()
        url = request.get_full_path()

        logging.info(
            f"Execution Time: {total_time} >> {http_method} | {host_port}{url}"
        )
        return response
