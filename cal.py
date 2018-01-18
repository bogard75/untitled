import pandas as pd
import numpy as np


sss = pd.DataFrame(np.random.randn(100, 4), columns=['A','B','C','D'])
sss.groupby(sss.A.round(1)).size().plot()

sss.A.round(1)