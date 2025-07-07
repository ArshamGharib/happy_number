def check_happy(n: int) -> bool:
    """Some of the numbers are happy numbers

    :param n: Your number
    :return: checks your number if it is a happy number
        with True or False
    """
    seen_number = set()
    while (n != 1) and (n not in seen_number):
        seen_number.add(n)
        n = sum([int(i)**2 for i in str(n)])
    return n == 1


if __name__ == "__main__":
    assert check_happy(7) is True
    assert check_happy(8) is False

    n = input('write your number: ')
    print(check_happy(int(n)))
