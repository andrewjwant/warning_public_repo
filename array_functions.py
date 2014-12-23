from numpy import loadtxt, ndarray, where
from datetime import datetime
from log_error_file import log_file

def col_index_header(search_term,
                     array_name):
    """Returns the column index of the specified search term in the given 
       array. Writes a statement to the log file if no array is present"""
    if type(array_name) == ndarray:
        return list(array_name[0, :]).index(search_term)
    else:
        log_file("{0} array not present".format(array_name))
