from typing import Union

# FactList = list[Union[str, bool]]
# FactTuple = tuple[Union[str, bool]]
# facts: Union[FactList, FactTuple], schema: Union[list[str], tuple[str]]
def is_list_or_tuple(inspected):
    return type(inspected) == list or type(inspected) == tuple

class DataBase:
    def __init__(self, facts, schema, test=False):
        self.current_facts = {}
        self.attributes_cardinality = {}
        if not test:
            if self.check_schema(schema) and self.check_facts(schema, facts):
                self.update_schema(schema)
                self.update_facts(facts)

    def check_schema(self, schemas: Union[list, tuple]) -> bool:
        try:
            if not is_list_or_tuple(schemas) or not all([is_list_or_tuple(schema) for schema in schemas]):
                print("Bad schemas, it should be a list/tuple of list/tuple")
                return False

            else:
                # needs improvement. catch AattributeError
                len_status = all([len(attribute) == 3 for attribute in schemas])
                one_or_many = all([attribute[2].lower() == "one" or attribute[2].lower(
                ) == "many" for attribute in schemas])
                string_status = all([type(item) == str
                                    for attribute in schemas for item in attribute])
        except IndexError:
            print("Bad schema, your cardinality specification is too short")
            return False

        return all((len_status, one_or_many, string_status))

    def update_schema(self, schema):
        self.attributes_cardinality = {
            attribute[0].lower(): attribute[-1].lower() for attribute in schema}

    def check_facts(self, schema, facts):
        entity_check, attribute_check, value_check, add_check, len_check = [], [], [], [], []
        attributes = [att[0] for att in schema]
        for fact in facts:
            try:
                entity = fact[0]
                att_name = fact[1]
                value = fact[2]
                add = fact[3]
                
                entity_check.append(type(entity) == str)
                attribute_check.append(att_name in attributes)
                value_check.append(not is_list_or_tuple(value))
                add_check.append(type(add) == bool)
                len_check.append(len(fact) == 4)
            
            except IndexError:
                print("Bad facts list")
                return false

        all_checks = [entity_check, attribute_check, value_check, add_check, len_check]
        return all(all_checks)

    def update_facts(self, facts):
        for fact in facts:
            name = fact[0]
            params = fact[1:]
            if self.current_facts.get(name, False) == False:
                self.current_facts[name] = Entity(
                    name, self.attributes_cardinality)
            self.current_facts[name].manage_attribute(params)

    def show_facts(self):
        facts = []
        for entity in self.current_facts.values():
            facts.extend(entity.get_attributes())
        self.prettify(facts)
    
    def prettify(self, facts):
        print('[')
        for i, fact in enumerate(facts):
            print(f'    {fact}', end='')
            if i != len(facts)-1:
                print(',')
        print('\n]')

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
        if self.attributes_cardinality[att_name] == "many":
            try:
                self.attributes[att_name].append(value)
            except KeyError:
                self.attributes[att_name] = [value]
            finally:
                return

        self.attributes[att_name] = value


    def remove_attribute(self, att_name, value):
        cardinality = self.attributes_cardinality[att_name]
        if cardinality == "many":
            try:
                self.attributes[att_name].remove(value)
            except ValueError:
                print("There's no fact with this value")
                return

        if (cardinality == "one" and self.attributes[att_name] == value) or self.attributes[att_name] == []:
            del self.attributes[att_name]
    
    def get_attributes(self):
        facts = []
        for att_name in self.attributes.keys():
            facts.extend(self.get_attribute(att_name))
        return facts
    
    def get_attribute(self, att_name):
        facts = []
        if is_list_or_tuple(self.attributes[att_name]):
            for value in self.attributes[att_name]:
                facts.append((self.name, att_name, value, True))
        else:
            facts.append((self.name, att_name, self.attributes[att_name], True))
        return facts