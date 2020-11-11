from main import DataBase


def check_schema_true():
    schemas_true = [[['GONNA', 'JUST one schema', 'one']], [['hey', 'this is', 'one'], ['a test', 'and i\'ll', 'manY']], [
        ['EVEN', 'IF', 'ONE'], ['OF STRINGS', 'ARE RIDICULOUS LARGE', 'MANY'], ['GONNA', 'pass the test', 'one']]]
    for schema in schemas_true:
        assert DataBase(None, None, test=True).check_schema(schema) == True


def check_schema_false():
    pass


# test1 = DataBase([1, 2, 3, 4], [('ok', 'yeah', 'thats my shit', 3), ('ops')])
check_schema_true()
