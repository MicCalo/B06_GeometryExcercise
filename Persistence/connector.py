# coding: utf8

import sqlite3
import pymysql
import logging

class Connector:
    def __init__(self, name: str, get_version_string: str):
        self.name = name
        self.get_version_string = get_version_string


    def connect(self):
        pass


    def fetch_one(self, query):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        db.close()

        return result


    def fetch_all(self, query, with_header: bool = False):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(query)
        result = list(cursor.fetchall())

        # if with_header is true, add the column names as first row
        if with_header:
            headers = []
            for col_desc in cursor.description:
                headers.append(col_desc[0])
            result.insert(0, tuple(headers))

        cursor.close()
        db.close()

        return result


    def execute_statement(self, query):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(query)
        last_row_id = cursor.lastrowid
        cursor.close()
        db.commit()
        db.close()
        return last_row_id


    def get_version(self):
        version = self.fetch_one(f'SELECT {self.get_version_string}()')
        return f'{self.name} version {version[0]}'
    

class MySqlConnector(Connector):
    def __init__(self, hostname: str, port: int, user: str, password:str, database_name:str):
        Connector.__init__(self, 'MySQL', 'VERSION')
        self.hostname=hostname
        self.port=port
        self.user=user
        self.password=password
        self.database_name=database_name

    def connect(self):
        db = pymysql.connect(
            host=self.hostname,
            user=self.user,
            port=self.port,
            passwd=self.password,
            database=self.database_name
        )
        return db
    

class SqliteConnector(Connector):
    def __init__(self, filename):
        Connector.__init__(self, 'SQLite', 'sqlite_version')
        self.filename=filename

    def connect(self):
        db = sqlite3.connect(self.filename)
        db.cursor().execute('PRAGMA foreign_keys = ON')
        return db
    
    
def create_connector(db_config: dict) -> Connector:
    type = db_config['type']
    if type == 'SQLITE':
        logging.info("using SQLite as DB driver")
        return SqliteConnector(db_config['file_name'])
    elif type == 'MYSQL':
        logging.info("using SQLite as DB driver")
        return MySqlConnector(
            hostname=db_config['hostname'],
            port=db_config['port'], 
            user=db_config['user'], 
            password=db_config['password'], 
            database_name=db_config['database_name'])
    else:
        logging.info(f"Unknown DB driver type {type}")
        raise NotImplementedError(f"DB type '{type}'")
