from sensors import *

class BinaryMatch:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class BinaryUnit:
    def __init__(self, etalon_pic, x, y, sens_rad, u_rad=0, e_rad=0, dx=0, dy=0):
        self.u_rad = u_rad
        self.sens_rad = sens_rad
        self.etalon = make_measurement(etalon_pic,x,y,sens_rad)
        self.e_rad = e_rad
        self.dx = dx
        self.dy = dy

    def apply(self, pic, x,y):
        matches = []
        expected_x = x + self.dx
        expected_y = y + self.dy
        for r in range(0, self.u_rad + 1):
            X, Y = get_coords_for_radius(expected_x, expected_y, r)
            for i in range(len(X)):
                mean = make_measurement(pic, X[i], Y[i], self.sens_rad)
                A_min = self.etalon - self.e_rad
                A_max = self.etalon +self.e_rad
                if mean >= A_min and mean <= A_max:
                    matches.append(BinaryMatch(X[i], Y[i]))
        return matches

    def apply2(self, pic, x,y):
        if len(self.apply(pic,x,y)) > 0:
            return 1
        return 0