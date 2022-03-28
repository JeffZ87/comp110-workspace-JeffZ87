"""Dictionary related utility functions."""

from csv import DictReader

__author__ = "730480180"

# helper functions


def read_csv_rows(file_path: str) -> list[dict[str, str]]:
    """Read a CSV file into a row orientated table"""
    result: list[dict[str, str]] = []
    file_handler = open(file_path, "r", encoding="utf8")
    csv_reader = DictReader(file_handler)
    for row in csv_reader:
        result.append(row)

    file_handler.close()
    return result


def column_value(row_data: list[dict[str, str]], col_header: str) -> list[str]:
    """Return a list of values of identified column from a row orientated data."""
    result: list[str] = []
    for row in row_data:
        result.append(row[col_header])

    return result


def columnar(row_data: list[dict[str, str]]) -> dict[str, list[str]]:
    """Convert row orientated data into column orientated data."""
    result: dict[str, list[str]] = {}
    for col_key in row_data[0]:
        result[col_key] = column_value(row_data, col_key)

    return result


def head(col_data: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Return the first [num] rows of data passed in."""
    result: dict[str, list[str]] = {}
    for col_key in col_data:
        row_data: list[str] = []
        max_rows: int = len(col_data[col_key])
        num_row: int = 0 
        if max_rows < num:
            num_row = max_rows
        else:
            num_row = num      

        # append [num] row from data table to a list object 
        i: int = 0
        while i < num_row:
            row_data.append(col_data[col_key][i])
            i += 1

        result[col_key] = row_data

    return result


def select(column_orientated_data: dict[str, list[str]], selected_column_list: list[str]) -> dict[str, list[str]]:
    """Filters original data to return selected column orientated data from a list of column name."""
    result: dict[str, list[str]] = {}
    for selected_column in selected_column_list:
        result[selected_column] = column_orientated_data[selected_column]  # create an element in selected column with the list of data associated with the key

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

# utility function


def previous_experience(col_data: dict[str, list[str]]) -> dict[str, int]:
    """Collects data about student's previous coding experience."""
    result: dict[str, int] = {}
    # possible_response: list[str] = ["None to less than one month!", "2-6 months", "7-12 months", "1-2 years", "Over 2 years"]
    # print(select(col_data, ["prior_exp"])["prior_exp"])
    unordered_table: dict[str, int] = count(select(col_data, ["prior_exp"])["prior_exp"])
    result = order_data(unordered_table, ["None to less than one month!", "2-6 months", "7-12 months", "1-2 years", "Over 2 years"])
    return result


def order_data(unordered_data: dict[str, int], expected_order: list[str]) -> dict[str, int]:
    """Order [unordered_data] as specified by the [expected_order]."""
    result: dict[str, int] = {}
    for item in expected_order:
        result[item] = 0

    for key in unordered_data:
        result[key] = unordered_data[key]

    return result


def filter_data(unfiltered_data: dict[str, list[str]], filter: dict[str, list[str]]) -> dict[str, list[str]]:
    """Removed all data that does not match with the filter keys & values."""
    result: dict[str, list[str]] = {}
    for key in filter:
        temp: list[str] = []
        if key in unfiltered_data:
            for item in filter[key]:
                for item2 in unfiltered_data[key]:
                    if item == item2:
                        temp.append(item)

            if len(temp) > 0:
                result[key] = temp

    return result


