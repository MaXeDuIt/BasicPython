
def do_twice(func):
    func()
    func()

def do_four(func):
    do_twice(func)
    do_twice(func)

def plus_minus_space():
    print('+ - - - -', end=' ')

def plus():
    print('+')

def slash_space():
    print('|        ', end=' ')

def slash():
    print('|')

def first_line_by2():
    do_twice(plus_minus_space)
    plus()

def second_line_by2():
    do_twice(slash_space)
    slash()

def grid_by2():
    first_line_by2()
    do_four(second_line_by2)

def draw_grid_by2():
    do_twice(grid_by2)
    first_line_by2()

def first_line_by4():
    do_four(plus_minus_space)
    plus()

def second_line_by4():
    do_four(slash_space)
    slash()

def grid_by4():
    first_line_by4()
    do_four(second_line_by4)

def draw_grid_by4():
    do_four(grid_by4)
    first_line_by4()


draw_grid_by2()
draw_grid_by4()