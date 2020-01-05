from sqlite3 import connect
from typing import Any, List


class SQLiteConnector:
    """Connector class to SQLite database"""

    def __init__(self, project_dir, db_name) -> None:
        self.dir = project_dir
        self.db_name = db_name

    def make_ddl_query(self, query, *args) -> None:
        """
        Make a DDL query ej. CREATE TABLE...

        :param query: Query
        :type query: str
        """
        with connect(str(self.dir) + "/" + self.db_name) as c:
            cursor = c.cursor()
            cursor.execute(query, args) if args else cursor.execute(query)
            c.commit()

    def make_query(self, query) -> List[Any]:
        """Make query to SQLite

        :param query: [description]
        :type query: [type]
        :return: [description]
        :rtype: [type]
        """
        with connect(self.dir + "/" + self.db_name) as c:
            cursor = c.cursor()
            cursor.execute(query)
            return cursor.fetchall()
