from sensors import *

class NonBinaryMatch:
    def __init__(self,x,y,value):
        self.x = x
        self.y = y
        self.value = value

class NonBinaryUnit:
    def __init__(self, etalon_pic, x, y, sens_rad, u_rad, dx, dy):
        self.u_radius = u_rad
        self.sensor_field_radius = sens_rad
        self.etalon = make_measurement(etalon_pic,x,y,sens_rad)
        self.dx = dx
        self.dy = dy

    def apply(self, pic, x, y):
        X, Y = get_coords_less_or_eq_raduis(x + self.dx, y + self.dy, self.u_radius)
        nearest_mean = make_measurement(pic, X[0], Y[0], self.sensor_field_radius)
        best_i = 0
        for i in range(1, len(X)):
            mean = make_measurement(pic, X[i], Y[i], self.sensor_field_radius)
            if abs(mean - self.etalon) < abs(nearest_mean - self.etalon):
                nearest_mean = mean
                best_i = i
        best_match = NonBinaryMatch(X[best_i], Y[best_i], nearest_mean)
        return best_match

    def apply2(self,pic, x, y):
        return self.apply(pic, x,y).value