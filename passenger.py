from place import Place

class Passager:
    def __init__(self, address, tuman, mahalla) -> None:
        self._address = address
        self._tuman = tuman
        self._mahalla = mahalla

    def get_place(self):
        return f"{self._address}, {self._tuman}, {self._mahalla}"
    
