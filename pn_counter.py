class PNCounter:
    def __init__(self, replica_id):
        self.replica_id = replica_id
        self.increments = {replica_id: 0}
        self.decrements = {replica_id: 0}

    def increment(self, n=1):
        self.increments[self.replica_id] += n

    def decrement(self, n=1):
        self.decrements[self.replica_id] += n

    def value(self):
        return sum(self.increments.values()) - sum(self.decrements.values())

    def merge(self, other):
        for k, v in other.increments.items():
            self.increments[k] = max(self.increments.get(k, 0), v)
        for k, v in other.decrements.items():
            self.decrements[k] = max(self.decrements.get(k, 0), v)
