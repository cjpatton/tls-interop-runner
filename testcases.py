import abc

class TestCase(abc.ABC):

    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def desc(self):
        pass

class TestCaseDelegatedCredentials(TestCase):

    def name(self):
        return "dc"

    def desc(self):
        return \
            "The client indicates support for delegated credentials and the " \
            "server signs the handshake with a delegated credential."

TESTCASES = [
    TestCaseDelegatedCredentials(),
]
