import doctest

class Project:
    def __init__(self, name: str, designer: str, area: float, cost_of_meter: float):
        """
        Создание и подготовка к работе объекта "Проект"

        :param name: Название проекта
        :param designer: Фамилия дизайнера проекта
        :param area: Площадь объекта в квадратных метрах
        :param cost_of_meter: Стоимость одного квадратного метра проекта

        Примеры:
        >>> project = Project("Апарт-отель", "Михайлов", 215, 2000)
        """
        self.name = name
        if not isinstance(designer, (str)):
            raise TypeError("Фамилия дизайнера проекта должна быть типа str")
        self.designer = designer
        if not isinstance(area, (int, float)):
            raise TypeError("Площадь объекта должна быть типа int или float")
        if area <= 0:
            raise ValueError("Площадь объекта должна быть положительным числом")
        self.area = area
        if not isinstance(cost_of_meter, (int, float)):
            raise TypeError("Стоимость одного квадратного метра проекта должна быть типа int или float")
        if cost_of_meter <= 0:
            raise ValueError("Стоимость одного квадратного метра проекта должна быть положительным числом")
        self.cost_of_meter = cost_of_meter

    def calculate_building_volume(self, floor_height: float) -> float:
        """
        Функция, вычисляющая строительный объем

        :param floor_height: Высота этажа в метрах

        :return: Значение строительного объема

        Примеры:
        >>> project = Project("Апарт-отель", "Михайлов", 215, 2000)
        >>> project.calculate_building_volume(3.6)
        """
        ...

    def cost_of_design(self, area, cost_of_meter) -> float:
        """
        Функция которая считает стоимость дизайн-проекта

        Примеры:
        >>> project = Project("Апарт-отель", "Михайлов", 215, 2000)
        >>> project.cost_of_design(215, 2000)
        """
        return self.area * self.cost_of_meter

    def __str__(self):
        return f"Проект {self.name}. Дизайнер {self.designer}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, designer={self.designer!r})"


class Skyscraper(Project):
    """
    Создание и подготовка к работе объекта "Небоскреб"

    :param name: Название проекта
    :param designer: Фамилия дизайнера проекта
    :param area: Площадь объекта в квадратных метрах
    :param cost_of_meter: Стоимость одного квадратного метра проекта
    :param number_of_floors: Количество типовых этажей
    :param year_of_foundation: Год ввода в экспуатацию

    Примеры:
    >>> skyscraper = Skyscraper("Апарт-отель", "Михайлов", 215, 2000, 26, 2017)
    """
    def __init__(self, name: str, designer: str, area: float, cost_of_meter: float, number_of_floors: int, year_of_foundation: int):
        super().__init__(name, designer, area, cost_of_meter)
        if not isinstance(number_of_floors, int):
            raise TypeError("Количество типовых этажей должно быть типа int")
        if number_of_floors <= 0:
            raise ValueError("Количество типовых этажей должно быть положительным числом")
        self.number_of_floors = number_of_floors
        if not isinstance(year_of_foundation, int):
            raise TypeError("Год ввода в экспуатацию должен быть типа int или float")
        if year_of_foundation <= 0:
            raise ValueError("Год ввода в экспуатацию должен быть положительным числом")
        self.year_of_foundation = year_of_foundation

    def cost_of_design(self, area, cost_of_meter, number_of_floors) -> float:
        """
        Вычислим стоимость дизайн-проекта
        Перегружаем метод базового класса, так как здание многоэтажное и состоит из числа типовых этажей

        Примеры:
        >>> skyscraper = Skyscraper("Апарт-отель", "Михайлов", 215, 2000, 26, 2017)
        >>> skyscraper.cost_of_design(215, 2000, 26)
        """
        return self.area * self.cost_of_meter * self.number_of_floors

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, designer={self.designer!r}, year_of_founfation={self.year_of_foundation!r})"
# Пустая строка