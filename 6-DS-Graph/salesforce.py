from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.deps = defaultdict(set)     # Dependancy list {A --> Dependant upon [B, C]}
        self.revDeps = defaultdict(set)  # Resolving list  {B --> Resolves [A]}
        self.numDeps = defaultdict(int)  # in-degree of a component, Number of dependancies for a component

    # Directed graph
    def add_edge(self, src, dest):
        # Where dest depends on src
        self.deps[dest].add(src)
        self.revDeps[src].add(dest)

        # Increase dependency (In-Degree) of dest component
        self.numDeps[dest] += 1


class Solution:
    def __init__(self):
        self.graph = Graph()
        self.installed = set()  # {InstalledComponent: outdegree}
        self.recStack = set()   # To prevent circular dependancy!!!

        """
        Bind text commands to functions to be called for the command
        {Command --> Function to be called for command}
        """
        self.Commands = {
            'DEPEND' : lambda arr: self.depends(arr),
            'INSTALL': lambda c: self.install(c),
            'REMOVE' : lambda c: self.remove(c),
            'LIST'   : lambda: self.list(),
            'END'    : lambda: False,
            'CANFINISH': lambda numCourses: self.canFinish(numCourses),

        }

    """
    Build graph
    process: "DEPEND TELNET TCPIP NETCARD"
    """
    def depends(self, arr):
        component = arr[0]
        requires = arr[1:]

        [self.graph.add_edge(component, req) for req in requires]

    """
    # Topological Sort - DFS - to resolve dependencies
    """
    def install(self, dest):
        print("Installing {0}".format(dest))
        # edge cases
        if dest in self.installed:
            print("Already installed")
            return True

        # Cycle??  A dependant on B and B dependant on A.... Then We can't install ANY
        self.recStack.add(dest)

        # 1st Install all dependencies for this component
        for dep in self.graph.deps[dest]:
            if dep in self.recStack:  # A --> B ---> A
                print("Circular Dependancy!!!! Beware of unlimited recurssion!!")
                return False

            if dep not in self.installed:
                self.install(dep)

        self.recStack.remove(dest)
        # All dependencies installed.
        # TRICK: PostOrder Visit: Install this component now AFTER installing all deps
        self.installed.add(dest)
        print(("Installed: {0}".format(dest)))

        """
        As part of installing this component, all other dependant components can now be installed
        so, Reduce in-degree of all components there were dependent on now installed components
        """
        for dependant in self.graph.revDeps[dest]:
            self.graph.numDeps[dependant] -= 1

    def remove(self, dest):
        """
        Go through Rev Dep Graph, if any of the deps Are present in installedMap - Cannot Install.
        Or else go ahead remove it
        """
        print(("Removing {0}".format(dest)))
        # edge case
        if dest not in self.installed:
            print(("{0} is not installed".format(dest)))
            return False

        # Check if any component is dependant on this component so it'll be affected
        if len(self.graph.revDeps[dest]) > 0:
            print(("{0} is still needed".format(dest)))
            return False

        # No one is dependant on this component, go ahead and remove
        self.installed.remove(dest)
        print(("{0} removed".format(dest)))
        for dependant in self.graph.revDeps[dest]:
            self.graph.deps[dependant].add(dest)
        return True

    def list(self):
        for item in self.installed:
            print(item)

    def query(self, input):
        input = input.split()

        # validations
        if len(input) <= 0:
            print("empty!")
            return False

        inputcode = input.pop(0).upper()
        if inputcode not in self.Commands:
            print("Please see Commands for valid commands")
        elif inputcode == 'END':
            return False
        else:
            argsList = input[0:]
            print(("Processing command {0} with args {1}".format(inputcode, argsList)))

            if inputcode.upper() == 'DEPEND':
                self.Commands[inputcode](argsList)
            elif inputcode.upper() == 'LIST':
                self.Commands[inputcode]()
            else:
                self.Commands[inputcode](argsList[0])

        return True

    def canFinish(self, n):
        self.installed = set()
        # Try to finish each course available
        for c in list(self.graph.deps.keys()):
            if self.install(c) == False:
                break

        # Finished courses will be part of 'installed' set
        totalFinishedCourses = len(self.installed)
        if n >= totalFinishedCourses:
            print(("True: {0} courses can be finished. Installed: {1}".format(n, self.installed)))
        else:
            print(("False: {0} courses can not be finished. Installed: {1}".format(n, self.installed)))


"""
UNIT TESTS
"""
def unittests():
    s = Solution()

    s.depends(['TELNET', 'TCPIP', 'NETCARD'])
    s.depends(['TCPIP', 'NETCARD'])
    s.depends(['DNS', 'TCPIP', 'NETCARD'])
    s.depends(['BROWSER', 'TCPIP', 'HTML'])
    s.install('TELNET')
    s.remove('TELNET')
    s.install('TELNET')
    s.remove('NETCARD')
    s.remove('TCPIP')
    s.list()


"""
MAKING IT COMPATIBLE TO HACKERRANK INPUTS IN STDIN
"""
def main():
    s = Solution()
    s.query("DEPEND TELNET TCPIP NETCARD")
    s.query("DEPEND TCPIP NETCARD")
    s.query("DEPEND DNS TCPIP NETCARD")
    s.query("DEPEND BROWSER TCPIP HTML")
    s.query("LIST")
    s.query("INSTALL TELNET")
    s.query("LIST")
    s.query("INSTALL NETCARD")
    s.query("INSTALL DNS")
    s.query("REMOVE TELNET")
    s.query("LIST")

    sCourses1 = Solution()
    sCourses1.query("DEPEND 1 0")
    sCourses1.query("CANFINISH 2")

    sCourses2 = Solution()
    sCourses2.query("DEPEND 1 0")
    sCourses2.query("DEPEND 0 1")
    sCourses2.query("CANFINISH 2")



if __name__ == "__main__":
    main()