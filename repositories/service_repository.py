from __future__ import annotations

from bson.objectid import ObjectId

from models.service import Service


class ServiceRepository:

    def __init__(self, service: Service):
        self.__service = service

    def get_by_id(self, pk: str) -> Service | None:
        try:
            return self.__service.objects.get(id=ObjectId(pk))
        except Exception as e:
            print('Error getting service: ', e)
            return None
