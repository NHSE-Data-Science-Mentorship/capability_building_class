from typing import List


def list_to_sql_array(my_list: List) -> str:
    """
    Parameters
    ----------
    my_list: List
        python list
    Returns
    -------
        string: SQL array with elements of my_list

    This function takes a python list and returns a SQL array
    to easily make SQL queries with a condition like
        WHERE column_name IN ('a', 'b', 'c')
    from a python list ['a', 'b', 'c']
    """
    return f"""('{"', '".join(my_list)}')"""
