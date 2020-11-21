from math import *

# Graph size
from typing import List

SIZE = 23
xSize = SIZE * 3
ySize = SIZE
graph = ""
bottom_y = -SIZE
top_y = SIZE
left_x = -xSize
right_x = xSize

max_x = 0
min_y = 0
min_x = 0
max_y = 0


# This function takes a value,
# and returns a value within the bounds
# of max and min.
# If the value is outside the bounds,
# it pushes it to the bound.
def cramp(v, max, min):
    if v > max:
        return max
    elif v < min:
        return min
    else:
        return v


# Relative Unit
rel_unit = 1
###
# IDEA: Idea for relative unit concept given by Ron Fefer .
###

# All occurrences of X in the function
temp = ""
func = ""


# Removes all spaces in the function
def make_temp(fx):
    global temp
    temp = fx.replace(" ", "")


# Finds all occurrences of x
def findOccurrences(ch):
    return [i for i, symbol in enumerate(temp) if symbol == ch]


# Every time x is mentioned in the function
# Make a list, so we can fix things like 5x -> 5 * x
xlist = []


# makes the list of occurrences
def make_x_list():
    global xlist
    xlist = findOccurrences('x')


# Insert char into str at index i
def insert(st, i, ch):
    return st[:i] + ch + st[i:]


# This parses the function string into
# a text the eval function can read.
def fix_function(fx):
    global xlist, temp, func
    # I found a smarter way :D
    for index in range(1, len(fx)):
        if fx[index] == "(" and fx[index - 1] == ")":
            fx = insert(fx, index, '*')
            index += 1
        elif (fx[index].isalpha() or fx[index] == "(") and fx[index - 1].isnumeric():
            fx = insert(fx, index, '*')
            index += 1
        elif fx[index].isnumeric() and fx[index - 1] == ")":
            fx = insert(fx, index, '*')
            index += 1
    return fx.replace("x", "(x)")


# Initialize axis
# fix_function(func)
xvalues = list(range(left_x, right_x + 1))

# Calculate y values, and for x that fall out of arange
# set value to 0, to not change scale of graph.
yvalues = []


# Eval every x in the range
# if error, enter 0
def calc_function(fx):
    global yvalues, xvalues
    for x in xvalues:
        try:
            yvalues.append(round(eval(fx.replace("x", str(x)))))
        except ZeroDivisionError:
            yvalues.append(0)
        except ValueError:
            yvalues.append(0)


# calc_function(func)
need_unit: bool = False


# Check if slope is equal at all points

def linear():
    global xSize, yvalues, need_unit, m

    # First of all, do we even need a relative scale?
    i = 0
    while yvalues[i] == 0 and i < len(yvalues) - 3:
        i += 1  # skip over dead area, if there is one.
        # Example of this is sqrt(x)

    # Calculate slope
    m = (yvalues[i + 2] - yvalues[i + 1]) / (xvalues[i + 1] - xvalues[i])  # (y1-y)/(x1-x)

    for index in range(1, xSize, 1):
        if yvalues[index] - yvalues[index - 1] != m:
            need_unit = True

# Unused

# If not, calculate scale.
def fix():
    global xSize, yvalues, ySize, rel_unit
    (maxY, minY) = (max(yvalues),
                    min(yvalues))
    if maxY > abs(minY):
        rel_unit = maxY / ySize
    else:
        rel_unit = abs(minY) / ySize
    fix_y_values()


# needUnit()
# Print the scale

# Translate y values to match scale
def fix_y_values():
    global yvalues
    global rel_unit
    yvalues = [round(y / rel_unit) for y in yvalues]


# fix_y_values()
graph = ""  # Initiate empty string for graph


# Draw x/y axis
def draw_axis():
    global graph, xvalues, yvalues
    for y in range(ySize, -ySize - 1, -1):
        for x_val in range(-xSize, xSize + 1):
            if min_x <= x_val <= max_x and min_y <= y <= max_y:
                if x_val == 0:
                    graph += "|"
                elif y == 0:
                    graph += "-"
                else:
                    graph += " "
            else:
                graph += " "
        graph += '\n'  # End of line'


