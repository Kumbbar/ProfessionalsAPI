import random

from django.db.models import QuerySet
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Person
from .serializers import PersonAdminSerializerAdmin, PersonSerializer


class PersonGetViewSet(
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet
                  ):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Person.objects.all()
    serializer_class = PersonAdminSerializerAdmin


class UpdatePersonsPositions(APIView):
    def get_roms_occupancy(self, data: QuerySet[Person]):
        result = dict()
        for i in range(0, 23):
            result[i] = data.filter(skud_number=i, skud_direction=Person.IN).count()
        return result

    def update_workers_positions(self):
        all_workers: QuerySet[Person] = Person.objects.filter(role=Person.WORKER)
        roms_occupancy = self.get_roms_occupancy(all_workers)
        for worker in all_workers:
            if random.randint(0, 100) < 40:
                continue
            if worker.skud_direction == Person.OUT:
                while True:
                    random_skud_number = random.choice(Person.WORKERS_ONLY_SKUD)
                    if roms_occupancy[random_skud_number] >= 2:
                        continue
                    worker.skud_number = random_skud_number
                    worker.skud_direction = Person.IN
                    roms_occupancy[random_skud_number] += 1
                    break
            else:
                worker.skud_direction = Person.OUT
            worker.save()

    def update_client_positions(self):
        all_clients: QuerySet[Person] = Person.objects.filter(role=Person.CLIENT)
        roms_occupancy = self.get_roms_occupancy(all_clients)
        for client in all_clients:
            if random.randint(0, 100) < 25:
                continue
            if client.skud_direction == Person.OUT:
                while True:
                    random_skud_number = random.choice(Person.WORKERS_ONLY_SKUD)
                    if roms_occupancy[random_skud_number] >= 3:
                        continue
                    client.skud_number = random_skud_number
                    client.skud_direction = Person.IN
                    roms_occupancy[random_skud_number] += 1
                    break
            else:
                client.skud_direction = Person.OUT
            client.save()

    def put(self, request):
        self.update_workers_positions()
        self.update_client_positions()
        return Response(status=status.HTTP_200_OK)
