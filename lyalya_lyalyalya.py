import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Целевая функция
def f2(x1, x2):
    return 3*x1**2 - 3*x1*x2 + 4*x2**2 - 2*x1 + x2

def f8(x1, x2):
    return x1**2 - 2*x1*x2 + 6*x2**2 + x1 + x2
# Диапазон значений
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)
Z = f2(X, Y)

# Создание фигуры
fig = plt.figure(figsize=(10, 6))

# 3D-график
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none", alpha=0.8)

# Подписи
ax.set_title("Целевая функция")
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("f(x1, x2)")
ax.legend()

plt.show()
