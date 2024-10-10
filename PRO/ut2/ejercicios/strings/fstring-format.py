def run(number):
    print(
        f'{number:.3f}'
        '\n'
        f'{number:.6f}'
        '\n'
        f'{number:8.2f}'
        '\n'
        f'{number:6e}'
        '\n'
        f'{number:010.4f}'
        '\n'
        f'{number:19.5f}'
    )
    


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
