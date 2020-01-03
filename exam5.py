# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(P)


# %%
# X coordination shifting
#s = np.array([[0,0], [0,0], [0,0]])
P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s = np.full((3, 2), 0)
P[:, 0:2] = s
print(P)


# %%
# Y coordination shifting
#s = np.array([[0, 0, 0], [0, 0, 0]])
P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s = np.full((2, 3), 0)
P[0:2, :] = s
print(P)


# %%
# -X coordination shifting
#s = np.array([[0,0], [0,0], [0,0]])
P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s = np.full((3, 2), 0)
P[:, -2:] = s
print(P)


# %%
# -Y coordination shifting
#s = np.array([[0, 0, 0], [0, 0, 0]])
P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s = np.full((2, 3), 0)
P[-2:, :] = s
print(P)


# %%


