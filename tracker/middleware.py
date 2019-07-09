from django.utils.deprecation import MiddlewareMixin


class PopupMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.is_popup = 'popup' in request.GET
