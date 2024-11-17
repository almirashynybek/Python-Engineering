class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item: str):
        self.__items.append(item)  # Corrected the typo here

    def __len__(self):
        print("Количество товаров в корзине:", end = '')
        return len(self.__items)  # Return the length of the list (not a string)
    
    def __getitem__(self, index: int):
        return self.__items[index]
    
    def __setitem__(self, index: int, value: str):  # Added 'value' argument here
        self.__items[index] = value  # Set the item at the specified index
    
    def __str__(self):
        return (
            f"В вашей корзине к покупке следующие товары: "
            f"{', '.join(self.__items) if self.__items else 'корзина пуста'}"
        )

# Example usage
cart = ShoppingCart()  # Create an instance of ShoppingCart
cart.add_item("Кофе")
cart.add_item("Книга")

print(len(cart))  # Output: 2
print(cart[0])  # Output: Кофе

cart[1] = 'Журнал'  # Update the item at index 1
print(cart)  # Output: В вашей корзине к покупке следующие товары: Кофе, Журнал
