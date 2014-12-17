from numpy import loadtxt

def import_array(file_type):    
    new_filename = raw_input("Insert {0} filepath here: ".format(file_type))
    try:
        if new_filename.endswith(".csv"):
            imported_array = loadtxt(new_filename,
                                    dtype="S32",
                                    delimiter=","
                                    )
            return imported_array
        else:
            log_file("{0} file not found".format(file_type))
    except:
        log_file("{0} file not found".format(file_type))           

