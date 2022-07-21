
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

def first_line():
    do_twice(plus_minus_space)
    plus()

def second_line():
    do_twice(slash_space)
    slash()

def grid():
    first_line()
    do_four(second_line)

def draw_grid():
    do_twice(grid)
    first_line()


draw_grid()