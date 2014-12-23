from numpy import ndarray, loadtxt, where
from datetime import datetime

data_list = loadtxt(r"sample_array.csv",
                    dtype="S32",
                    delimiter=","
                   )
class Sample(object):
    
    def __init__(self, 
                 name, 
                 data=None, 
                 comment=False, 
                 sample_datetime=None):
        
        self.name = name
        self.data = data
        self.comment = comment
    
    def get_datetime(self):
        pass
        


sample_dictionary = {}

for index, sample_id in enumerate(data_list[:, 0]):
    if len(sample_id) != 0:
        sample_dictionary[sample_id[-6:]] = Sample(sample_id, 
                                                   data_list[index, 1:].astype(float))
        
    else:
        pass
        
