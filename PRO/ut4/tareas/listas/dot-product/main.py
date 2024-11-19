def run(u: list, v: list) -> float | None:
    u_length = len(u)
    v_length = len (v)
    dprod = 0

    if u_length == v_length:
        for umul, vmul in zip(u,v):
            dprod += umul * vmul
    else:
        dprod = None

    return dprod


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
