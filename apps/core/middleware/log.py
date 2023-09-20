import logging

logger = logging.getLogger("logging_mw")


def simple_logging_middleware(get_response):
    def middleware(request):
        # TODO: Log during request
        http_method = request.method
        host_port = request.get_host()
        url = request.get_full_path()
        content_type = request.content_type
        user_agent = request.headers["user_agent"]
        msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent}"

        logger.info(msg)

        try:
            x = 45 / 0
        except ZeroDivisionError:
            logger.debug("Not possible to divide by zero")

        response = get_response(request)
        # TODO: Log during response

        # TODO: Investigate the response and decide on what to log.

        print("Called during response")

        return response

    return middleware
