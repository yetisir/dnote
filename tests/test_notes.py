from cnote import notes

import conftest


def test_initialization_1(user, host, datetime_now):
    test_input = notes.Note('This is a sample note!      ')

    test_output_name = f'{conftest.TEST_USER}-note-589fc654'
    test_output_body = 'This is a sample note!'
    test_output_timestamp = int(conftest.TEST_TIMESTAMP.timestamp())
    test_output_host = conftest.TEST_HOST
    test_output_tags = []
    test_output_id = '589fc654334242778b7f82fd97f88435'

    assert test_input.name == test_output_name
    assert test_input.body == test_output_body
    assert test_input.timestamp == test_output_timestamp
    assert test_input.host == test_output_host
    assert set(test_input.tags) == set(test_output_tags)
    assert test_input.id == test_output_id


def test_initialization_2(user, host, datetime_now):
    test_input = notes.Note(
        'This is a sample note!\t\n',
        name='Custom note name\t\n',
        tags=[
            'custom tag 1\t\n',
            'custom tag 2\t\n',
        ])

    test_output_name = 'Custom note name'
    test_output_body = 'This is a sample note!'
    test_output_timestamp = int(conftest.TEST_TIMESTAMP.timestamp())
    test_output_host = conftest.TEST_HOST
    test_output_id = '1a7b5dcf737ca2db439eafe13449890f'
    test_output_tags = [
        'custom tag 1',
        'custom tag 2',
    ]

    assert test_input.name == test_output_name
    assert test_input.body == test_output_body
    assert test_input.timestamp == test_output_timestamp
    assert test_input.host == test_output_host
    assert set(test_input.tags) == set(test_output_tags)
    assert test_input.id == test_output_id


def test_initialization_3(user, host, datetime_now):
    test_input = {
        'body': 'This is a sample note!',
        'name': 'Custom note name',
        'tags': [
            'custom tag 1',
            'custom tag 2',
        ],
        'host': 'testhost',
        'timestamp': 1608915955,
        'id': '1b35b9f893cedb677d5429b5b0f4bf2b'
    }

    test_output_name = 'Custom note name'
    test_output_body = 'This is a sample note!'
    test_output_timestamp = 1608915955
    test_output_host = 'testhost'
    test_output_id = '1b35b9f893cedb677d5429b5b0f4bf2b'
    test_output_tags = [
        'custom tag 1',
        'custom tag 2',
    ]

    note = notes.Note.from_dict(test_input)

    assert note.name == test_output_name
    assert note.body == test_output_body
    assert note.timestamp == test_output_timestamp
    assert note.host == test_output_host
    assert set(note.tags) == set(test_output_tags)
    assert note.id == test_output_id


def test_tokens(user, host, datetime_now):
    test_input = notes.Note(
        'This is a sample note!\t\n',
        name='Custom note name\t\n',
        tags=[
            'custom tag 1\t\n',
            'custom tag 2\t\n',
        ])

    test_output = {
        'body': {
            '0cc175b9c0f1b6a831c399e269772661': 'a',
            'a2a551a6458a8de22446cc76d639a9e9': 'is',
            '86260f27f78d5a8a6412c2a99c9d5c89': 'sampl',
            '9033e0e305f247c0c3c80d0c7848c8b3': '!',
            'd529e941509eb9e9b9cfaeae1fe7ca23': 'not',
            'd9aebf7d5a83db9709fe0af7b92ab73a': 'thi',
        },
        'host': {
            '67b3dba8bc6778101892eb77249db32e': 'host',
        },
        'name': {
            '8b9035807842a4e4dbe009f3f1478127': 'custom',
            'd529e941509eb9e9b9cfaeae1fe7ca23': 'not',
            '22c78aadb8d25a53ca407fae265a7154': 'nam',
        },
        'tags': {
            '8b9035807842a4e4dbe009f3f1478127': 'custom',
            'c4ca4238a0b923820dcc509a6f75849b': '1',
            'c81e728d9d4c2f636f067f89cc14862c': '2',
            'e4d23e841d8e8804190027bce3180fa5': 'tag',
        },
    }

    assert test_input.tokens == test_output


def test_serialization(user, host, datetime_now):
    test_input = notes.Note(
        'This is a sample note!\t\n',
        name='Custom note name\t\n',
        tags=[
            'custom tag 1\t\n',
            'custom tag 2\t\n',
        ])

    test_output = {
        'body': 'This is a sample note!',
        'name': 'Custom note name',
        'tags': [
            'custom tag 1',
            'custom tag 2',
        ],
        'host': conftest.TEST_HOST,
        'timestamp': int(conftest.TEST_TIMESTAMP.timestamp()),
        'id': '1a7b5dcf737ca2db439eafe13449890f'
    }

    assert test_input.to_dict() == test_output


def test_show(user, host, datetime_now, capfd):
    test_input = notes.Note(
        'This is a sample note!\t\n',
        name='Custom note name\t\n',
        tags=[
            'custom tag 1\t\n',
            'custom tag 2\t\n',
        ])

    test_input.show()

    stdout = capfd.readouterr()[0]
    stdout_lines = stdout.split('\n')

    assert test_input.host in stdout_lines[0]
    assert test_input.id in stdout_lines[0]
    assert test_input.name in stdout_lines[0]


def note_collection_initialization(user, host, datetime_now):
    collection = notes.NoteCollection()
    return collection
