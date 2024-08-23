"""
# unpacking

a, b, *nums = 1, 2, 3, 4, 5

# *args -> tuple

def add(x, y, *rest):
    return x+y+sum(rest)

print(add(a, b, *nums))

"""
"""
# make a function in python to check in which quadrant my line forms

def get_quadrant(x, y):
        if x > 0 and y > 0:
            return "Quadrant 1"
        elif x < 0 and y > 0:
            return "Quadrant 2"
        elif x < 0 and y < 0:
            return "Quadrant 3"
        elif x > 0 and y < 0:
            return "Quadrant 4"
        elif x == 0 and y != 0:
            return "On Y-axis"
        elif y == 0 and x != 0:
            return "On X-axis"
        else:
            return "Origin"

def find_quadrant(*points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    # print(x1, x2, y1, y2)

    q1 = get_quadrant(x1, y1)
    q2 = get_quadrant(x2, y2)

    quadrants = set([q1, q2])

    print(q1, q2)

    if len(quadrants) == 1:
        return f"The line lies entirely in {q1}."
    else:
        return f"The line crosses multiple regions: {', '.join(quadrants)}."

# Example usage:
p1 = (2, 3)
p2 = (-1, -4)

result = find_quadrant(p1, p2)
print(result)
"""

# def add(x, y, *args, z):
#     print(x + y + sum(args) + z)

# add(1, 2, 3, 4, 5, 6, 7, 8, 9, z=10)


########################################################
# **kwargs -> keyword arguments

# def connect(**connection_info):
#     print(type(connection_info))
#     print(connection_info)

# connect(server='localhost', port=8080, user='admin', password='root')

# config = {'server':'localhost', 'port':8080, 'user':'admin', 'password':'root'}

# connect(**config)
# connect(connection_info=[1, 2, 3])

########################################################
# type hint

def say_hi(name: str) -> str:
    return f"Hi {name}"

print(say_hi(123))