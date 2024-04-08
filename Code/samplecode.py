import pandas as pd
import numpy as np

#create dataframe
df = pd.DataFrame(np.random.randn(100, 6), columns=['a', 'b', 'c', 'd', 'e','f'])

print(df)