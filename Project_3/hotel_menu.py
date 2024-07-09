print("Welcome!")
menu={
        'Pasta Alfredo': 280,
        'Vegetable Lasagna': 260,
        'Margherita Pizza': 250,
        'Paneer Butter Masala': 240,
        'Cheesecake': 180,
        'Chocolate Brownie': 150,
        'Bruschetta': 130,
        'Spring Rolls': 120,
        'Ice Cream Sundae': 120,
        'Gulab Jamun': 100,
        'Garlic Bread': 100,
        'Cold Coffee': 90,
        'Hot Coffee': 80,
        'Mojito': 70,
        'Orange Juice': 60,
        'Lemonade': 55,
        'Coca Cola': 50,
}

print("\nOur Menu: ")
print("-----------")
total_order = 0
for item, price in menu.items():
    print(f"{item}: Rs.{price}")

next_order = True

while next_order:
    order = input("\nEnter the name of item you want to add in your order: ")
    if order in menu:
        total_order += menu[order]
        print(f"{order} added in your order")
        another_order = input("\nDo you want to add another item? press (yes/no): ").lower()
        if another_order == "yes":
            next_order = True
        else:
            next_order = False
    else:
        print(f"{order} is not available")
        another_order = input("\nDo you want to add another item? press (yes/no): ").lower()
        if another_order == 'yes':
            next_order = True
        else:
            next_order = False

print(f"Your total bill is: Rs.{total_order}")

