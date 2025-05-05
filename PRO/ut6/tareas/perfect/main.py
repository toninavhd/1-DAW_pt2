def find_divisors(n: int):
    divisors = []
    for num in range(1, n):
        if n % num == 0:
            divisors.append(num)
    return divisors


def is_perfect(n: int) -> bool:
    divisors = find_divisors(n)
    perfect_n = True
    if sum(divisors) != n:
        perfect_n = False
    return perfect_n


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_perfect)
