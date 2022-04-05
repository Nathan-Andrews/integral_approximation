from math import pi, sin, cos, sqrt

#enter the values for n, a and b here
n = 4
a = 0
b = sqrt(pi / 2)


def function(x):
    """computes the value of the function f(x) at a value x"""
    # enter the function you want to integrate in the return statement
    try:
        return sin(x ** 3)
    except ZeroDivisionError:
        print("division by zero!")
        return 0
    except:
        print("Invalid function")
        return 0


def find_input(n, a, b):
    """Returns an n-number of values between a and b as a list"""
    j = (b - a) / n
    l = []
    for i in range(n + 1):
        l.append(a + i * j)
    #print(l)
    return l

def trapezoidal_rule(n, a, b):
    """Estimates the value of an integral using the trapezoidal rule"""

    x_values = find_input(n, a, b)
    l = []
    k = 0
    for i in x_values:
        fx = function(i)

        l.append(fx)

        if (i == a) or (i == b):
            k += fx
        else:
            k += 2 * fx
    return round((b-a) * k / (2 * n), 4)


def simpsons_rule(n, a, b):
    """Estimates the value of an integral using the trapezoidal rule"""

    x_values = find_input(n, a, b)
    l = []
    k = 0
    for i in range(len(x_values)):
        x = x_values[i]
        fx = function(x)

        l.append(fx)

        if (x == a) or (x == b):
            k += fx
        elif (i % 2) == 0:
            k += 2 * fx
        else:
            k += 4 * fx
    return round((b-a) * k / (3 * n), 4)


print("{} by trapezoidal rule".format(trapezoidal_rule(n, a, b)))

print("{} by simpsons rule".format(simpsons_rule(n, a, b)))