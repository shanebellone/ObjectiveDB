# ObjectiveDB

ODB is a minimal object database with zero dependencies written in Python. 

It offers three basic services found in db_services.py:

- retrieve data
- retrieve database
- store data

Custom services can be added to this file. Please note, ObjectiveDB should be accessed via context manager.

## Using ObjectiveDB

**Create a test file in the ObjectiveDB folder.**

Call store_data([db_name], [object], [uid]) to create Database/[db_name].odb:

`db_response = store_data("test_database", {"Test Key": "Test Value"}, "test_uid")`

Call retrieve_data([db_name], [uid]) to retrieve the stored object.

`requested_data = retrieve_data([db_name], [uid])`
