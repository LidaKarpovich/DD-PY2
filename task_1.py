from typing import Union


class Phone:
    def __init__(self, brand: str, model: Union[str, int], memory: float, busy_memory: float, price: Union[int, float]):
        """
        Инициализация класса Phone. Является родительским классам для нескольких других
        :param brand: получаемое имя производителя телефона
        :param model: получаемое значение модели телефона
        :param memory: получаемое значение памяти телефона (в ГБ)
        :param busy_memory: получаемое значение памяти телефона, занятой базовыми настройками
        :param price: получаемая цена опредленного телефона (в рублях)
        """
        self.brand = brand
        self.model = model
        self.memory = memory
        self.busy_memory = busy_memory
        self.price = price

    @property
    def brand(self) -> str:
        """
        :return: Возвращает установленное имя производителя
        """
        return self._brand

    @brand.setter
    def brand(self, new_brand) -> None:
        """
        Установка полученного имя производителя
        :param new_brand: получение имя производителя
        :return: ---
        """
        if not isinstance(new_brand, str):  # проверка на правильность типа
            raise TypeError
        self._brand = new_brand

    @property
    def model(self) -> Union[str, int]:
        """
        :return: Возвращает установленное название модели
        """
        return self._model

    @model.setter
    def model(self, new_model) -> None:
        """
        Установка названия модели
        :param new_model: полученное название модели
        :return: ---
        """
        if not isinstance(new_model, (str, int)):
            raise TypeError
        self._model = new_model

    @property
    def memory(self) -> float:
        """
        :return: Возвращает установленное значение памяти
        """
        return self._memory

    @memory.setter
    def memory(self, new_memory) -> None:
        """
        Установка полученного значения памяти
        :param new_memory: получение значения памяти
        :return: ---
        """
        if not isinstance(new_memory, float):  # проверка на правильность типа
            raise TypeError
        if new_memory < 0:  # проверка на корректность значения
            raise ValueError
        self._memory = new_memory

    @property
    def busy_memory(self) -> float:
        """
        :return: Возвращает установленное значение памяти, занятой базовыми настройками
        """
        return self._busy_memory

    @busy_memory.setter
    def busy_memory(self, new_busy_memory) -> None:
        """
        Установка полученного значения памяти
        :param new_busy_memory: получение значения памяти, занятое базовыми настройками
        :return: ---
        """
        if not isinstance(new_busy_memory, float):  # проверка на правильность типа
            raise TypeError
        if new_busy_memory < 0:  # проверка на корректность значения
            raise ValueError
        self._busy_memory = new_busy_memory

    @property
    def price(self) -> Union[int, float]:
        """
        :return: Возвращает установленное значение цены
        """
        return self._price

    @price.setter
    def price(self, new_price) -> None:
        """
        Установка полученного значения цены
        :param new_price: получение значения цены
        :return: ---
        """
        if not isinstance(new_price, (int, float)):  # проверка на правильность типа
            raise TypeError
        if 0 > new_price:  # проверка на корректность значения
            raise ValueError
        self._price = new_price

    def free_memory(self):
        """
        Вычисление свободной памяти телефона (без базовых настроек)
        :return: возвращает объем свободной памяти
        """
        free = self.memory - self.busy_memory
        return free

    def __str__(self):
        return f"Телефон. Бренд = {self.brand}. Модель = {self.model}. Общий объем памяти = {self.memory}. Занятая память = {self.busy_memory}. Цена = {self.price}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, memory={self.memory!r}, busy_memory={self.busy_memory!r}, price={self.price!r})"


class Touch_Tone(Phone):
    def __init__(self, brand: str, model: Union[str, int], memory: float, busy_memory: float, price: Union[int, float], new_sim: float):
        """
        Инициализируем кнопочный телефон, наследуюя от родительского класса Телефон
        :param new_sim: дополнительное количество памяти, которое можно добавить с помощью карты памяти
        """
        super().__init__(brand, model, memory, busy_memory, price)
        self.new_sim = new_sim

    @property
    def new_sim(self) -> float:
        """
        :return: Возвращаем количество дополнительной памяти
        """
        return self._new_sim

    @new_sim.setter
    def new_sim(self, new_amount) -> None:
        """
        Устанавливаем значение дополнительной памяти
        :param new_amount: объем новой памяти
        :return: ---
        """
        if not isinstance(new_amount, float):
            raise TypeError
        if new_amount < 0:
            raise ValueError
        self._new_sim = new_amount

    def free_memory(self):
        """
        Перегружаем метод free_memory, подстраиваясь под объем памяти + новая память с карты памяти
        :return: Итоговый объем памяти
        """
        value = (super().free_memory() + self.new_sim)
        return value

    def __str__(self):
        return f"Телефон. Бренд = {self.brand}. Модель = {self.model}. Общий объем памяти = {self.memory}. Занятая память = {self.busy_memory}. Цена = {self.price}, Доп.память = {self.new_sim}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, memory={self.memory!r}, busy_memory={self.busy_memory!r}, price={self.price!r}, new_sim={self.new_sim!r})"


class Touchscreen(Phone):
    def __init__(self, brand: str, model: Union[str, int], memory: float, busy_memory: float, price: Union[int, float], diagonal: float):
        """
        Инициализируем сенсорные телефоны, наследуем из класса Phone
        :param diagonal: диагональ экрана (в дюймах)
        """
        super().__init__(brand, model, memory, busy_memory, price)
        self.diagonal = diagonal

    @property
    def diagonal(self) -> float:
        """
        :return: возвращаем размер диагонали экрана параметр объекта
        """
        return self._diagonal

    @diagonal.setter
    def diagonal(self, new_diagonal) -> None:
        """
        Устанавливаем необходимый размер диагонали
        :param new_diagonal: диагональ экрана
        :return: ---
        """
        if not isinstance(new_diagonal, float):
            raise TypeError
        if new_diagonal < 0:
            raise ValueError
        self._diagonal = new_diagonal

    def free_memory(self):
        """
        Перегрузка метода вычисления свободной памяти
        :return: объем свободной памяти
        """
        value = (super().free_memory())
        return value

    def __str__(self):
        return f"Телефон. Бренд = {self.brand}. Модель = {self.model}. Общий объем памяти = {self.memory}. Занятая память = {self.busy_memory}. Цена = {self.price}, Диагональ = {self.diagonal}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, memory={self.memory!r}, busy_memory={self.busy_memory!r}, price={self.price!r}, diagonal={self.diagonal!r})"

if __name__ == "__main__":
    phone_1 = Touch_Tone("Nokia", "3310 DS", 0.015, 0.002, 3120, 16.0)
    print(phone_1)
    print(phone_1.free_memory())
    print(phone_1.__repr__())

    phone_2 = Touchscreen("Apple", "IPhone 11", 127.9, 2.1, 54200, 6.06)
    print(phone_2)
    print(phone_2.free_memory())
    print(phone_2.__repr__())
    pass

