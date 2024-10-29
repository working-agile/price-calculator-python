from price_calculator import DataProcessor, Item

def test_manual():
    print("Today is: 1. January 2025")
    print("Registering training courses:")

    i1 = Item("10 January 2025", 10, 30, 8, True, "CSD", 3000)
    i2 = Item("9 January 2025", 9, 30, 7, True, "CSPO", 4000)
    i3 = Item("20 January 2025", 20, 30, 27, False, "CSM", 3000)
    list = [i1, i2, i3]

    DataProcessor.list = list

    DataProcessor.calculate_data(False)

    for item in list:
        print("------------------------------")
        print("Training course")
        print(f"Type: {item.type}")
        print(f"When: {item.date}")
        print(f"Remaining days before training course: {item.days}")
        print(f"Online: {item.online}")
        print(f"Full Price: {item.full}")
        print(f"Current price: {item.current}")
        print(f"Number of seats: {item.seats}")
        print(f"Remaining available seats: {item.avail}")

    print("-----------------------------------------------------")
    print(f"Total sales target remaining: {DataProcessor.value}")
    print("-----------------------------------------------------")

    print("\n\nMove to next day: 2. January")

    DataProcessor.calculate_data(True)

    print("Registered training courses")

    for item in list:
        print("------------------------------")
        print("Training course")
        print(f"Type: {item.type}")
        print(f"When: {item.date}")
        print(f"Remaining days before training course: {item.days}")
        print(f"Online: {item.online}")
        print(f"Full Price: {item.full}")
        print(f"Current price: {item.current}")
        print(f"Number of seats: {item.seats}")
        print(f"Remaining available seats: {item.avail}")

    print("-----------------------------------------------------")
    print(f"Total sales target remaining: {DataProcessor.value}")
    print("-----------------------------------------------------")
