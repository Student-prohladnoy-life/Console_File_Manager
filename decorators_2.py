import sys
import os


def info_platform():
    print("System data", sys.platform, "(", os.name, ")")

def add_separators(info_platform):

    def inner(*args, **kwargs):

        print('#' * 24)
        print()
        result = info_platform()
        print()
        print('#' * 24)
        return result

    return inner

new_info_platform = add_separators(info_platform)


