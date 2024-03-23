from django.db import models


class Person(models.Model):
    CLIENT = 'Клиент'
    WORKER = 'Сотрудник'
    ROLES_CHOICES = [
        (CLIENT, 'Клиент'),
        (WORKER, 'Сотрудник')
    ]

    IN = 'in'
    OUT = 'out'
    SKUD_DIRECTIONS_CHOICES = [
        (IN, 'in'),
        (OUT, 'out')
    ]

    ALL_SKUD = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22
    )
    WORKERS_ONLY_SKUD = (
        2, 3, 4, 5, 6, 9, 10,
        11, 13, 16, 17, 18, 20, 22
    )
    CLIENTS_ONLY_SKUD = list(set(ALL_SKUD) - set(WORKERS_ONLY_SKUD))

    role = models.CharField(
        max_length=20,
        choices=ROLES_CHOICES,
        default=CLIENT,
    )
    skud_number = models.IntegerField(default=0)
    skud_direction = models.CharField(
        max_length=20,
        choices=SKUD_DIRECTIONS_CHOICES,
        default=OUT,
    )
    skud_datetime = models.DateTimeField(auto_now=True)
