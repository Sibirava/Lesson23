class Transport:

    def __init__(self, tank=0):
        self._tank = tank

    def __str__(self):
        return f"tank = {self._tank}"

    @property
    def tank(self):
        return self._tank

    @tank.setter
    def tank(self, tank):
        if tank > 0:
            self._tank = tank