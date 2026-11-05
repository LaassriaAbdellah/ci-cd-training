
from validation import validate_order


def main():
    print("Application de validation des commandes")

    orders = [
        (100, 2),
        (-50, 3),
        (200, 0),
        (150, 5)
    ]

    for amount, quantity in orders:
        valid = validate_order(amount, quantity)

        if valid:
            print(f"Commande valide : {amount}, {quantity}")
        else:
            print(f"Commande invalide : {amount}, {quantity}")


if __name__ == "__main__":
    main()
