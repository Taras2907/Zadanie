from functools import wraps
from csv import DictReader


def csv_reader(filename=None):

    if filename is None:
        raise AttributeError("File name is obligatory argument")

    def csv_reader_decorator(func):
        wraps(func)

        def wrapper(*args, **kwargs):

            try:
                with open(filename) as f:
                    row_data = DictReader(f)
                    data = [{k: v for k, v in row.items()} for row in row_data]
                    return func(*args, data=data, **kwargs)
            except FileNotFoundError:
                print(f'file {filename} is not found please check is the path correct')

        return wrapper

    return csv_reader_decorator


