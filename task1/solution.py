def strict(func):
    def wrapper(*args):
        annotations = func.__annotations__
        param_names = [name for name in annotations if name != "return"]

        if len(args) != len(param_names):
            raise TypeError(f"{func.__name__}() ожидает {len(param_names)} аргумента")

        for i in range(len(args)):
            expected_type = annotations[param_names[i]]
            if not isinstance(args[i], expected_type):
                raise TypeError(
                    f"Аргумент '{param_names[i]}' должен быть типа {expected_type.__name__}"
                )

        return func(*args)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# test
if __name__ == "__main__":
    print(sum_two(1, 2))  # OK
    print(sum_two(1, 2.4))  # error
    print(sum_two(1))  # error
    print(sum_two(1, 2, 3))  # error
    print(sum_two())  # error
    print(sum_two('1', '2'))  # error
    print(sum_two(1.2, 2))  # error
