class MinusPriceException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message


try:
    price = float(input('Enter the price: '))
    if 0 > price:
        raise MinusPriceException('The price cannot be less than 0!')
except MinusPriceException as err:
    print(err.get_exception_message())
except ValueError:
    print('The price must be in numbers only!')
else:
    print(f'Price: {price}')