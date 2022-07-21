
def print_twice(value):
    print(value)
    print(value)

def do_twice(func, value):
    func(value)
    func(value)

def print_spam(value):
    print(value)

def do_four(func, value):
    do_twice(func, value)
    do_twice(func, value)

# do_twice(func=print_spam, value='спам')
do_twice(func=print, value='spam')
do_four(func=print, value='спам')