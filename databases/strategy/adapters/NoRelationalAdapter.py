from abc import ABC, abstractmethod


class NoRelationalAdapter(ABC):
    @abstractmethod
    def findAll(self, connection, collection_name):
        pass

    @abstractmethod
    def findOneByData(self, connection, collection_name, query):
        pass

    @abstractmethod
    def insert(self, connection, collection_name, document):
        pass

    @abstractmethod
    def update(self, connection, collection_name, query, updated_data):
        pass

    @abstractmethod
    def delete(self, connection, collection_name, query):
        pass
