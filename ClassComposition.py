seperator = ', '

class Author:
    def __init__(self, name, email, gender):
        self.__name = name
        self.__email = email
        self.__gender = gender

        if self.__gender not in ['M', 'F']:
            raise ValueError

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getGender(self):
        return self.__gender
    
    def __str__(self):
        return (f"Author[name = {self.__name}, email = {self.__email}, gender = {self.__gender}]")


# class Book:

#     def __init__(self, name, author, price, qty = 0):
#         self.__name = name
#         self.__price = price
#         self.__qty = qty
#         self.__author = author    

#     def getName(self):
#         return self.__name

#     def getAuthor(self):
#         return self.__author

#     def getPrice(self):
#         return self.__price

#     def setPrice(self, price):
#         self.__price = price

#     def getQty(self):
#         return self.__qty

#     def setQty(self, qty):
#         self.__qty = qty

#     def __str__(self):
#         return (f"Book[{self.__name}, {self.__author}, {self.__price}, {self.__qty}]")

#     def getAuthorName(self):
#         return self.getAuthor().getName()

#     def getAuthorEmail(self):
#         return self.getAuthor().getEmail()
    
#     def getAuthorGender(self):
#         return self.getAuthor().getGender()


class Book:

    def __init__(self, name, price, authors = [], qty = 0):
        self.__name = name
        self.__price = price
        self.__qty = qty
        self.__authors = authors    

    def getName(self):
        return self.__name

    def getAuthors(self):
        return self.__authors

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price 

    def getQty(self):
        return self.__qty

    def setQty(self, qty):
        self.__qty = qty

    def __str__(self):
        authorsresult = []
        for authors in self.__authors:
            authorsresult.append(authors.__str__())
        return (f"Book[name = {self.__name}, authors = {seperator.join(authorsresult)}, price = {self.__price}, qty = {self.__qty}]")


    def getAuthorNames(self):
        result = []
        for authors in self.__authors:
            result.append(authors.getName())
        return seperator.join(result)

    def getAuthorEmails(self):
        result = []
        for authors in self.__authors:
            result.append(authors.getEmail())
        return seperator.join(result)

    def getAuthorGenders(self):
        result = []
        for authors in self.__authors:
            result.append(authors.getGender())
        return seperator.join(result)


author1 = Author('Fitzgerald', 'fitzgerald@email.com', 'M')
author2 = Author('Flaubert', 'flaubert@email.com', 'M')
Testbook = Book('Gatsby' , '20.0', [author1, author2], '1')

# print(author1.getName())
# print(author1.getEmail())   
# print(author1.getGender())
# author1.setEmail('f.scott@email.com')
# print(author1.getEmail())
# print(author1.__str__())

# print(Testbook.getAuthor())
# print(Testbook.__str__())

# print(Testbook.getAuthor().getName())
# print(Testbook.getAuthor().getEmail())

print(Testbook)
print(Testbook.getAuthors())
print(Testbook.getAuthorNames())
print(Testbook.getAuthorEmails())

