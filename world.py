from data import *
from utils import *

class World3:
    def __init__(self):
        self.etalon_pic, self.pics_train, self.pics_test=get_all_data3()
        self.train_sample_size = 200
        self.test_sample_size = 200

    def get_test_sample(self, control, condition):
        return self._get_sample(control, condition, self.test_sample_size, self.pics_test)

    def get_train_sample(self,control, condition):
        return self._get_sample(control, condition, self.train_sample_size, self.pics_train)

    def _get_sample(self, control, condition, sample_size, pics):
        results = []
        while True:
            if len(results) >= sample_size:
                return results
            pic = select_random_pic(pics)
            x, y = select_random_xoord_on_pic(pic)
            if condition is None or condition(pic, x, y) > 0:
                res = control.apply2(pic, x, y)
                results.append(res)
        return results

