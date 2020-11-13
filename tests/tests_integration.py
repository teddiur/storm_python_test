from app import DataBase, DataBaseViewer

def test_update_facts():
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
    schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
    ]
    expected_result = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '91234-5555', True),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True)
    ]

    TestDataBase = DataBase(schema, facts, test=True)
    TestDataBase.update_schema(schema)
    TestDataBase.update_facts(facts)
    Viewer = DataBaseViewer(TestDataBase)
    Viewer.show_current_facts()
    assert TestDataBase.check_facts(schema, facts) == True
