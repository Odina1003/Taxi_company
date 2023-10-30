from place import Place
from passenger import Passager
class Trip:
    def __init__(self) -> None:
        self._places: list[Place]
        self._place: list[Passager]

    def to_sting(self):
        return f"{self._place}, {self._places}"
    