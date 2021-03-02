# alix, 3/1/21
from melons import melons
def print_melon(melons):
    """Print each melon with corresponding attribute information."""

    for melon_name, attributes in melons.items():
        print(melon_name.upper())
        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

print(print_melon(melons))


