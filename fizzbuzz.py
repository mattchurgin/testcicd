"""Testing fizzbuzz for ci/cd"""


def fizzbuzz(input_integer: int) -> str:
    """
    Takes an integer and input and outputs fizz if divisible by 5,
    buzz if divisble by 3, fizzbuzz if divisible by both, or the
    integer if else
    """
    if input_integer % 15 == 0:
        return "fizzbuzz"
    if input_integer % 5 == 0:
        return "buzz"
    if input_integer % 3 == 0:
        return "fizz"
    return str(input_integer)


if __name__ == "__main__":
    for i in range(100):
        print(str(i), ": ", fizzbuzz(i))
