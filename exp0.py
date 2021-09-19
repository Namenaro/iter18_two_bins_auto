# ЗАДАЧА ЭКСПЕРИМЕНТА - ОТЛАДИТЬ ФОРМУЛУ ПРИБЫЛИ НА УПРАВЛЕНИИ
# ПРИБЫЛЬ ОТ БИНАРНОГО ДЕТЕКТОРА на УПРАВЛЕНИИ ТАКОМ-ТО: profit (А,u) -> число
# руками тыкаем где А и несколько ю
# замеряем силу связи между А в разных его конфигурациях и данным ю
# попутно для каждого ю строи все графики
# на итоговой картинке строим все связи линиями

from data import *
from logger import *
from binary import *

def eval_profit(A, u, pic_trains, pics_test):




if __name__ == "__main__":
    logger = HtmlLogger("18exp")

    etalon_pic, pics_train, pics_test  = get_all_data3()

    logger.close()
