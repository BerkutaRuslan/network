from django.utils.timezone import now

from accounts.models import User


class SetLastVisitMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        user = request.user
        if user.is_authenticated:
            User.objects.filter(pk=user.id).update(last_activity=now())
            return response
        else:
            return response
