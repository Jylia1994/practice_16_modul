class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f"{self.name} {self.surname}.{self.city}.Баланс:{self.balance} руб."
    def get_client(self):
        return f"{self.name} {self.surname},г.{self.city}."

client_1 = Client("Иван", "Петров", "Москва", 50)
client_2 = Client("Катерина", "Соколова", "Казань", 100)
client_3 = Client("Александр", "Иванов", "Тверь", 70)
client_4 = Client("Василий", "Пупкин", "Коломна", 50)

print(client_1)
print(" ")
print(client_1.get_client())
print(" ")
client_list = [client_1,client_2,client_3,client_4]
for guest in client_list:
    print(guest.get_client())