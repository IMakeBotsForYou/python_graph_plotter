from math import *
# Graph size
SIZE = 20
xSize = SIZE * 3
ySize = SIZE
graphs = []
top_y = []
bottom_y = []
right_x = []
left_x = []
ch_list = []
unit_list = []


def cramp(x, max, min):
    if x > max:
        return max
    elif x < min:
        return min
    else:
        return x

def get_fx():
    print("Editor's note: To do powers, you can do either x * x, xx, pow(x, 2), or x**2")
    print("Available functions: cos, sin, tan, sqrt, pow")
    print("If you use trigo functions, recommended scaling: off")
    amount = int(input("How many graphs do you want?  "))
    for gr_n in range(amount):
        graphs.append(input(f'Input #{gr_n}. f(x) = '))
        custom_range = input("Custom range? y/n  ")
        if custom_range == 'y':
            top_y.append(cramp(int(input("Input top of range = ")), SIZE, -SIZE))
            bottom_y.append(cramp(int(input("Input top of range = ")), SIZE, -SIZE))
            left_x.append(cramp(int(input("Input left of range = ")), SIZE, -SIZE))
            right_x.append(cramp(int(input("Input right of range = ")), SIZE, -SIZE))
        else:
            top_y.append(ySize)
            bottom_y.append(-ySize)
            right_x.append(xSize)
            left_x.append(-xSize)
        ch_list.append(input("Char for current graph: "))
        unit_list.append(input("Use scaling for this: y/n "))


# Relative Unit
rel_unit = 1
###
# IDEA: Idea for relative unit concept given by Ron Fefer .
###

# All occurrences of X in the function
temp = ""
func = ""


def make_temp(fx):
    global temp
    temp = fx.replace(" ", "")


def findOccurrences(ch):
    return [i for i, symbol in enumerate(temp) if symbol == ch]


# Every time x is mentioned in the function
# Make a list, so we can fix thigns like 5x -> 5 * x
xlist = []


###make_temp(func)
def make_x_list():
    global xlist
    xlist = findOccurrences('x')


###make_x_list()func
# Is there nothing before the x? (e.g.   cos(x) -> true   5x -> false)
# This way, replacing x with * x later on causes no problems, as its 1 * x
def standAloneX(i):
    global temp
    if i > 0 and not ("" + temp[i - 1]).isalnum():
        return temp[:i] + "(1x)" + temp[i + 1:]
    else:
        return temp


def insert(st, i, ch):
    return st[:i] + ch + st[i:]


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
            '''
    # 5cos(x) => 5 * cos(1 * x)
    # if (len(xlist) > 0):
    #     if xlist[0] == 0:
    #         temp = "1{0}".format(temp)
    #         xlist.pop(0)
    # xlist = findOccurrences('x')
    # while len(xlist) > 0:
    #     # update list
    #     i = xlist[-1]
    #     temp = standAloneX(i)
    #     del xlist[-1]
'''
    return fx.replace("x", "(x)")


# Initialize axis
# fix_function(func)
xvalues = list(range(-xSize, xSize + 1))
'''
# xvalues = np.arange(-xSize, xSize+1, 1.0)
# yvalues = [eval(func.replace("x", str(x))) for x in xvalues]

###print(f'Plotting: f(x) = {save}')'
'''
# Calculate y values, and for x that fall out of arange
# set value to 0, to not change scale of graph.
yvalues = []


def calc_function(fx):
    global yvalues, xvalues
    yvalues = []
    for x in xvalues:
        try:
            yvalues.append(round(eval(fx.replace("x", str(x)))))
        except:
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
    print("Scale: " + str(rel_unit) + ":1")


# linear()
# If not, calculate scale.

'''
(max(yvalues[xSize + left_x[g]:right_x[g] + xSize]),
                        min(yvalues[xSize + left_x[g]:right_x[g] + xSize]))
'''


def need_unit_check():
    global need_unit, xSize, yvalues, left_x, right_x, ySize, g, rel_unit
    if need_unit:
        (maxY, minY) = (max(yvalues),
                        min(yvalues))
        if maxY > abs(minY):
            rel_unit = maxY / ySize
        else:
            rel_unit = abs(minY) / ySize
        fix_y_values()
    print("Scale: " + str(rel_unit) + ":1")


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
    global graph
    for y in range(ySize, -ySize - 1, -1):
        for x in range(-xSize, xSize + 1):
            if x == 0:
                graph += '|'  # Y axis
            elif y == 0:
                graph += '-'  # X axis
            else:
                graph += ' '  # Not axis
        graph += '\n'  # End of line


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
def draw(index, char):
    global graph
    return graph[:index] + char + graph[index + len(char):]


def fill_graph(ch):
    global graph
    global temp
    for y in range(top_y[g], bottom_y[g] - 1, -1):  # Top->bottom
        for x in range(left_x[g], right_x[g] + 1):  # Left->Right
            if yvalues[x + xSize] == y:  # If yvalues has current value at current x
                graph = draw(translate(x, y), ch)  # Draw the point

# Show how big the graph really is
def add_graph_numbers():
    global graph
    graph = draw(translate(-2, 0), '(0,0)')
    graph = draw(translate(-len(f'({round(ySize * rel_unit)},0)') // 2 + 1, ySize), f'(0,{round(ySize * rel_unit)})')
    graph = draw(translate(-len(f'({round(ySize * rel_unit)},0)') // 2 + 1, -ySize), f'(0,{round(-ySize * rel_unit)})')
    graph = draw(translate(xSize - len(f'(0,{round(xSize * rel_unit)})') + 1, 0), f'(0,{round(xSize * rel_unit)})')
    graph = draw(translate(-xSize, 0), f'(0,{round(-xSize * rel_unit)})')


draw_axis()


def make_full_function(fx, ch):
    global yvalues, need_unit
    fix_function(fx)
    make_temp(fx)
    make_x_list()
    func = fix_function(fx)
    print("Plotting: " + func)
    calc_function(func)
    linear()
    if unit_list[g] == 'y':
        need_unit_check()
    fill_graph(ch)
    # add_graph_numbers()


# Draw graph
# draw_axis()
# fill_graph()
# add_graph_numbers()
get_fx()
for g in range(len(graphs)):
    make_full_function(graphs[g], ch_list[g])
add_graph_numbers()
# Draw another functions

print(graph)
# Editor's notes;
print("Footnote: Any values that fall out of range are represented with a 0.")
print("Of course, a x = 0 value doesn't always mean an error.")
