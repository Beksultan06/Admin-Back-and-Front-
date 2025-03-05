from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import VisitLog
from django.utils.timezone import now, timedelta

class MetricsView(APIView):
    def get(self, request):
        total_views = VisitLog.objects.count()
        total_visits = VisitLog.objects.values("session_id").distinct().count()
        last_24_hours = now() - timedelta(hours=24)
        total_unique_visitors = VisitLog.objects.filter(action="visit").count()

        data = {
            "views": total_views,
            "visits": total_visits,
            "visitors": total_unique_visitors
        }

        return Response(data)