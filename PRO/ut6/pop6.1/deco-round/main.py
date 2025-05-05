def cround(ndecimals:int):
    def decorator(func):
        def wrapper(*args,**kwargs):
            return round(func(*args,**kwargs),ndecimals)
        return wrapper
    return decorator

def run(func, ndecimals, func_args, func_kwargs):
    return cround(ndecimals)(func)(*func_args, **func_kwargs)

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
