import collections


class SimpleDb(object):
    def __init__(self):
        """ An LRU that caches transactions already commited """
        self.entries = collections.OrderedDict()
        self.num_entries_to_cached_value = {}
        self.pre_entries = []  # Stores previous values to allow rollback

    def assign(self, key, value):
        """ Sets value of key to value. Inserts key into database if it doesn't already exist. """
        current_value = self.get(key)
        if current_value == value:
            return
        self.__update_num_equal_to(current_value, value)
        self.__update_current_transaction(key, current_value)
        self.entries[key] = value

    def __update_num_equal_to(self, current_value, new_value=None):
        """
        Decrements by one the number items present with current_value (if current_value
        is not equal to None) and increments by one the number present with new_value
        (if new_value is not equal to None).
        """
        for amount_to_add, value in [(-1, current_value), (1, new_value)]:
            if value is not None:
                self.num_entries_to_cached_value.setdefault(value, 0)
                self.num_entries_to_cached_value[value] += amount_to_add

    def __update_current_transaction(self, key, value):
        """
        Stores current value of key if not already stored to most recent transaction
        (if any transactions open) to enable restoration of previous state on rollback.
        """
        if self.pre_entries and key not in self.pre_entries[-1]:
            self.pre_entries[-1][key] = value


    def get(self, key):
        """ Returns value of key if it exists in the database, otherwise returns None. """
        return self.entries[key] if key in self.entries else None

    def get_num_equal_to(self, value):
        """ Returns number of entries in the database that have the specified value. """
        return self.num_entries_to_cached_value[value] if value in self.num_entries_to_cached_value else 0

    def unset(self, key):
        """ Removes key from database if it's present. """
        current_value = self.entries.pop(key, None)
        if current_value is None:
            return
        self.__update_num_equal_to(current_value)
        self.__update_current_transaction(key, current_value)

    def begin(self):
        """ Opens transaction block. """
        self.pre_entries += [{}]

    def rollback(self):
        """
        Reverts database to its state before most current transaction.
        Returns True on success, returns False if there aren't any open transactions.
        """
        if not self.pre_entries:
            return False
        for key, value in self.pre_entries.pop().items():
            current_value = self.get(key)
            if current_value == value:
                continue
            self.__update_num_equal_to(current_value, value)
            if value is None:
                del self.entries[key]
            else:
                self.entries[key] = value
        return True

    def commit(self):
        """
        Commits all transactions to database. Returns True on success,
        returns False if there aren't any open transactions.
        """
        if not self.pre_entries:
            return False
        self.pre_entries = []
        return True



def display(value, default=None):
    """
    Prints value to stdout. If value is None and a default value is
    specified (and not None), then the default value is printed instead. Otherwise
    the None value is printed.
    """
    if value is None and default is not None:
        value = default
    print(value)


OPS = {
        'GET':        (2, lambda db, key:  display(db.get(key), "NULL")),
        'NUMEQUALTO': (2, lambda db, value: display(db.get_num_equal_to(value))),
        'UNSET':      (2, lambda db, key:  db.unset(key)),
        'BEGIN':      (1, lambda db:        db.begin()),
        'ROLLBACK':   (1, lambda db:        db.rollback() or display("NO TRANSACTION")),
        'COMMIT':     (1, lambda db:        db.commit() or display("NO TRANSACTION")),
        'END':        (1, lambda db:        False),
        'SET':        (3, lambda db, key, value: db.assign(key, value)),
}


def process_command(simpleDb, command):
    """
    Parses string commands and applies them to the database.
    Returning False indicates that no more commands should be passed in.
    """
    command = command.split()
    opcode = command.pop(0).upper() if len(command) > 0 else None
    if opcode is None or opcode not in OPS or len(command) != (OPS[opcode][0] - 1):
        print("INVALID COMMAND")
    elif 'END' == opcode:
        return False
    else:
        OPS[opcode][1](simpleDb, *command)
    return True


def run():
    """ Reads database command from the command line and passes it through for processing. """
    # BEGIN \n SET a 30 \n BEGIN \n SET a 40 \n COMMIT \n GET a \n ROLLBACK \n END
    simpleDb = SimpleDb()
    while process_command(simpleDb, input()):
        pass

run()
