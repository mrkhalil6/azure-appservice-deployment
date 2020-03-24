from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['POST'])
@permission_classes((AllowAny,))
def postcallview(request):
    x = request.data.get("test")
    return HttpResponse(x)
