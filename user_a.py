from pn_counter import PNCounter

a = PNCounter("A")
a.increment(3)
a.decrement(1)
print(f"User A's counter: {a.value()}")
