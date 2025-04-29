from abc import ABC, abstractmethod

class Car:
    body: str
    wheels: str
    engine: str
    interior: str
    airco: str
    navigation: str

    def __init__(self):
        self.body = None
        self.wheels = None
        self.engine = None
        self.interior = None
        self.airco = None
        self.navigation = None

    def __str__(self):
        options = ""
        if self.airco:
            options += f" with {self.airco}"
        if self.navigation:
            options += f" and {self.navigation}"
        return f"Car with {self.body}, {self.wheels}, {self.engine}, and {self.interior}{options}."


class CarBuilder(ABC):

    @property
    @abstractmethod
    def car(self):
        """Returns the product created by the builder."""
        pass

    def build_body(self):
        """Builds the body of the car."""
        pass

    @abstractmethod
    def build_wheels(self):
        """Builds the wheels of the car."""
        pass

    @abstractmethod
    def build_engine(self):
        """Builds the engine of the car."""
        pass

    @abstractmethod
    def add_luxury_interior(self):
        """Builds the interior of the car."""
        pass

    @abstractmethod
    def add_airco(self):
        """Builds the air conditioning system of the car."""
        pass

    @abstractmethod
    def add_navigation(self):
        """Builds the navigation system of the car."""
        pass

class CityCarBuilder(CarBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._car = Car()

    @property
    def car(self):
        return self._car

    def build_body(self):
        self._car.body = "Compact body"
        return self

    def build_wheels(self):
        self._car.wheels = "Small wheels"
        return self

    def build_engine(self):
        self._car.engine = "Small engine"
        return self

    def add_basic_interior(self):
        self._car.interior = "Basic interior"
        return self

    def add_luxury_interior(self):
        self._car.interior = "Luxury interior"
        return self

    def add_airco(self):
        self._car.airco = "Air conditioning"
        return self

    def add_navigation(self):
        self._car.navigation = "Navigation system"
        return self

class SUVCarBuilder(CarBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._car = Car()

    @property
    def car(self):
        return self._car

    def build_body(self):
        self._car.body = "SUV body"
        return self

    def build_wheels(self):
        self._car.wheels = "Large wheels"
        return self

    def build_engine(self):
        self._car.engine = "Powerful engine"
        return self

    def add_basic_interior(self):
        self._car.interior = "Basic interior"
        return self

    def add_luxury_interior(self):
        self._car.interior = "Luxury interior"
        return self

    def add_airco(self):
        self._car.airco = "Air conditioning"
        return self

    def add_navigation(self):
        self._car.navigation = "Navigation system"
        return self


class CarDirector:
    def __init__(self, builder: CarBuilder) -> None:
        self.builder = builder

    def construct_everyday_car(self) -> None:
        self.builder\
            .build_body()\
            .build_wheels()\
            .build_engine()

    def construct_luxury_edition_car(self) -> None:
        self.builder\
            .build_body()\
            .build_wheels()\
            .build_engine()\
            .add_luxury_interior()\
            .add_airco()\
            .add_navigation()


# Test code
def produce_car(director: CarDirector):
    # The function can be called with any CarDirector
    # and will produce the car using the appropriate method.
    director.construct_everyday_car()
    print(director.builder.car)

    director.construct_luxury_edition_car()
    print(director.builder.car)

if __name__ == "__main__":
    # Calling the test function with CityCarBuilder
    city_car_builder = CityCarBuilder()
    director = CarDirector(city_car_builder)
    produce_car(director)

    # Calling the test function with SUVCarBuilder
    suv_car_builder = SUVCarBuilder()
    director = CarDirector(suv_car_builder)
    produce_car(director)
