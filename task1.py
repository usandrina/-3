import doctest

class Book:
    >>> book = Book('Хроники Нарнии', 'Клайв С. Льюис')
    >>> name = book.name
    >>> print(name)

    >>> book = Book('Хроники Нарнии', 'Клайв С.Льюис')
    >>> author = book.author
    >>> print(author)

    def __init__(self, name: str, author: str):
        >>> book = Book('Хроники Нарнии','Клайв С. Льюис')

        if not isinstance(name,str):
            raise TypeError('Название книги должно быть строкой')
        if not isinstance(author, str):
            raise TypeError('Автор книги должен быть строкой')
        self._name = name
        self._author = author

    def __str__(self):

        >>> book = Book('Хроники Нарнии', 'Клайв С.Льюис')
        >>> print(f'{book!r}')
        return f'Книга {self.name}, Автор {self.author}'



    def __repr__(self):

        >>> book = Book('Хроники Нарнии', 'Клайв С.Льюис')
        >>> print(f'{book!r}')

        return f'{self.__class__.__name__}(name = {self.name!r}, author = {self.author!r}'

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

class PaperBook (Book):
    >>> paper_book = PaperBook('Хроники Нарнии', 'Клайв С.Льюис', 920)
    >>> pages = paper_book.pages
    >>> print(pages)

    >>> paper_book = PaperBook('Хроники Нарнии', 'Клайв С.Льюис',920)
    >>> paper_book.pages = 1000
    >>> print(paper_book.pages)

    def __int__(self, name: str, author: str, pages: int):
        >>>paper_book = PaperBook('Хроники Нарнии', 'Клайв С.Льюис',920)
        super().__init__(name, author)
        self.pages = pages


    def __repr__(self):
        >>>paper_book = PaperBook('Хроники Нарнии', 'Клайв С.Льюис',920)
        >>>print(f'{paper_book!r}')

        return f'{self.__class__.__name__}(name = {self.name!r}, author = {self.author!r}, pages = {self.pages!r})'

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        if not isinstance(new_pages, int):
           raise TypeError ('Количество страниц должно быть типа int')
        if new_pages <= 0:
            raise ValueError('Количество страниц должно быть положительным числом')
        self._pages = new_pages

class AudioBook (Book):
    >>> audio_book = AudioBook('Хроники Нарнии', 'Клайв С.Льюис', 30.9)
    >>> duration = audio_book.duration
    >>> print(duration)

    def __int__(self, name: str, author: str, duration: float):
        >>> audio_book = AudioBook('Хроники Нарнии', 'Клайв С.Льюис', 30.9)
        super().__init__(name,author)
        self.duration = duration

    def __repr__(self):
        >>> audio_book = AudioBook('Хроники Нарнии', 'Клайв С.Льюис', 30.9)
        >>> print(f'{audio_book!r}')

        return f'{self.__class__.__name__} (name = {self.name!r}, author = {self.author!r}, duration = {self.duration!r}'

    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, new_duration: float):
        if  not isinstance(new_duration, float):
            raise TypeError('Продолжительность должна быть типа float')
        if new_duration <= 0:
            raise ValueError('Продолжительность должна быть положительным числом')
        self._duration = new_duration

if __name__ = '__main__':
    doctest.testmod()
