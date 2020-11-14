# storm_python_test
Storm's Python test

## Description
> O objetivo desse desafio é escrever uma função que retorne quais são os fatos vigentes sobre essas entidades.
> Ou seja, quais são as informações que estão valendo no momento atual.
> A função deve receber `facts` (todos fatos conhecidos) e `schema` como argumentos.

## To-do list
* [x] create database class
    * [x] entities dict ({})
    * [x] cardinality dict ({})
* [x] Database method to check if schema is well formatted
* [x] Database method to check if input facts is well formatted
* [x] Database method to update schema (update cardinality dict with {schema_name: cardinality})
* [x] Database method to update update entities
    * [x] if name doesn't exist in entities instantialize Entity and add it to the dict
    * [x] call Entity method to update it's facts
* [x] Database method to print all entities' current facts (it calls all Entities method to print its facts)

* [x] create Entity class
    * [x] name (str) param
    * [x] cardinality (dict) param
    * [x] attributes ({})
* [x] Entity method to manage attribute
    * [x] Decide if add, reassing or delete
        * [x] Entity method to add attribute
        * [x] Entity method to reassing attribute
        * [x] Entity method to delete attribute
* [x] Entity method to print its attributes