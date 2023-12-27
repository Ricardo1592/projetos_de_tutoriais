from src.interfaces.iobserver import IObserver


class Alarm:

    def __init__(self):
        self.beep = False
        self.subscribers: list[IObserver] = []

    def add_pessoa(self, subscriber: IObserver):
        self.subscribers.append(subscriber)

    def alarm_state(self):
        return self.beep

    def ring(self):
        self.beep = True
        for subscriber in self.subscribers:
            subscriber.update()





