import doctest


class Phone:
    def __init__(self, brand: str, memory_capacity: (int, float), occupied_volume: (int, float)):
        """
        Создание и подготовка к работе объекта "Телефон"
        :param brand: Производитель
        :param memory_capacity: Объем памяти
        :param occupied_volume: Занимаемый объем
        Примеры:
        >>> phone = Phone("iPhone", 32, 1.1)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Производитель должен быть типа str")

        self.brand = brand

        if not isinstance(memory_capacity, (int, float)):
            raise TypeError("Объем памяти должн быть int или float")
        if occupied_volume <= 0:
            raise ValueError("Объем памяти не может быть не положительным числом")
        self.memory_capacity = memory_capacity

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Занимаемый объем памяти должн быть int или float")
        if occupied_volume <= 0:
            raise ValueError("Занимаемый объем памяти не может быть не положительным числом")
        self.occupied_volume = occupied_volume

    def brand_phone(self, another_phone: str) -> bool:
        """
        Сравнивает бред телефона с необходимым
        :param another_phone: необходимый бренд
        :raise TypeError: если another_phone не строка
        :return: Совпадает ли бренд
        Примеры:
        >>> phone = Phone("iPhone", 32, 1.1)
        >>> phone.brand_phone("Samsung")
        """
        ...

    def has_phone_enough_memory(self, another_memory: (int, float)) -> None:
        """
        Сравнивает количество необходимой памяти
        :param another_memory: Объем памяти в интересуемом телефоне
        :raise ValueError: Если количество интересуемой памяти меньше 0, то вызываем ошибку
        Примеры:
        >>> phone = Phone("iPhone", 32, 1.1)
        >>> phone.has_phone_enough_memory(16)
        """

        if not isinstance(another_memory, (int, float)):
            raise TypeError("Память должна быть типа int или float")
        if another_memory < 0:
            raise ValueError("Память должна должна положительным числом")
        ...

    def new_occupied_memory(self, new_memory: (int, float)):
        """
        Заполение используемой памяти телефона.
        :param new_memory: Объем добавляемой памяти
        :raise ValueError: Если количество добавляемой памяти превышает объем допустимой памяти телефона,
        то возвращается ошибка.
        :return: Объем занимаемой памяти
        Примеры:
        >>> phone = Phone("iPhone", 32, 1.1)
        >>> phone.new_occupied_memory(20)
        """
        ...


class Flower:
    def __init__(self, type_: str, availability: bool, amount: int):
        """
        Создание и подготовка к работе объекта "Цветок"
        :param type_: Вид цветка (сорт)
        :param availability: наличие в магазине
        :param amount: Доступное количество
        Примеры:
        >>> flower = Flower("Роза", True, 10)  # инициализация экземпляра класса
        """
        if not isinstance(type_, str):
            raise TypeError("Вид цветка должен быть типа str")

        self.type_ = type_

        if not isinstance(availability, bool):
            raise TypeError("Наличие должно быть bool")
        self.availability = availability

        if not isinstance(amount, int):
            raise TypeError("Количество должно быть int")
        if amount < 0:
            raise ValueError("Количество не может быть отрицательным числом")
        self.amount = amount

    def type_flower(self, another_type: str) -> bool:
        """
        Сравнивает тип цветка с необходимым
        :param another_type: необходимый цветок
        :raise TypeError: если another_type не строка
        :return: Совпадает ли тип цветка
        Примеры:
        >>> flower = Flower("Роза", True, 10)
        >>> flower.type_flower("Лилия")
        """
        ...

    def to_sell(self):
        """
        Если availability == True: Товар в наличии
        Если availability == False: Товар отсутсвует
        :raise TypeError: Тип данных должен быть bool
        Примеры:
        >>> flower = Flower("Роза", True, 10)
        >>> flower.to_sell()
        """
        ...

    def new_amount(self, new_flowers: int):
        """
        Добавление нового количества цветов
        :param new_flowers: Количество новых цветов
        :raise ValueError: Если количество новых цветов отрицательная величина
        :return: Объем занимаемой памяти
        Примеры:
        >>> flower = Flower("Роза", True, 10)
        >>> flower.new_amount(20)
        """
        ...


class Vkontakte:
    def __init__(self, name_surname: str, year_of_birth: int, amount_of_friends: int):
        """
        Создание и подготовка к работе объекта "Страница ВКонтакте"
        :param name_surname: Имя Фамилия владельца страницы
        :param year_of_birth: год рождения в формате **** - число от 1900 до 2022
        :param amount_of_friends: Количество друзей
        Примеры:
        >>> vk = Vkontakte("Иван Иванов", 1990, 100)  # инициализация экземпляра класса
        """
        if not isinstance(name_surname, str):
            raise TypeError("Имя Фамилия должены быть типа str")

        self.name_surname = name_surname

        if not isinstance(year_of_birth, int):
            raise TypeError("Год рождения должна быть типа int")
        if year_of_birth < 1900:
            raise ValueError("Человек должен быть не старше 1900 года")
        if year_of_birth > 2022:
            raise ValueError("Человек должен быть не младше 2022 года")
        self.year_of_birth = year_of_birth

        if not isinstance(amount_of_friends, int):
            raise TypeError("Количество друзей должно быть int")
        if amount_of_friends < 0:
            raise ValueError("Количество друзей не может быть отрицательным числом")
        self.amount_of_friends = amount_of_friends

    def is_it_name(self, another_human: str) -> bool:
        """
        Сравнивает имя владельца с необходимым
        :param another_human: необходимая страница
        :raise TypeError: если another_human не строка
        :return: Совпадает ли имя владельца
        Примеры:
        >>> vk = Vkontakte("Иван Иванов", 1990, 100)
        >>> vk.is_it_name("Вова Иванов")
        """
        ...

    def acceptable_age(self, current_year: int) -> bool:
        """
        current_age = current_year - year_of_birth
        Если current_age >= 18: Человек совершеннолетний, функция выдает True
        Если current_age < 18: Человек несовершеннолетний, False
        :raise TypeError: Тип данных должен быть int
        Примеры:
        >>> vk = Vkontakte("Иван Иванов", 1990, 100)
        >>> vk.acceptable_age(2022)
        """
        ...

    def new_amount(self, new_friends: int):
        """
        Добавление новых друзей
        :param new_friends: Количество новых друзей
        :raise ValueError: Если количество новых друзей отрицательная величина
        :return: Общее число друзей после добавления
        Примеры:
        >>> vk = Vkontakte("Иван Иванов", 1990, 100)
        >>> vk.new_amount(3)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
