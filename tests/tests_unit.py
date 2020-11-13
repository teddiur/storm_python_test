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


def test_update_schema():
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


def test_init_facts():
    facts = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua alice, 10', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '234-5678', True),
        ('joão', 'telefone', '91234-5555', True),
        ('joão', 'telefone', '234-5678', False),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True),
    ]
    expected_result = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '91234-5555', True),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True)
    ]
