from Cars import Cars_info
from Cars import Car_manager

manager = Car_manager()

while True:
    print("\n1) Show all cars\n2) Add a car\n3) Find by name\n4) Delet car\n5) Exit")
    try:
        choice = int(input("Choose: "))
    except ValueError:
        print("Enter a number.")
        continue

    match choice:
        case 1:
            manager.show_all_cars()
        case 2:
            manager.add_car()
        case 3:
            q = input("Name to find: ")
            manager.find_cars(q)
        case 4:
            n = input('Car name: ')
            manager.delet_car(n)
        case 5:
            print("Bye!")
            break
        case _:
            print("Invalid option.")