from numpy import loadtxt, where
from error_log_file import log_file

%pwd "Insert pathname here"

class FileObject(object):
    
    def __init__(self,
                 name, 
                 content=None):
        self.name = name
        self.content = content
                 
    def add_content(self):
        if self.content is None:
            array_to_import = raw_input("Insert {0} filepath here: ".format(self.name))
            if array_to_import.endswith(".csv"):
                self.content = loadtxt(array_to_import,
                                       dtype="S32",
                                       delimiter=","
                                      )
            else:
                log_file("{0} file not found".format(self.name))
        else:
            log_file("{0} file already has content".format(self.name)) 

class SampleObject(object):
    
    def __init__(self,
                 bc=None,
                 d=None,
                 sn=None,
                 p_time_d_h_m=None,
                 p_datetime=None
                ):
        
        self.bc = bc
        self.d = d
        self.sn = sn
        self.p_time_d_h_m = p_time_d_h_m
        self.p_datetime

    def add_d(self):
        pass
    
    def add_sn(self):
        pass
    
    def add_p_time_d_h_m(self):
        pass
        
    def add_p_datetime(self):
        pass
                                                    
        


file_list = [
            ]

file_dictionary = {}

for item in file_list:
    file_dictionary[item] = FileObject(item)

print file_dictionary.keys()

file_dictionary["file"].add_content()
