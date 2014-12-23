from datetime import datetime

def log_file(error_text):
    """Creates or opens a file with the date of runtime and inserts the reported
       error, with one new line per error."""
    
    file_name = datetime.today().strftime("%Y%m%d") + "ErrorLog.txt"
    with open(file_name, "a+") as error_log_file:
        error_log_file.write(error_text + "\n")
