from src.interfaces.iobserver import IObserver


class Pessoa(IObserver):

    def __init__(self):
        super().__init__()
        self.awake = False

    def is_awake(self):
        return self.awake

    def update(self):
        print("updating...")
        self.awake = True
