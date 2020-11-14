from .data import facts, schema
from typing import Tuple, List, Dict, Union, Type


def is_list_or_tuple(inspected):
    return type(inspected) == list or type(inspected) == tuple


Fact = Union[List[Union[str, bool]], Tuple[Union[str, bool]]]
Facts = List[Fact]
Schema = List[List[str]]


class Entity:
    def __init__(self, name: str, cardinality: Dict[str, str]) -> None:
        self.name = name
        self.cardinality = cardinality
        self.attributes = {}  # name: value OU name: [value1, value2]

    def manage_fact(self, attribute: List[Union[str, bool]]) -> None:
        attribute_name = attribute[0]
        attribute_value = attribute[1]
        add = attribute[2]
        if add:
            self._add_fact(attribute_name, attribute_value)
        else:
            self._remove_fact(attribute_name, attribute_value)

    def _add_fact(self, att_name: str, value: str) -> None:
        if self.cardinality[att_name] == "many":
            try:
                self.attributes[att_name].append(value)
            except KeyError:
                self.attributes[att_name] = [value]
            finally:
                return

        self.attributes[att_name] = value

    def _remove_fact(self, att_name: str, value: str) -> None:
        cardinality = self.cardinality[att_name]
        if cardinality == "many":
            try:
                self.attributes[att_name].remove(value)
            except ValueError:
                print("There's no fact with this value")
                return

        if (cardinality == "one" and self.attributes[att_name] == value) or self.attributes[att_name] == []:
            del self.attributes[att_name]

    def get_facts(self) -> List[Tuple[str]]:
        facts = []
        for att_name in self.attributes.keys():
            facts.extend(self._get_fact(att_name))
        return facts

    def _get_fact(self, att_name: str) -> List[Tuple[str]]:
        facts = []
        if is_list_or_tuple(self.attributes[att_name]):
            for value in self.attributes[att_name]:
                facts.append((self.name, att_name, value, True))
        else:
            facts.append(
                (self.name, att_name, self.attributes[att_name], True))
        return facts


class DataBase:
    def __init__(self, schema: Schema, facts: Facts, test=False) -> None:
        self._entities = {}
        self._cardinality = {}
        if test:
            return
        if self.check_schema(schema):
            self.update_schema(schema)
            self.update_facts(facts)

    def get_entities(self) -> List[Type[Entity]]:
        return self._entities.values()

    def get_entities_dict(self) -> Dict[str, Type[Entity]]:
        return self._entities

    def get_cardinality(self) -> Dict[str, str]:
        return self._cardinality

    def _set_fact(self, entity_name: str, params: Fact) -> None:
        current_facts = self.get_entities_dict()
        cardinality = self.get_cardinality()
        if current_facts.get(entity_name, False) == False:
            self._entities[entity_name] = Entity(
                entity_name, cardinality)
        self._entities[entity_name].manage_fact(params)

    def _set_cardinality(self, attribute_name: str, value: str) -> None:
        self._cardinality[attribute_name] = value

    def check_schema(self, schema: Schema) -> bool:
        try:
            if not is_list_or_tuple(schema) or not all([is_list_or_tuple(schema_item) for schema_item in schema]):
                print("Bad schema, it should be a list/tuple of list/tuple")
                return False

            else:
                # needs improvement. catch AattributeError
                len_status = all([len(attribute) == 3 for attribute in schema])
                one_or_many = all([attribute[2].lower() == "one" or attribute[2].lower(
                ) == "many" for attribute in schema])
                string_status = all([type(item) == str
                                     for attribute in schema for item in attribute])
        except IndexError:
            print("Bad schema, your cardinality specification is too short")
            return False

        return all((len_status, one_or_many, string_status))

    def update_schema(self, schema: Schema) -> None:
        [self._set_cardinality(attribute[0].lower(),
                               attribute[-1].lower()) for attribute in schema]

    def check_facts(self, schema: Schema, facts: Facts) -> bool:
        entity_check, attribute_check, value_check, add_check, len_check = [], [], [], [], []
        for fact in facts:
            try:
                entity = fact[0]
                att_name = fact[1]
                value = fact[2]
                add = fact[3]

                entity_check.append(type(entity) == str)
                attribute_check.append(att_name in schema)
                value_check.append(not is_list_or_tuple(value))
                add_check.append(type(add) == bool)
                len_check.append(len(fact) == 4)

            except IndexError:
                print("Bad facts list")
                return false

        all_checks = [entity_check, attribute_check,
                      value_check, add_check, len_check]
        return all(all_checks)

    def update_facts(self, facts: Facts) -> None:
        schema = self.get_cardinality().keys()
        if self.check_facts(schema, facts):
            for fact in facts:
                name = fact[0]
                params = fact[1:]
                self._set_fact(name, params)


class DataBaseViewer:
    def __init__(self, YourDataBase: Type[DataBase]) -> None:
        self.database = YourDataBase

    def show_current_facts(self) -> None:
        entities = self.database.get_entities()
        facts = []
        [facts.extend(entity.get_facts()) for entity in entities]

        self.prettify(facts)

    def prettify(self, facts: List[Tuple[str]]) -> None:
        print('[')
        for i, fact in enumerate(facts):
            print(f'    {fact}', end='')
            if i != len(facts)-1:
                print(',')
        print('\n]')


YourDataBase = DataBase(schema, facts)
YourDataBaseViewer = DataBaseViewer(YourDataBase)
YourDataBaseViewer.show_current_facts()
