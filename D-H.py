#
# y=g^x mod p

A = 8
B = 9


def ci_fan_mod(p, g, flag):
    if flag == 0:
        y1 = pow(g, A)
        y2 = pow(g, B)
        print("取mod前：", y1, y2)
        y3 = pow(g, A, p)
        y4 = pow(g, B, p)
        print("取mod后：y1=", y3, " y2=", y4)
        return y3, y4
    if flag == 1:
        y3 = pow(g, A)
        print(y3)
        y3 = pow(g, A, p)
        print("A算得的Ks:", y3)
    if flag == 2:
        y4 = pow(g, B)
        print(y4)
        y4 = pow(g, B, p)
        print("B算得的Ks:", y4)


def count_ks(p, g):
    y1, y2 = ci_fan_mod(p, g, 0)
    ci_fan_mod(p, y2, 1)
    ci_fan_mod(p, y1, 2)


p = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
     227, 229, 233, 239, 241, 251]
g = [2, 5, 2, 6, 3, 3, 2, 3, 2, 2, 6, 5, 2, 5, 2, 2, 2, 19, 5, 2, 3, 2, 3, 2, 6, 3, 7, 7, 6]
# count_ks(101, 2)
for i in range(len(p)):
    print("第" + str(i + 1) + "个：")
    print("p=",p[i],"g=",g[i])
    count_ks(p[i], g[i])
