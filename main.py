from typing import Union

FactList = list[Union[str, bool]]
FactTuple = tuple[Union[str, bool]

class DataBase(object):
    def __init__(self, facts: Union[FactList, FactTuple], schema: Union[list[str], tuple[str]]):
        self.facts= facts
        self.schema= schema
        self.check_schema()
        self.init_schema()
        self.check_facts()
        self.add_facts()

    def check_schema(self):

        pass
