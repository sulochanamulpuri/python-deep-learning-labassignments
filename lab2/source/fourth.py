from random import randint
import numpy as np
Z = np.random.randint(0,25, size=(15))
print("Original array: %s"   %Z)
print("Most Frequent item in the list:")
print(np.bincount(Z).argmax())
