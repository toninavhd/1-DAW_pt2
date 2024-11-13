def run(limit: int) -> None:
    result = 0
    
    for multiple_of_3 in range(0, limit, 3):
        if result >= limit:
            break
        print(multiple_of_3, end=' ')
        result += multiple_of_3
        

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
