import os

endpoints_path = os.path.abspath("impl-endpoints")

class Impl:

    def __init__(self, _name, roles):
        self._roles = _roles
        self._name = _name

    def name(self):
        return self._name

    def dir(self):
        return os.path.join(endpoints_path, self._name)

IMPLEMENTATIONS = [
    Impl("cloudflare-go", roles=["client"]),
    Impl("boringssl")
rustls = Impl("rustls")

CLIENTS = [

    cfgo,
]

SERVERS = [
    boringssl,
    rustls,
]
