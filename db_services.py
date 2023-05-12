from Database.interface import ObjectDatabase


def retrieve_data(database, uid):
    with ObjectDatabase(database) as db:
        return db.hash_table.get(uid)


def retrieve_database(database):
    with ObjectDatabase(database) as db:
        return db


def store_data(database, obj, uid):
    with ObjectDatabase(database) as db:
        return db.add(obj, uid)
