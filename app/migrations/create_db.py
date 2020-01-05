import os
import json
import sys
import pickle
from pathlib import Path
from sqlite3 import connect

sys.path.append("../..")
from app.connector.sqlite import SQLiteConnector

project_dirname = Path.cwd().parents[1]
DB_NAME = "poke.db"
DB_CONNECTOR = SQLiteConnector(project_dir=project_dirname, db_name=DB_NAME)


def load_pickle_file(file: str) -> object:
    return pickle.load(file=open(str(project_dirname) + "/app/data/.pickle", "rb"))


def create_db() -> None:
    """
    Generate project database
    """
    pokedex = load_pickle_file("pokedex")
    moves = load_pickle_file("movement")
    types = load_pickle_file("types")

    DB_CONNECTOR.make_ddl_query(
        """ CREATE TABLE IF NOT EXISTS POKEMON
                ([id] INTEGER PRIMARY KEY,[name] varchar(25),
                 [type] varchar(10), [stats] json, [moves] text)"""
    )

    DB_CONNECTOR.make_ddl_query(
        """ CREATE TABLE IF NOT EXISTS TYPES
                ([id] INTEGER PRIMARY KEY,[name] varchar(25),
                 [double_damage_from] text, [double_damage_to] text,
                 [half_damage_from] text, [half_damage_to] text,
                 [no_damage_from] text, [no_damage_to] text)"""
    )

    DB_CONNECTOR.make_ddl_query(
        """ CREATE TABLE IF NOT EXISTS MOVES
                ([id] INTEGER PRIMARY KEY,[name] varchar(25),
                 [type] varchar(25), [pp] integer, [power] integer,
                 [accuracy] integer)"""
    )

    sql_poke = """
        INSERT INTO pokemon(name, type, stats, moves)
        VALUES(?,?,?,?) """
    sql_moves = """
        INSERT INTO moves(name, type, pp, power, accuracy)
        VALUES(?,?,?,?,?) """
    sql_types = """
        INSERT INTO types(name, double_damage_from, double_damage_to,
                          half_damage_from, half_damage_to, no_damage_from,
                          no_damage_to)
        VALUES(?,?,?,?,?,?,?) """

    for name, poke in pokedex.items():
        DB_CONNECTOR.make_ddl_query(
            sql_poke,
            name,
            " ".join(poke["type"]),
            json.dumps(poke["stats"]),
            " ".join(poke["moves"]),
        )
    for move_name, move in moves.items():
        DB_CONNECTOR.make_ddl_query(
            sql_moves,
            move_name,
            move["type"],
            move["pp"],
            move["power"],
            move["accuracy"],
        )
    for type_name, poke_types in types.items():
        DB_CONNECTOR.make_ddl_query(
            sql_types,
            type_name,
            " ".join(poke_types["double_damage_from"]),
            " ".join(poke_types["double_damage_to"]),
            " ".join(poke_types["half_damage_from"]),
            " ".join(poke_types["half_damage_to"]),
            " ".join(poke_types["no_damage_from"]),
            " ".join(poke_types["no_damage_to"]),
        )


if not os.path.isfile(DB_NAME):
    # Connect this way create the database
    connect(str(project_dirname) + "/" + DB_NAME)
    create_db()
