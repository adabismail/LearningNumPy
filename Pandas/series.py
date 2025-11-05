import pandas as pd
import numpy as np

#series is 1d labeled array, 
series_list = [1,2,3]
series_array = np.array([1,2,3])
seires_dict = {'a':10,'b':20, 'c':30}
labels = ["a", "b", "c"]

series1 = pd.Series(series_list, index=labels)
series2 = pd.Series(series_array)
series3= pd.Series(seires_dict)
print(f"{series1}, \n\n{series2} \n\n{series3}")


