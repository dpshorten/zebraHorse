import numpy as np
import matplotlib.pyplot as plt
import pickle

f = open("df_f.pkl", "rb")
df_f = pickle.load(f)

plt.plot(df_f[0])
plt.show()
