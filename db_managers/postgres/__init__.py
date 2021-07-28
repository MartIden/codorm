from dataclasses import dataclass

from contracts import BaseConfigurator, BaseConnection, BaseDBManager, BaseModel


@dataclass
class PostgresConfigurator(BaseConfigurator):
    login: str
    password: str
    db_name: str


class PostgresConnection(BaseConnection):

    def _open_connection(self):
        pass

    def close_connection(self):
        pass


connection = "dddddddd"


class PostgresManager(BaseDBManager):

    _connection = connection

    def execute(self, sql_expression: str) -> bool:
        print(self._connection)
        return True

    def create(self, model: BaseModel):
        pass

    def read(self, primary_key: int):
        pass

    def update(self, model: BaseModel):
        pass

    def delete(self, primary_key: int):
        pass
