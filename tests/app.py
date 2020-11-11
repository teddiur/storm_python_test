from typing import Union

# FactList = list[Union[str, bool]]
# FactTuple = tuple[Union[str, bool]]
# facts: Union[FactList, FactTuple], schema: Union[list[str], tuple[str]]


class DataBase:
    def __init__(self, facts, schema, test=False):
        self.facts = []
        self.schema = schema
        if not test:
            if self.check_schema(schema) and self.check_facts(facts):
                self.attributes_cardinality = self.init_schema()
                self.init_facts(facts)

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

    def init_schema(self, schema):
        attribute_cardinality = {
            attribute[0].lower(): attribute[-1].lower() for attribute in schema}
        return attribute_cardinality

    def check_facts(self):
        return True

    def init_facts(self, facts):
        pass


class Entity:
    def __init__(self, name, attribute, value, added):
        self.name = name
        self.attribute = attribute
        self.value = value
        self.added = added
