"""
'Problem statement
https://coderpad.io/2NNNE94C

At Affirm, we have many forms of data ranging from raw external data (e.g. credit reports) to primitive values that are consumed by our ML models as features. They can also be an intermediate representation to derive other data or used in business rule evaluations (e.g. legal and compliance checks).

This creates a data dependency graph where there is a direct flow of data. Consider the following dependency graph:

user ID   merchant ID
\         /
\       /
\     /
\   /
\ /
how much the user spent at the
merchant within the last 7 days

More formally, we would need,
deterministic resolvers that declare a set of data they know how to resolve given a set of required data.
In code, this can look like the following:
"""
class AmountResolver(object):
    requires = ['user_id', 'merchant_id']
    resolves = ['user_loan_amount_at_some_merchant_7_days']

    @staticmethod
    def run(inputs):
        # do something
        pass

class DebtResolver(object):
    requires = ['user_id', 'user_loan_amount_at_some_merchant_7_days']  # Atleast-1,
    resolves = ['debt_to_income'] # Exactly ONE

    @staticmethod
    def run(inputs): # -> inputs is a dict{key = signalName -> string, Signalvalue =int}):
        # do something
        pass

"""
Let's say there is an engine that needs to schedule these resolvers and be able return values for requested data.
Concretely, you should implement the following pseudocode API in the language of your choice:
"""

class Engine(object):
        d = {}


        def register(self, resolver):
            # type: (Resolver) -> None
            """
            The register function takes a resolver class and performs any pre-computation
            necessary to use the resolver in the resolve function.
            """
            self.resolver = resolver


            d[resolver.resolves[0]] = resolver



            pass

        def resolve(self, signal_to_resolve, base_signals):
            # GEt resolver for signal_to_resolve
            # Figure out requires
            # type: (str, Dict[str, int]) -> int
            """
            Uses registered resolvers and base_signals to resolve one signal.
            """
            visited = {}

            if signal_to_resolve in d and signal_to_reolsve not in visited:

                visited[signal_to_resolve] = True

                resolver = d[signal_to_resolve]

                # Resolve recursively for all requirements
                self.resolveRecur(signal_to_resolve, visited)





        def resolveRecur(self, signal_to_resolve, visited):

            for requirement in d[signal_to_resolve]:

                # Break
                resolver = d[requirement]
                resolver.run(requirement)

                visited[requirement] = True
                resolveRecur(requirement)


"""
    Dict
    debt_to_income -> DebtResolver
    user_loan_amount_at_some_merchant_7_days -> AmoutResolver

    DS
    DAG (resolver as node itself)....

    Alternatve DS:
    dictionary:

    Key : signal
    value: resolver(signal) -->

    Node: ?
    Edge: ?

    Algorithm: (Target=signal_to_resolve, base_signal)
    DFS (dependancies) ... base_signal -> 1. 2. --> .... ( = target , return)
"""

    r = Resolver()
    e = Engine()
    e.register(r)
    e.resolve('debt_to_income', base_signals={'user_id': 182773, 'merchant_id': 2727282})
