# Iki adet class yaratacagim, birincisi Item (urun) ikincisi ShoppingCart (alisveris arabasi)
# Urun gereken tum bilgileri icermeli (isim, fiyat)
# Alisveris arabasi sunlari icermeli (kullanicisi, icerdigi urunler) 
# Alisveris arabasi toplam fiyat hesaplayabilmeli, kasada indirim hesaplayabilmeli


class User:
    def __init__(self, name, year) -> None:
        self.name = name
        self.year = year


class Item:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self, user, items) -> None:
        self.user = user
        self.items = items

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def get_checkout(self):
        total = self.get_total()
        return total - total * (self.user.year / 100)

user_1 = User("Ahmet", 10)
user_2 = User("Asli", 5)

item_1 = Item("kalem", 15)
item_2 = Item("cikolata", 10)
item_3 = Item("semsiye", 55)

cart_1 = ShoppingCart(user_1, [item_1, item_3, Item("mont", 250)])
cart_2 = ShoppingCart(user_2, [item_2] * 5)

print(cart_1.get_checkout())
print(cart_2.get_checkout())
