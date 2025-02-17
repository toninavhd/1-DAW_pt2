def sort(asc=True):
    def decorator(func):
        def wrapper(*args, **kwargs) -> list:
            sorted_elements = sorted(func(*args, **kwargs))
            if asc:
                return sorted_elements
            else:
                return reversed(sorted_elements=True)
            return func(*args, **kwargs)

        return wrapper

    return decorator