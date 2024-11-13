def run():
    str_num = '1'
    rep_num = 1
    limit = 9

    for _ in range(limit):
        mul_factors = int(str_num * rep_num)
        result = mul_factors * mul_factors

        print(result)
        rep_num += 1

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
