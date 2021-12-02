# EXAMPlES FPOM: https://realpython.com/python-thinking-recursively/

# n! = n x (n−1)!
# n! = n x (n−1) x (n−2)!
# n! = n x (n−1) x (n−2) x (n−3)!
# ⋅
# ⋅
# n! = n x (n−1) x (n−2) x (n−3) ⋅⋅⋅⋅x 3!
# n! = n x (n−1) x (n−2) x (n−3) ⋅⋅⋅⋅ x 3 x 2!
# n! = n x (n−1) x (n−2) x (n−3) ⋅⋅⋅⋅ x 3 x 2 x 1!


def n_factorial(sum, n):
    if n == 1:
        print(sum)
    else:
        sum = sum * n
        n_factorial(sum, n - 1)


def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)


def sum_of_digits(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_digits(n - 1)


def list_sum_recursive(input_list):
    if len(input_list) == 0:
        return 0
    else:
        return input_list[0] + list_sum_recursive(input_list[1:])


# 1, 1, 2, 3, 5, 8, 11, 18, 29
def fibonacci_recursive(n):

    lista = [0] * 10

    for i in range(n):
        if i == 0:
            lista[i] = 1
        elif i == 1:
            lista[i] = 2
        else:
            lista[i] = lista[i-2] + lista[i-1]
    return lista


def fibonacci_recursive(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)


if __name__ == '__main__':
    print(fibonacci_recursive(5))