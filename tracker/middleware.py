from django.utils.deprecation import MiddlewareMixin


class PopupMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        request.is_popup = 'popup' in request.GET
