from pydantic import BaseModel, Field
from enum import Enum

class ColorEnum(str, Enum):
    red = "red"
    green = "green"
    blue = "blue"
    yellow = "yellow"
    black = "black"
    white = "white"
    grey = "grey"
    orange = "orange"
    pink = "pink"
    purple = "purple"
    brown = "brown"
    silver = "silver"
    gold = "gold"
    bronze = "bronze"

class TransmissionEnum(str, Enum):
    manual = "manual"
    automatic = "automatic"
    semi_automatic = "semi-automatic"

class FuelTypeEnum(str, Enum):
    gasoline = "gasoline"
    ethanol = "ethanol"
    diesel = "diesel"
    electric = "electric"
    hybrid = "hybrid"

class MotorTypeEnum(str, Enum):
    v4 = "V4"
    v6 = "V6"
    v8 = "V8"
    v10 = "V10"
    v12 = "V12"
    inline4 = "Inline-4"
    inline6 = "Inline-6"
    rotary = "Rotary"
    electric = "Electric"

class AutomobileSchema(BaseModel):
    year: str = Field(..., min_length=4, max_length=4)
    model: str = Field(..., min_length=2, max_length=255)
    color: ColorEnum
    manufacturer: str
    motor: MotorTypeEnum
    fuel: FuelTypeEnum
    price: str
    kilometers: int = Field(..., ge=0)
    transmission: TransmissionEnum
    number_of_wheels: int = Field(..., ge=2, le=5)


