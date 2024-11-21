def run(u: list, v: list) -> float | None:
    u_length = len(u)
    v_length = len (v)
    dprod = None
    
    if u_length == v_length:
        dprod = 0
        for umul, vmul in zip(u,v):
            dprod += umul * vmul
            
    return dprod


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
