from automobil.database.types import ColorEnum, TransmissionEnum, FuelTypeEnum, MotorTypeEnum
from automobil.database.models import Automobile, engine
from typing import Optional, List, Dict, Any
from mcp.server.fastmcp import FastMCP
from sqlalchemy.orm import sessionmaker
from sqlalchemy import cast, Numeric

mcp = FastMCP()

@mcp.tool(
    name="query_automobiles",
    description="Queries the car database based on specified criteria."
)

def query_automobiles(
    year: Optional[str] = None,
    model: Optional[str] = None,
    color: Optional[ColorEnum] = None,
    manufacturer: Optional[str] = None,
    motor: Optional[MotorTypeEnum] = None,
    fuel: Optional[FuelTypeEnum] = None,
    max_price: Optional[float] = None,
    max_kilometers: Optional[int] = None,
    transmission: Optional[TransmissionEnum] = None,
) -> List[Dict[str, Any]]:
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    with Session() as session:

        query = session.query(Automobile)

        if year:
            query = query.filter(Automobile.year == year)
        if model:
            query = query.filter(Automobile.model.ilike(f"%{model}%"))
        if color:
            query = query.filter(Automobile.color == color.value)
        if manufacturer:
            query = query.filter(Automobile.manufacturer.ilike(f"%{manufacturer}%"))
        if motor:
            query = query.filter(Automobile.motor == motor.value)
        if fuel:
            query = query.filter(Automobile.fuel == fuel.value)
        if max_price is not None:
            query = query.filter(cast(Automobile.price, Numeric) <= max_price)
        if max_kilometers is not None:
            query = query.filter(Automobile.kilometers <= max_kilometers)
        if transmission:
            query = query.filter(Automobile.transmission == transmission.value)

        results = query.all()

        automobiles_list = []
        for auto in results:
            automobiles_list.append(
                {
                    "id": auto.id,
                    "year": auto.year,
                    "model": auto.model,
                    "color": auto.color,
                    "manufacturer": auto.manufacturer,
                    "motor": auto.motor,
                    "fuel": auto.fuel,
                    "price": auto.price,
                    "kilometers": auto.kilometers,
                    "transmission": auto.transmission,
                    "number_of_wheels": auto.number_of_wheels,
                }
            )
        return automobiles_list
