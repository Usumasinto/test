from importlib.metadata import distributions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from zones.api.serializers import DistributionSerializer
from zones.api.serializers import ZoneSerializer

from zones.models import Zone
from zones.models import Distribution




@api_view(['GET', 'PUT'])
def edit(request):
    zone_id = request.data.get('id')
    name = request.data.get('name')

    zone = Zone.objects.filter(pk=zone_id).first()
    if not zone:
        return Response('', status=status.HTTP_400_BAD_REQUEST)

    zone.name = name
    zone.save()

    return Response()


@api_view(['DELETE'])
def deleteZone(request, pk):
    zone= Zone.objects.get(id=pk)
    zone.delete()

    return Response('zone was deleted')



