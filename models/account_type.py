_account_types = {
    'ADMIN': 1,
    'NATIVE': 2,
    'NOVEL_UPDATES': 3,
    'GLOBAL_MOD': 4
}

class AccountTypeMeta(type):
    def __getattr__(cls, key):
        if key in _account_types:
            return _account_types[key]
        else:
            return None

class AccountType(object):
    __metaclass__ = AccountTypeMeta

    @static
    def name_of(id):
        for x in _account_types:
            if _account_types[x] == id:
                return x
        return None