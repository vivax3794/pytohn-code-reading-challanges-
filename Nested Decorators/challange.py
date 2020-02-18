print("[1] defining decorator_one")


def decorator_one(func):
    print("[2] decorator_one body")

    def decorator_one_inner(function):
        print("[3] decorator_one_inner body")

        def decorator_one_inner_inner(*args, **kwargs):
            print("[4] decorator_one_inner_inner body")
            return func(function, *args, **kwargs)

        print("[5] decorator_one_inner returning")
        return decorator_one_inner_inner

    print("[6] decorator_one returning")
    return decorator_one_inner


print("[7] defining decorator_two")


@decorator_one
def decorator_two(function, *args, **kwargs):
    print("[8] decorator_two body")
    return function(*args, **kwargs)


print("[9] defining function_one")


@decorator_two
def function_one():
    print("[10] function_one body")


print("[11] running function_one")
function_one()
print("[12] done")