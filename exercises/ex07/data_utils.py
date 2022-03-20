"""Dictionary related utility functions."""

from csv import DictReader

__author__ = "730480180"

# Define your functions below


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Read a CSV file into a row orientated table."""
    result: list[dict[str, str]] = []
    file_handle = open(path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()
    return result


def column_values(row_orientated_data: list[dict[str, str]], col_key: str) -> list[str]:
    """Return a list of values of identified column from a row orientated data."""
    result: list[str] = []
    
    for row in row_orientated_data:
        result.append(row[col_key])
    
    return result


def columnar(row_orientated_data: list[dict[str, str]]) -> dict[str, list[str]]:
    """Convert row orientated data into column orientated data."""
    result: dict[str, list[str]] = {}

    for column_key in row_orientated_data[0]:
        result[column_key] = column_values(row_orientated_data, column_key)
        
    return result


def head(column_orientated_data: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Return the first [num] rows of data passed in."""
    result: dict[str, list[str]] = {}

    for column_key in column_orientated_data:
        row_data: list[str] = []
        num_of_rows: int = len(column_orientated_data[column_key])

        if num_of_rows < num:
            num = num_of_rows  # if the number of rows in argument is greater than row in data, [num] will be the total number of rows in data
        
        i: int = 0

        # append [num] row from data table to a list object 
        while i < num:
            row_data.append(column_orientated_data[column_key][i])
            i += 1

        result[column_key] = row_data

    return result


def select(column_orientated_data: dict[str, list[str]], selected_column_list: list[str]) -> dict[str, list[str]]:
    """Filters original data to return selected column orientated data from a list of column name."""
    result: dict[str, list[str]] = {}

    for selected_column in selected_column_list:
        result[selected_column] = column_orientated_data[selected_column]  # create an element in selected column with the list of data associated with the key

    return result


def concat(column_orientated_data1: dict[str, list[str]], column_orientated_data2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column based data from two different column orientated data tables combined."""
    result: dict[str, list[str]] = {}

    # populate [result] with data1
    for column in column_orientated_data1:
        temp_col_list: list[str] = []
        
        for item in column_orientated_data1[column]:  # populate new list object of column values; 
            temp_col_list.append(item)

        result[column] = temp_col_list  # this avoid changed the same list linked

    for column in column_orientated_data2:
        if column in column_orientated_data1.keys():  # check if column key is exist in data1
            result[column] += column_orientated_data2[column]
        else:
            result[column] = column_orientated_data2[column]

    return result


def count(data_list: list[str]) -> dict[str, int]:
    """Given a `list[str]`, this function will produce a `dict[str, int]` where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}

    for item in data_list:
        if item in result:
            result[item] += 1  # if item already exist, increment the count by 1
        else:
            result[item] = 1  # else create a new element in dict and initialize count to 1

    return result