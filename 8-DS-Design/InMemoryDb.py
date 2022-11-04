import collections


class Boxmydb(object):
    """ In Memory mydb. Main cache (commit all by-default) + Prev txns in progress (used by rollback) """
    def __init__(self):
        """ An LRU that caches transactions already commited (used for COMMIT) """
        self.entries = collections.OrderedDict()
        """ An LRU that caches ongoing transactions (used for ROLLBACK)) """
        self.prev_transactions = []
        self.housekeeping = collections.OrderedDict()

    """
    Commit: By default we commit to mydb!
            Clear all txns till prev BEGIN block (no more rollback)
    """
    def commit(self):
        if not self.prev_transactions:
            return False
        self.prev_transactions = []
        return True

    """Everything latest is in mydb, just get it"""
    def get(self, key):
        if key in self.entries:
            return self.entries[key]
        else:
            return None

    """
    Transaction Begins
    Create a list of dict for each transaction to store prev_transactions
    """
    def begin(self):
        self.prev_transactions += [collections.OrderedDict()]

    """
    Set value in mydb +
    Save value history in prev_transactions to be replaced in case rollback
    """
    def setting(self, key, new_value=None):
        value_in_mydb = self.get(key)
        self.update_prev_transactions(key, value_in_mydb)
        self.update_housekeeping(value_in_mydb, new_value)
        self.entries[key] = new_value

    def update_prev_transactions(self, key, value):
        """
        Stores all prior values that were in mydb
        They can be used to rollback
        """
        if self.prev_transactions and key not in self.prev_transactions[-1]:
            self.prev_transactions[-1][key] = value

    """ Just to maintain Commit log
        Value 1 would be current in mydb,
        All others would be prior values
    """
    def update_housekeeping(self, value_in_mydb, new_value=None):
        try:
            self.housekeeping[value_in_mydb] -= 1
        except KeyError:
            self.housekeeping.setdefault(value_in_mydb, 0)
            self.housekeeping[value_in_mydb] -= 1

        try:
            self.housekeeping[new_value] += 1
        except KeyError:
            self.housekeeping.setdefault(new_value, 0)
            self.housekeeping[new_value] += 1

    """
    Rollback: Get last txn block's values and set in mydb! Purge last txn then!
    """
    def rollback(self):
        if not self.prev_transactions:
            return False

        # purge last txn
        last_txn = self.prev_transactions.pop()
        # Get all values from last txn block and overwrite in mydb
        for last_key, last_value in last_txn.items():
            value_in_mydb = self.get(last_key)
            """
            if value_in_mydb == last_value:
                continue
            """
            self.update_housekeeping(value_in_mydb, last_value)
            if last_value is None:
                del self.entries[last_key]
            else:
                self.entries[last_key] = last_value
        return True


def output(value, default=None):
    """
    Prints value to stdout. If value is None and a default value is
    specified (and not None), then the default value is printed instead. Otherwise
    the None value is printed.
    """
    if value is None and default is not None:
        value = default
    print(value)


"""
argparser.args (Commad)
"""

""" Format
COMMAND:      ArgsNo,   Call relevent fun
"""
Commands = {
        'GET':        (2, lambda mydb, key:  output(mydb.get(key), "NULL")),
        'SET':        (3, lambda mydb, key, value: mydb.setting(key, value)),
        'BEGIN':      (1, lambda mydb:        mydb.begin()),
        'ROLLBACK':   (1, lambda mydb:        mydb.rollback() or output("NO MORE TRANSACTION")),
        'COMMIT':     (1, lambda mydb:        mydb.commit() or output("NO MORE TRANSACTION")),
        'END':        (1, lambda mydb:        False),
}


def query(mydb, input):
    input = input.split()

    # validations
    if len(input) <= 0:
        print("empty!")
        return False

    inputcode = input.pop(0).upper()
    if inputcode not in Commands:
        print("Please see Commands for valid commands")
    elif inputcode == 'END':
        return False
    else:
        Commands[inputcode][1](mydb, *input)
    return True


def main():
    mydb = Boxmydb()
    while True:
        query(mydb, input())

if __name__ == "__main__":
    main()

"""
def run():
    while query(raw_input()):
        pass

run()
"""
