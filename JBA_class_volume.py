class Sphere:
    # finish class Sphere here
    PI = 3.1415

    def __init__(self, radius):
        self.radius = radius
        self.volume = (4 / 3) * self.PI * (radius ** 3)


s = Sphere(5)
print(s.volume)
