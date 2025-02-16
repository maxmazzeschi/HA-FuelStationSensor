from dataclasses import dataclass
from typing import Any


@dataclass
class Fuel:
    id: int
    price: float
    name: str
    fuelId: int
    isSelf: bool
    serviceAreaId: int
    insertDate: str
    validityDate: str

    @staticmethod
    def from_dict(obj: Any) -> "Fuel":
        _id = int(obj.get("id"))
        _price = float(obj.get("price"))
        _name = str(obj.get("name"))
        _fuelId = int(obj.get("fuelId"))
        if (str(obj.get("isSelf"))) == "True":
            _isSelf = 1
        else:
            _isSelf = 0
        _serviceAreaId = int(obj.get("serviceAreaId"))
        _insertDate = str(obj.get("insertDate"))
        _validityDate = str(obj.get("validityDate"))
        return Fuel(
            _id,
            _price,
            _name,
            _fuelId,
            _isSelf,
            _serviceAreaId,
            _insertDate,
            _validityDate,
        )

    def to_dict(self):
        """Convert Fuel object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "fuelId": self.fuelId,
            "isSelf": self.isSelf,
            "serviceAreaId": self.serviceAreaId,
            "insertDate": self.insertDate,
            "validityDate": self.validityDate,
        }
