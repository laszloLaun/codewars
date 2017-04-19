def build_string(*args):
    print("I like {0}!".format(", ".join(args)))
    return "I like {0}!".format(", ".join(args))

build_string("Lacus", "Angi")
