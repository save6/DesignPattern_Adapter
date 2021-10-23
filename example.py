from abc import ABCMeta, abstractmethod

class BookShelf(metaclass=ABCMeta):
    @abstractmethod
    def books(self):
        pass

class BookReader(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        pass

class BookShelf(BookShelf):

    def __init__(self,reader:BookReader):
        self.reader = reader
    
    def books(self):
        return self.reader.read()
    
    def printBooks(self):
        print('-----------')
        for book in self.books():
            print(book["title"] + "/著者:" + book["author"])

class JsonBookReader(BookReader):
    def read(self):
        return [
            {'title':'坊ちゃん','author':'夏目漱石'},
            {'title':'人間失格','author':'太宰治'},
            {'title':'走れメロス','author':'太宰治'}
        ]

class CsvBookReader():
    def readCsv(self):
        return [
            ['夏目漱石','坊ちゃん'],
            ['太宰治','人間失格'],
            ['太宰治','走れメロス']
        ]

class CsvBookReaderAdapter(BookReader):

    def __init__(self,csvBookReader:CsvBookReader):
        self.csvBookReader = csvBookReader
    
    def read(self):
        return list(map(lambda x:{'title':x[1],'author':x[0]},self.csvBookReader.readCsv()))

BOOK_SHELF1 = BookShelf(JsonBookReader())
BOOK_SHELF1.printBooks()

BOOK_SHELF2 = BookShelf(CsvBookReaderAdapter(CsvBookReader()))
BOOK_SHELF2.printBooks()