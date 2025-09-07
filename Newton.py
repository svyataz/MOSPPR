import numpy as np
import builtins

original_print = print

def custom_print(*args, **kwargs):
    kwargs.setdefault("sep", "")
    kwargs.setdefault("end", "")
    original_print(*args, **kwargs)

builtins.print = custom_print

class fast_grad:

    def __init__(self, start_points, e):
        self.start_points = start_points
        self.e = e

    @staticmethod
    def f2(x):
        return 3 * x[0] ** 2 - 3 * x[0] * x[1] + 4 * x[1] ** 2 - 2 * x[0] + x[1]

    def derivative_1(self, x, i):
        temp_x = x.copy()
        temp_x[i] += self.e
        return (fast_grad.f2(temp_x)
                - fast_grad.f2(x)) / self.e

    def derivative_2(self, x, i):
        temp_x = x.copy()
        temp_x[i] += self.e
        u1 = fast_grad.f2(temp_x)
        temp_x[i] -= self.e
        u2 = fast_grad.f2(temp_x)
        temp_x[i] -= self.e
        u3 = fast_grad.f2(temp_x)
        return (u1 - 2  * u2 + u3) / (self.e ** 2)

    def derivative_mix(self, x):
        u2_x, u3_x, u4_x = x.copy(), x.copy(), x.copy()
        u2_x[0] -= self.e
        u3_x[1] -= self.e
        u4_x[0] -= self.e
        u4_x[1] -= self.e
        u1 = fast_grad.f2(x)
        u2 = fast_grad.f2(u2_x)
        u3 = fast_grad.f2(u3_x)
        u4 = fast_grad.f2(u4_x)
        return (u1 - u2 - u3 + u4) / (self.e ** 2)

    def main(self):

        k = 1
        x = self.start_points
        curr_grad = np.array([self.derivative_1(x, 0),
                              self.derivative_1(x, 1)])

        while np.linalg.norm(curr_grad) >= self.e:
            print(f"\n\033[3mИТЕРАЦИЯ {k}\n\n\033[0m*")
            print(f"Базисный вектор:\n{x[0]:.4f}\t\t\t{x[1]:.4f}\n")
            print(f"численное значение Базисного вектора:"
                  f"\n{fast_grad.f2(x):.4f}\n")
            print(f"Координаты вектора градиента:"
                  f"\n{curr_grad[0]:.4f}\t\t\t{curr_grad[1]:.4f}\n")
            print(f"Значение норма вектора:"
                  f"\n{np.linalg.norm(curr_grad):.4f}\n")
            H = np.array([[self.derivative_2(x, 0), self.derivative_mix(x)],
                         [self.derivative_mix(x), self.derivative_2(x,1)]])
            if np.all(np.linalg.eigvals(H) > 0):
                x -= np.linalg.inv(H) @ curr_grad
            else:
                p = - curr_grad
                h = (np.dot(curr_grad, p) /
                    np.dot(p, np.dot(p, H)))
                x -= h * curr_grad
                print(f"Новый шаг:"
                      f"\n{h:.4f}\n")
            print(f"Координаты нового вектора:\n{x[0]:.4f}\t\t\t{x[1]:.4f}\n")
            print(f"численное значениеБазисного вектора:"
                f"\n{fast_grad.f2(x):.4f}\n")
            k += 1
            curr_grad = np.array([self.derivative_1(x, 0),
                                  self.derivative_1(x, 1)])

HJ_ob = fast_grad([2,2],0.0001)
HJ_ob.main()
