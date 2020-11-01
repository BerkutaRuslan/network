from django.utils.timezone import now

from accounts.models import User


class SetLastVisitMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        return self.get_response(request)

    def process_request(self, request):
        response = self.get_response(request)
        user = request.user
        User.objects.filter(pk=user.id).update(last_login=now())
        return response