# Bring coordinate system to 0, 0 of axis
# instead of top left corner
def centralize(x, y):
    x = x + xSize
    y = -y + ySize
    return x, y


# Translate (x,y) pair of coordinates
# into an index in the print string
def translate(x, y):
    (x, y) = centralize(x, y)
    return (xSize * 2 + 2) * y + x


# Replace at index
def draw(index: int, char: str) -> str:
    global graph
    return graph[:index] + char + graph[index + len(char):]


# Draw the line itself
def fill_graph(ch):
    global graph
    global temp
    for y in range(top_y, bottom_y - 1, -1):  # Top->bottom
        for x in range(left_x, right_x + 1):  # Left->Right
            if yvalues[x + xSize] == y:  # If yvalues has current value at current x
                graph = draw(translate(x, y), ch)  # Draw the point


# Simaniot (whats the word in English lol) markers?
def add_graph_numbers():
    global graph
    # fixes for if the graph is a single, straight horizontal line
    if int(abs(max_y // rel_unit - min_y // rel_unit) // 10) == 0:
        fix1 = -2
        fix2 = 2
    else:
        fix1 = 0
        fix2 = 0

    # y marks
    for v in range(int(min_y // rel_unit) + fix1, int(max_y // rel_unit - 1) + fix2, 5):
        if -ySize < v < -2 or ySize > v > 2 :
            graph = draw(translate(-len(f'({round(v)})') // 2 + 1, v), f'({round(v)})')

    left_numbers = min_x + len(f'{abs(min_x)}') + 6
    right_numbers = max_x - len(f'{max_x}') - 5
    amount = 6
    # x marks
    for v in range(left_numbers, right_numbers, abs(right_numbers - left_numbers) // amount):
        if v <= -7 or v >= 7:
            graph = draw(translate(v - len(f'({round(abs(v))})') // 2 + 1, 0), f'({round(abs(v))})')


print("Editor's note: To do powers, you can do either x * x, xx, pow(x, 2), or x**2")
print("Available functions: cos, sin, tan, sqrt, pow")
print("If you use trigo functions, recommended scaling: off")
c = True
a = "dd"
# Loop until valid function is given
# fix tomorrow.
while c:
    try:
        f = input(f'Input f(x) = ')
        make_temp(f)
        make_x_list()
        func = fix_function(f)
        a = round(eval(func.replace("x", '(1)')))
    except ZeroDivisionError:
        print("Asymptote")
        c = False
    except SyntaxError:
        print("Error parsing")
    except NameError:
        print("Error parsing")
    if isinstance(a, int):
        c = False

custom_range = input("Custom range? y/n  ")
if custom_range == 'y':
    top_y = cramp(int(input("Input top of range = ")), SIZE, -SIZE)
    bottom_y = cramp(int(input("Input top of range = ")), SIZE, -SIZE)
    left_x = cramp(int(input("Input left of range = ")), SIZE, -SIZE)
    right_x = cramp(int(input("Input right of range = ")), SIZE, -SIZE)
else:
    top_y = ySize
    bottom_y = -ySize
    right_x = xSize
    left_x = -xSize
make_temp(f)
make_x_list()
func = fix_function(f)

print("Plotting: " + func)
calc_function(func)

max_x, min_x, max_y, min_y = (max(xvalues), min(xvalues), max(yvalues), min(yvalues))
draw_axis()
scale_q = "n"

# think about how to fix this linear shit 2morrow

if not linear() and (max_y > ySize or min_y < -ySize):
    scale_q = 'y'
if scale_q == 'y':
    fix()
ch = input("What character to draw the graph with? ")
while len(ch) > 1:
    print("Input invalid, must be only 1 char.")
    ch = input("What character to draw the graph with? ")
print("Scale: " + str(rel_unit) + ":1")
fill_graph(ch)
add_graph_numbers()
# Draw another functions

print(graph)
# Editor's notes;
print("Footnote: Any values that fall out of range are represented with a 0.")
print("Of course, a x = 0 value doesn't always mean an error.")
print("Also, the markers on the graph represent the x/y values without scaling")
print("since with scaling, they would be too large to fit sometimes.")
