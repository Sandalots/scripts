import random as r
def main():
    return r.randint(1, 999)


def convert_to_binary(num):
    return bin(num)


def convert_to_hex(num):
    return hex(num)


def convert_to_octal(num):
    return oct(num)


if __name__ == "__main__":
    print(main())
    print(convert_to_binary(main()))
    print(convert_to_hex(main()))
    print(convert_to_octal(main()))