import random

from django.db.models import QuerySet
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from api.models import Person
from api.serializers import PersonAdminSerializerAdmin, PersonSerializer


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
    def update_workers_positions(self):
        all_workers: QuerySet[Person] = Person.objects.filter(role=Person.WORKER)
        for worker in all_workers:
            if random.randint(0, 100) < 40:
                continue
            if worker.skud_direction == Person.OUT:
                worker.skud_number = random.choice(Person.WORKERS_ONLY_SKUD)
                worker.skud_direction = Person.IN
            else:
                worker.skud_direction = Person.OUT
            worker.save()

    def update_client_positions(self):
        all_clients: QuerySet[Person] = Person.objects.filter(role=Person.CLIENT)
        for client in all_clients:
            print(Person.CLIENTS_ONLY_SKUD)
            if random.randint(0, 100) < 20:
                continue
            if client.skud_direction == Person.OUT:
                client.skud_number = random.choice(Person.CLIENTS_ONLY_SKUD)
                client.skud_direction = Person.IN
            else:
                client.skud_direction = Person.OUT
            client.save()

    def put(self, request):
        self.update_workers_positions()
        self.update_client_positions()
        return Response(status=status.HTTP_200_OK)
