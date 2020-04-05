# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

base =pd.read_csv('iris.csv')

amostra = np.random.choice(a = [0,1],size =150, replace = True,p=[0.5,0.5])

len(amostra[amostra == 1])


