# Linked list

# Что такое LinkedList?

# LinkedList или связный список – это структура данных.
# Связный список обеспечивает возможность создать двунаправленную
# очередь из каких-либо элементов. Каждый элемент такого списка
# считается узлом. По факту в узле есть его значение, а также
# две ссылки – на предыдущий и на последующий узлы. То есть
# список «связывается» узлами, которые помогают двигаться вверх
# или вниз по списку. Из-за таких особенностей строения из связного
# списка можно организовать стек, очередь или двойную очередь.

# Давайте визуализируем сухие определения. Теперь у нас есть коты,
# которые сидят в коробках. И на каждой коробке написано какая
# она по порядку и за какой должна стоять.

# Что мы будем делать со связным списком:

# 1) Проверять содержится ли в нем тот или иной элемент;
# 2) Добавлять узлы в конец;
# 3) Получать значение узла по индексу;
# 4) Удалять узлы.

class Box:
    def __init__(self, cat = None):
        self.cat = cat
        self.nextcat = None

    class LinkedList:
        def __init__(self):
            self.head = None


        def contains(self, cat):
            lastbox = self.head
            while (lastbox):
                if cat == lastbox.cat:
                    return True
                else:
                    lastbox = lastbox.nextcat
                return False

        def addToEnd(self, newcat):
            newbox = Box(newcat)
            if self.head is None:
                self.head = newbox
                return
            lastbox = self.head
            while (lastbox.nextcat):
                lastbox = lastbox.nextcat
            lastbox.nextcat = newbox

        def get(self, catIndex):
            lastbox = self.head
            boxIndex = 0
            while boxIndex <= catIndex:
                if boxIndex == catIndex:
                    return lastbox.cat
                boxIndex = boxIndex + 1
                lastbox = lastbox.nextcat

        def removeBox(self, rmcat):
            headcat = self.head

            if headcat is not None:
                if headcat.cat == rmcat:
                    self.head = headcat.nextcat
                    headcat = None
                    return
            while headcat is not None:
                if headcat.cat == rmcat:
                    break
                lastcat = headcat
                headcat = headcat.nextcat
            if headcat == None:
                return
            lastcat.nextcat = headcat.nextcat
            headcat = None

        def LLprint(self):
            currentCat = self.head
            print("LINKED LIST")
            print("-----")
            i = 0
            while currentCat is not None:
                print(str(i) + ": " + str(currentCat.cat))
                i += 1
                currentCat = currentCat.nextcat
            print("-----")



