from app import DataBase


def test_schema_small_true():
    schema = [['GONNA', 'JUST one schema', 'one']]
    assert DataBase(None, None, test=True).check_schema(schema) == True

def test_schema_big_true():
    schema = [['EVEN', 'IF', 'ONE'], ['OF STRINGS', 'ARE RIDICULOUS LARGE', 'MaNY'], ['GONNA', 'pass the test', 'one']]
    assert DataBase(None, None, test=True).check_schema(schema) == True

def test_schema_onemany_false():
    schema = [['GONNA', 'JUST one schema', 'one', 'hehe']]
    assert DataBase(None, None, test=True).check_schema(schema) == False

def test_schema_number_false():
    schema = [['EVEN', 'IF', 'ONE'], ['OF STRINGS', 1, 'erp'], ['GONNA', 'pass the test', 'one']]
    assert DataBase(None, None, test=True).check_schema(schema) == False

def test_schema_lenght_false():
    schema = [['EVEN', 'IF', 'ONE'], ['yeah'] ['OF STRINGS', 'hehe', 'many'], ['GONNA', 'pass the test', 'one']]
    assert DataBase(None, None, test=True).check_schema(schema) == False

def test_update_schema_true():
    schemas = [[['endereço', 'JUST one schema', 'oNe']],
               [['endereço', 'cardinality', 'one'], [
                   'telefone', 'and i\'ll', 'manY']],
               [['rua', 'IF', 'ONE'], ['casas', 'ARE RIDICULOUS LARGE', 'MANY'], ['nome', 'pass the test', 'one']]]
    expected_result = [{'endereço': 'one1'}, {'endereço': 'one', 'telefone': 'many'}, {
        'rua': 'one', 'casas': 'many', 'nome': 'one'}]

    for i, schema in enumerate(schemas):
        # Dict comparission doesn't work well if dicts are different
        result = DataBase(None, None, test=True).update_schema(
            schema) == expected_result[i]
        assert result == True



