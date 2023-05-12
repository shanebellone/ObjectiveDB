from Database._database import ObjectiveDB


class ObjectDatabase:
    hash_table: dict

    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self._load_db()
        return self

    def __exit__(self, type, value, traceback):
        del self.hash_table

    def _load_db(self):
        db = ObjectiveDB(self.db)
        if db.data is None:
            self.hash_table = {}
        else:
            self.hash_table = db.data

    def _save_db(self):
        register = ObjectiveDB(self.db, self.hash_table)
        return register.status

    def add(self, obj, uid):
        is_duplicate = uid in self.hash_table.keys()
        if is_duplicate is True:
            return KeyError("Duplicate UID")
        else:
            self.hash_table.update({uid: obj})
            status = self._save_db()
        return status

    def retrieve(self, uid, val_key):
        obj_dict = self.hash_table.get(uid)
        obj = obj_dict.get(val_key)
        return obj
