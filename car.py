from transport import Transport


class Car(Transport):
    def __str__(self):
        return f"Car: tank = {self._tank}"


c = Car()
print(c)