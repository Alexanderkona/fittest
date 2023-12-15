import numpy as np
import matplotlib.pyplot as plt

# Создаем ряды данных X и Y
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 3, 5, 4, 6])

# Функция для вычисления среднего значения
def mean(data):
    return sum(data) / len(data)

# Найдем средние значения X и Y
mean_X = mean(X)
mean_Y = mean(Y)

# Найдем ковариацию и дисперсию
cov_xy = np.mean(X*Y) - mean_X * mean_Y
var_x = np.mean(X**2) - mean_X**2

# Вычисляем коэффициенты линейной регрессии
beta = cov_xy / var_x
alpha = mean_Y - beta * mean_X

# Печатаем коэффициенты
print("Коэффициент наклона (beta):", beta)
print("Коэффициент пересечения (alpha):", alpha)

# Строим график регрессии
plt.scatter(X, Y, color='blue') # рассеяние данных
plt.plot(X, alpha + beta*X, color='red') # линия регрессии
plt.title('Линейная регрессия')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
