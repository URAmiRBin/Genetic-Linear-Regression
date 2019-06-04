a = 1
b = 0
c = 0.27
d = -0.25
points = []
for x in range(100):
    points.append(a*(x*x*x) + b*(x*x) + c*x + d)
print(points)
