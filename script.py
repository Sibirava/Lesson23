from car import Car
from lorry import Lorry
from gasstation import GasStation


def main():
    ls = [Car(50), Car(150), Car(150), Car(100), Car(5), Lorry(545)]

    total = GasStation.calculate_total_fuel(ls)

    print(f"Total: {total}")


if __name__ == "__main__":
    main()