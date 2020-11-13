from typing import Union

# FactList = list[Union[str, bool]]
# FactTuple = tuple[Union[str, bool]]
# facts: Union[FactList, FactTuple], schema: Union[list[str], tuple[str]]


class DataBase:
    def __init__(self, facts, schema, test=False):
        self.current_facts = {}
        self.attributes_cardinality = {}
        if not test:
            if self.check_schema(schema) and self.check_facts(facts):
                self.update_schema(schema)
                self.update_facts(facts)

    def check_schema(self, schema: Union[list, tuple]) -> bool:
        def is_list_or_tuple(list_or_tuple):
            return type(schema) == list or type(schema) == tuple

        if not is_list_or_tuple(schema) or not is_list_or_tuple(schema[0]):
            print("Bad schema")
            return False

        else:
            # needs improvement. catch AattributeError
            len_status = all([len(attribute) == 3 for attribute in schema])
            one_or_many = all([attribute[2].lower() == "one" or attribute[2].lower(
            ) == "many" for attribute in schema])
            string_status = all([type(item) == str
                                 for attribute in schema for item in attribute])

        return all((len_status, one_or_many, string_status))

    def update_schema(self, schema):
        self.attribute_cardinality = {
            attribute[0].lower(): attribute[-1].lower() for attribute in schema}

    def check_facts(self, facts):
        return True

    def update_facts(self, facts):
        for fact in facts:
            name = fact[0]
            if self.current_facts.get(name, False) == False:
                self.current_facts[name] = Entity(
                    name, self.attributes_cardinality)
                    
            self.current_facts[name].manage_attribute(fact[1:])


class Entity:
    def __init__(self, name, attributes_cardinality):
        self.name = name
        self.attributes_cardinality = attributes_cardinality
        self.attributes = {}  # name: value OU name: [value1, value2]

    def manage_attribute(self, attribute):
        attribute_name = attribute[0]
        attribute_value = attribute[1]
        add = attribute[2]

        if add:
            self.add_attribute(
                attribute_name, attribute_value)
        else:
            self.remove_attribute(attribute_name, attribute_value)

    def add_attribute(self, att_name, value):
        if self._names_cardinality[att_name] == "many":
            try:
                self.attributes[att_name].append(value)
            except AttributeError:
                self.attributes[att_name] = [value]
            finally:
                return

        self.attributes[att_name] = value

    def remove_attribute(self, att_name, value):
        cardinality = self.attribute_cardinality[att_name]
        if cardinality == "many":
            try:
                self.attributes[att_name].remove(value)
            except ValueError:
                print("Não há um fato com esse valor")
                return

        if (cardinality == "one" and self.attributes[att_name] = value) or self.attributes[att_name] == [] 
            del self.attributes[att_name]