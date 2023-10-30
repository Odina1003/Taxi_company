class Place:
    def __init__(self, address, tuman, mahalla) -> None:
        self._address = address
        self._tuman = tuman
        self._mahalla = mahalla

    def to_string(self):
        return f'{self._address}, {self._tuman}, {self._mahalla}'
    