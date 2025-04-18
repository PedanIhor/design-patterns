from abc import ABC, abstractmethod

# Abstract Factory Pattern
# Abstract classes for furniture
class Chair(ABC):
    @abstractmethod
    def sit_on(self) -> str: pass

class Table(ABC):
    @abstractmethod
    def eat_at(self) -> str: pass

class Sofa(ABC):
    @abstractmethod
    def lie_on(self) -> str: pass

# Abstract Factory class
class FurnitureAbstractFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair: pass

    @abstractmethod
    def create_table(self) -> Table: pass

    @abstractmethod
    def create_sofa(self) -> Sofa: pass

# Implementations of furniture for different styles
class VictorianChair(Chair):
    def sit_on(self) -> str:
        return "Sitting on a Victorian chair."

class VictorianTable(Table):
    def eat_at(self) -> str:
        return "Eating at a Victorian table."

class VictorianSofa(Sofa):
    def lie_on(self) -> str:
        return "Lying on a Victorian sofa."

class ModernChair(Chair):
    def sit_on(self) -> str:
        return "Sitting on a modern chair."

class ModernTable(Table):
    def eat_at(self) -> str:
        return "Eating at a modern table."

class ModernSofa(Sofa):
    def lie_on(self) -> str:
        return "Lying on a modern sofa."

class ArtDecoChair(Chair):
    def sit_on(self) -> str:
        return "Sitting on an Art Deco chair."

class ArtDecoTable(Table):
    def eat_at(self) -> str:
        return "Eating at an Art Deco table."

class ArtDecoSofa(Sofa):
    def lie_on(self) -> str:
        return "Lying on an Art Deco sofa."

# Factories for different styles
class ModernFurnitureFactory:
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

class ArtDecoFurnitureFactory:
    def create_chair(self) -> Chair:
        return ArtDecoChair()

    def create_table(self) -> Table:
        return ArtDecoTable()

    def create_sofa(self) -> Sofa:
        return ArtDecoSofa()

class VictorianFurnitureFactory:
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_table(self) -> Table:
        return VictorianTable()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


# Test code
def test_furniture(factory: FurnitureAbstractFactory) -> None:
    chair = factory.create_chair()
    table = factory.create_table()
    sofa = factory.create_sofa()

    print(chair.sit_on())
    print(table.eat_at())
    print(sofa.lie_on())

if __name__ == "__main__":
    # Test with Modern Furniture Factory
    print("Modern Furniture:")
    modern_factory = ModernFurnitureFactory()
    test_furniture(modern_factory)

    # Test with Art Deco Furniture Factory
    print("\nArt Deco Furniture:")
    art_deco_factory = ArtDecoFurnitureFactory()
    test_furniture(art_deco_factory)

    # Test with Victorian Furniture Factory
    print("\nVictorian Furniture:")
    victorian_factory = VictorianFurnitureFactory()
    test_furniture(victorian_factory)