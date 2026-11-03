
def validate_order(amount, quantity):
    if amount <= 0:
        return False

    if quantity <= 0:
        return False

    return True
