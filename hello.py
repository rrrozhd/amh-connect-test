"""A tiny greeting module."""


def greet(name):
    """Return a greeting for ``name``, e.g. ``greet("world") == "Hello, world!"``."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("world"))
