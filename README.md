# storm_python_test
Storm's Python test

## To-do list
[x] create database class
    [x] current_facts dict ({})
    [x] schema_cardinality dict (definied in update_schema()) ({})
[x] Database method to check if schema is well formatted
[ ] Database method to check if input facts is well formatted
[x] Database method to update schema (create a dict with {schema_name: cardinality})
[ ] Database method to update update current_facts
    [ ] if name doesn't exist in current_facts instantialize Entity and add it to the dict
    [ ] call Entity method to update it's facts
[ ] Database method to print all current_facts (it calls all Entities method to print its facts)

[x] create Entity class
    [x] name (str) param
    [x] attributes_cardinality (dict) param
    [x] attributes ({})
[ ] Entity method to update facts
    [ ] Decide if add, reassing or delete
        [ ] Entity method to add fact
        [ ] Entity method to reassing fact
        [ ] Entity method to delete fact
[ ] Entity method to print its facts


current_facts = {name: entity}
schema_cardinality = {att_name: one|many}
entity -> name, attributes_cardinality, attributes