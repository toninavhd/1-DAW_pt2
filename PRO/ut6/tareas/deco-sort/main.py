def sort(asc=True):
    def decorator(func):
        def wrapper(*args, **kwargs) -> list:
            sorted_elements = sorted(func(*args, **kwargs))
            if asc:
                return sorted_elements
            else:
                return sorted(sorted_elements, reverse=True)

        return wrapper

    return decorator

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
