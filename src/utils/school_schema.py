from schema import Schema, Or, And


class Schemalist:
    INFO = Schema({
        'name': str,
        'gender': int,
        'grade': int,
        'phone_number': Or(str, int),
    })
