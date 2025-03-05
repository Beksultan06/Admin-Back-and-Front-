import json
from django.utils.timezone import now
from .models import VisitLog

class VisitLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.session_key:
            request.session.create()
        session_id = request.session.session_key

        if not VisitLog.objects.filter(session_id=session_id, action="visit").exists():
            VisitLog.objects.create(session_id=session_id, action="visit")

        return self.get_response(request)