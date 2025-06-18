from .backend.data_processor import DataProcessor
from .backend.persistence.e_commerce_persistence import booting_ecommerce_system

def main():
    print("Booting the system...")
    booting_ecommerce_system()

    print("Simulating operations...")

    print("------------------------------------------------------------------")
    print("   Calculate the current prices...")
    print("------------------------------------------------------------------")

    processor = DataProcessor()
    processor.calculate_data(False)  # don't change the date
    print_report(processor)

    print("------------------------------------------------------------------")
    print("   Job signals a new day has started, prices need to be updated...")
    print("------------------------------------------------------------------")

    processor.calculate_data(True)  # move to next day
    print_report(processor)

def print_report(processor):
    print("Current prices of scheduled training courses:")
    print("---------------------------------------------")
    for item in processor.get_list():
        print(f"Type: {item.type}")
        print(f"When: {item.tr_date}")
        print(f"Remaining days before training course: {item.days}")
        print(f"Full Price: {item.full}")
        print(f"Current price: {item.curr}")
        print(f"Number of seats: {item.seats}")
        print(f"Remaining available seats: {item.avail}")
        print()
    print(f"Remaining total sales target: {processor.get_sales_value()}")

main()
