import os
import pickle
from pathlib import Path


class ObjectiveDB:
    status = None
    data = None

    def __init__(self, db, obj=None):
        base_path = os.path.abspath('Database')
        self.location = Path(base_path).joinpath(db + ".odb")
        self.db = self._load_db()
        if obj is None:
            self.status = self._retrieve_data()
        else:
            self.status = self._store_data(obj)
        self._close_db()

    def _close_db(self):
        try:
            self.db.close()
            return True
        except:
            return False, "_close_db failed"

    def _load_db(self):
        try:
            if os.path.exists(self.location):
                return open(self.location, "r+b")
            else:
                return open(self.location, "ab")
        except:
            return False, "_load_db failed"

    def _retrieve_data(self):
        try:
            obj = pickle.load(self.db)
            self.data = obj
            return True
        except:
            return False, "_retrieve_data failed"

    def _store_data(self, obj):
        try:
            pickle.dump(obj, self.db)
            return True
        except:
            return False, "_store_data failed"
