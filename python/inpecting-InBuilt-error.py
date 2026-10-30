import inspect, builtins


def show_tree(base, level=0, max_depth=1):
    if level > max_depth:
        return
    for name, obj in vars(builtins).items():
        if inspect.isclass(obj) and issubclass(obj, base) and obj is not base:
            print("\t" * level + f"- {name}")
            show_tree(obj, level + 1, max_depth)


show_tree(Exception, max_depth=1)