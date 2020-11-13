# storm_python_test
Storm's Python test

## To-do list
[x] create database class
    [x] current_facts dict ({})
    [x] schema_cardinality dict (definied in update_schema()) ({})
[x] Database method to check if schema is well formatted
[ ] Database method to check if input facts is well formatted
[x] Database method to update schema (create a dict with {schema_name: cardinality})
[x] Database method to update update current_facts
    [x] if name doesn't exist in current_facts instantialize Entity and add it to the dict
    [x] call Entity method to update it's facts
[ ] Database method to print all current_facts (it calls all Entities method to print its facts)

[x] create Entity class
    [x] name (str) param
    [x] attributes_cardinality (dict) param
    [x] attributes ({})
[x] Entity method to manage attribute
    [x] Decide if add, reassing or delete
        [x] Entity method to add attribute
        [x] Entity method to reassing attribute
        [x] Entity method to delete attribute
[ ] Entity method to print its attributes


current_facts = {name: entity}
schema_cardinality = {att_name: one|many}
entity -> name, attributes_cardinality, attributes