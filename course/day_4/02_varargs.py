def mean(first, *more_value):
    """Returns the mean value of the argument list"""
    return (first + sum(more_value)) / (1 + len(more_value))


list = [1, 2, 3, 4, 5, 6, 7]
print(f'Mean {list} → {mean(*list)}')
