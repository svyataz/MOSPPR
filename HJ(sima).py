import builtins

original_print = print

def custom_print(*args, **kwargs):
    kwargs.setdefault("sep", "")
    kwargs.setdefault("end", "")
    original_print(*args, **kwargs)

builtins.print = custom_print

class HJ:
    def __init__(self, start_points, h, d, m, e):
        self.start_points = start_points
        self.h = h
        self.d = d
        self.m = m
        self.e = e

    @staticmethod
    def f2(x1, x2):
        return 3 * x1 ** 2 - 3 * x1 * x2 + 4 * x2 ** 2 - 2 * x1 + x2

    def main(self):
        base = self.start_points
        i = 0
        while self.h >= self.e:
            print(f"\n\033[3mИТЕРАЦИЯ {i}\n\n\033[0m*")
            x = base.copy()
            f0 = HJ.f2(*x)
            print(f"Базисный вектор:\n{x[0]:.4f}\t\t\t{x[1]:.4f}\n")
            print(f"численное значениеБазисного вектора:"
                   f"\n{f0:.4f}\n")
            for j in range(2):
                x[j] += self.h
                print(f"Вектор при положительном шаге:\n{x[0]:.4f}\t\t\t{x[1]:.4f}\n")
                print(f"Значение вектора при положительном шаге:"
                        f"\n{HJ.f2(*x):.4f}\n")
                if HJ.f2(*x) < f0:
                    f0 = HJ.f2(*x)
                    continue
                x[j] -= self.h * 2
                print(f"Вектор при отрицательном шаге:\n{x[0]:.4f}\t\t\t{x[1]:.4f}\n")
                print(f"Значение вектора при отрицательном шаге:"
                        f"\n{HJ.f2(*x):.4f}\n")
                if HJ.f2(*x) < f0:
                    f0 = HJ.f2(*x)
                else:
                    x[j] += self.h
            i+=1
            print(f"Вектор X1:\n{x[0]:.4f}\t\t\t{x[1]:.4f}\n")
            print(f"Численное значение вектора X1:"
                    f"\n{HJ.f2(*x):.4f}\n")
            if base == x:
                self.h /= self.d
                continue
            xp = [x[j] + self.m * (x[j] - base[j]) for j in range(2)]
            print(f"Вектор Xp:\n{xp[0]:.4f}\t\t\t{xp[1]:.4f}\n")
            print(f"Численное значение вектора Xp:"
                    f"\n{HJ.f2(*xp):.4f}\n")
            if HJ.f2(*xp) < f0:
                base = xp
            else:
                base = x

HJ_ob = HJ([2,2], 1, 2, 2, 0.0001)
HJ_ob.main()

