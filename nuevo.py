python -m pip install \
  --upgrade \
  --pre \
  --index-url https://pypi.anaconda.org/scipy-wheels-nightly/simple \
  --extra-index-url https://pypi.org/simple \
  matplotlib
    
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar([1, 2, 3], [3, 2, 1])
plt.show()
