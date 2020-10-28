class Databass:

    __id = []
    __name = []
    __rej = []
    __year = []
    __country = []

    def __init__(self):
        self.__id.append(0)
        self.__name.append("Ntest")
        self.__rej.append("Rtest")
        self.__year.append("Ytest")
        self.__country.append("Ctest")

    # сохранение в файл
    def save(self):
        f = open("databass.txt", "w")
        f.write(str(len(self.__id)))
        f.write("\n")
        for i in self.__id:
            f.write(self.__name[i] + "|")
            f.write(self.__rej[i] + "|")
            f.write(self.__year[i] + "|")
            f.write(self.__country[i] + "|")
            f.write("\n")
        f.close()

    # загрузка из файла
    def load(self):
        try:
            f = open("databass.txt", "r")
            self.__id = []
            self.__name = []
            self.__rej = []
            self.__year = []
            self.__country = []
            for i in range(int(f.readline())):
                self.__id.append(i)
            for i in self.__id:
                s = f.readline()
                s = s.split("|")
                self.__name.append(s[0])
                self.__rej.append(s[1])
                self.__year.append(s[2])
                self.__country.append(s[3])
            f.close()
        except FileNotFoundError:
            print("Файл не найден, ты чего творишь?")

    # добавление в файл
    def append(self, name, rej, year, country):
        self.__id.append(len(self.__id))
        self.__name.append(name)
        self.__rej.append(rej)
        self.__year.append(year)
        self.__country.append(country)
        self.save()

    # изменение записи
    def change(self, id, pole, word):
        if pole == "название":
            self.__name[int(id)] = word
        elif pole == "режисер":
            self.__rej[int(id)] = word
        elif pole == "год":
            self.__year[int(id)] = word
        elif pole == "страна":
            self.__country[int(id)] = word
        self.save()

    # поиск записи
    def find(self, pole, word):
        try:
            if pole == "название":
                return self.__name.index(word)
            elif pole == "режисер":
                return self.__rej.index(word)
            elif pole == "год":
                return self.__year.index(word)
            elif pole == "страна":
                return self.__country.index(word)
        except ValueError:
            return -1


    # удаление записи по id
    def delete(self, id):
        self.__name.pop(id)
        self.__rej.pop(id)
        self.__year.pop(id)
        self.__country.pop(id)
        self.__id = []
        for i in range(len(self.__name)):
            self.__id.append(i)
        self.save()

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_rej(self):
        return self.__rej

    def get_year(self):
        return self.__year

    def get_country(self):
        return self.__country