import pandas as pd
import numpy as np

#create dataframe
df = pd.DataFrame(np.random.randn(100, 5), columns=['a', 'b', 'c', 'd', 'e'])

print(df)