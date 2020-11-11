from typing import Union

# FactList = list[Union[str, bool]]
# FactTuple = tuple[Union[str, bool]]
# facts: Union[FactList, FactTuple], schema: Union[list[str], tuple[str]]


class DataBase:
    def __init__(self, facts, schema, test=False):
        self.facts = facts
        self.schema = schema
        if not test:
            self.check_schema(schema)
            self.init_schema()
            self.check_facts()
            self.init_facts()

    def check_schema(self, schema: Union[list, tuple]) -> bool:
        def is_list_or_tuple(list_or_tuple):
            return type(schema) == list or type(schema) == tuple

        if not is_list_or_tuple(schema) or not is_list_or_tuple(schema[0]):
            print("Bad schema")
            return False

        else:
            # needs improvement
            len_status = all([len(attribute) == 3 for attribute in schema])
            one_or_many = all([attribute[2].lower() == "one" or attribute[2].lower(
            ) == "many" for attribute in schema])
            string_status = all([type(item) == str
                                 for attribute in schema for item in attribute])

        return all((len_status, one_or_many, string_status))
        # only_schema = schema[0]
        # len_status = len(only_schema)

        # type_schema = only_schema[2].lower()
        # one_or_many = type_schema == "one" or type_schema == "many"

        # string_status = all([type(item) for item in only_schema])

    def init_schema(self):
        pass

    def check_facts(self):
        pass

    def init_facts(self):
        pass
