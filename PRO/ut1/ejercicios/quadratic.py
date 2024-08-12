# *************************
# ECUACIÓN DE SEGUNDO GRADO
# *************************


def run(a: int, b: int, c: int) -> tuple:

    discriminant = (b**2 - 4*a*c)
    quadratic_discriminant = discriminant**0.5
    
    x1 = (-b + quadratic_discriminant) / (2*a)
    x2 = (-b - quadratic_discriminant) / (2*a)

    return x1, x2


if __name__ == '__main__':
    run(4, -6, 2)