from typing import List


class MenuItem:
    def __init__(self, name: str, price: float) -> None:
        self._name: str = name
        self._price: float = price

    def calculate_total(self) -> float:
        return self._price


class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size: str) -> None:
        super().__init__(name, price)
        self.size: str = size


class Appetizer(MenuItem):
    def __init__(
        self, name: str, price: float, is_shareable: bool
    ) -> None:
        super().__init__(name, price)
        self.is_shareable: bool = is_shareable


class MainCourse(MenuItem):
    def __init__(
        self, name: str, price: float, calories: int
    ) -> None:
        super().__init__(name, price)
        self.calories: int = calories


class Order:
    def __init__(self) -> None:
        self.items: List[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def show_order(self) -> None:
        print("\n======= TU PEDIDO =======")
        if not self.items:
            print("No has agregado productos.")
        else:
            for item in self.items:
                print(f"- {item._name} ........ $ {item._price:.3f}")

    def calculate_total(self) -> float:
        total: float = 0.0
        for item in self.items:
            total = total + item.calculate_total()
        return total

    def apply_discount(self) -> float:
        total: float = self.calculate_total()

        if total > 50:
            print("\nDescuento aplicado: 15%")
            total = total * 0.85

        elif total > 30:
            print("\nDescuento aplicado: 5%")
            total = total * 0.95

        elif len(self.items) >= 5:
            print("\nDescuento aplicado: 10%")
            total = total * 0.9

        return total


menu: List[MenuItem] = [
    Beverage("Agua", 2.0, "Mediana"),
    Beverage("Gaseosa", 3.0, "Grande"),
    Beverage("Jugo", 4.0, "Mediano"),
    Appetizer("Papas fritas", 5.0, True),
    Appetizer("Nachos", 6.0, True),
    Appetizer("Aros de cebolla", 5.5, True),
    MainCourse("Hamburguesa", 10.0, 800),
    MainCourse("Pizza", 12.0, 900),
    MainCourse("Pasta", 11.0, 700),
    MainCourse("Ensalada", 8.0, 400),
]


order: Order = Order()

while True:
    print("\n======= MENÚ =======")
    for i in range(len(menu)):
        print(f"{i}. {menu[i]._name} ........ $ {menu[i]._price:.3f}")

    print("\nOpciones:")
    print("a -> Agregar producto")
    print("v -> Ver pedido")
    print("t -> Terminar")

    option: str = input("\nSeleccione una opción: ")

    if option == "a":
        choice: str = input("Ingrese el número del producto: ")

        if choice.isdigit():
            index: int = int(choice)

            if 0 <= index < len(menu):
                order.add_item(menu[index])
                print("Producto agregado")
            else:
                print("Número inválido")
        else:
            print("Ingrese un número válido")

    elif option == "v":
        order.show_order()

    elif option == "t":
        break

    else:
        print("Opción no válida")


print("\n======= RESUMEN =======")
order.show_order()

print("\n--------------------------")
print(f"Total: $ {order.calculate_total():.3f}")
print(f"Total con descuento: $ {order.apply_discount():.3f}")
print("--------------------------")
