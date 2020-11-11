from app import DataBase


def test_schema_true():
    schemas_true = [[['GONNA', 'JUST one schema', 'one']], [['hey', 'this is', 'one'], ['a test', 'and i\'ll', 'manY']], [
        ['EVEN', 'IF', 'ONE'], ['OF STRINGS', 'ARE RIDICULOUS LARGE', 'MANY'], ['GONNA', 'pass the test', 'one']]]
    for schema in schemas_true:
        assert DataBase(None, None, test=True).check_schema(schema) == True


def test_schema_false():
    schemas_false = [[['GONNA', 'JUST one schema', 'one', 'hehe']], [['hey', 'this is', 'nope'], ['a test', 'and i\'ll', 'manY']], [
        ['EVEN', 'IF', 'ONE'], ['OF STRINGS', 1, 'erp'], ['GONNA', 'pass the test', 'one']]]
    for schema in schemas_false:
        assert DataBase(None, None, test=True).check_schema(schema) == False
