from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class BaseModel:
    primary_key: int


@dataclass
class BaseConfigurator:
    host: str
    port: int


class BaseConnection(ABC):
    __instance = None
    _cursor: Any

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, configurator: BaseConfigurator):
        self._configurator = configurator

    @property
    def cursor(self):
        return self._cursor

    @abstractmethod
    def _open_connection(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass


class BaseDBManager(ABC):

    _connection = None

    @abstractmethod
    def execute(self, sql_expression: str) -> bool:
        pass

    @abstractmethod
    def create(self, model: BaseModel):
        pass

    @abstractmethod
    def read(self, primary_key: int):
        pass

    @abstractmethod
    def update(self, model: BaseModel):
        pass

    @abstractmethod
    def delete(self, primary_key: int):
        pass
