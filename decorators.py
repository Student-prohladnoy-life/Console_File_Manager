


def info_developer():
    print("Student-prohladnoy-life")


def add_separators(info_developer):

    def inner(*args, **kwargs):

        print('>-<' * 10)
        print()
        result = info_developer()
        print()
        print('>-<' * 10)
        return result

    return inner

new_info_developer = add_separators(info_developer)
