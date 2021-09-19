"""
Какова средняя ожидаемая ошибка предсказания управления исходя из статистики,
накопленной по этому управлению, совершаемому из ситуации выполнения этого условия
"""
from world import *
from utils import *
from model import *


def eval_error_of_prediction(world, condition, control, nbins):
    train_sample = world.get_train_sample(control, condition)
    test_sample = world.get_test_sample(control, condition)
    return eval_error_from_samples(train_sample, test_sample, nbins)


def eval_min_error_of_prediction(world, condition, control):
    train_sample = world.get_train_sample(control, condition)
    test_sample = world.get_test_sample(control, condition)
    nbinses = list(range(2,20,3))
    errors = []
    for nbins in nbinses:
        error = eval_error_from_samples(train_sample, test_sample, nbins)
        errors.append(error)

    minimal_error=min(errors)
    nbins = nbinses[errors.index(minimal_error)]
    return minimal_error, nbins



def eval_error_from_samples(train_sample, test_sample, nbins):
    model = Model(train_sample, test_sample)
    predictions_sample = model.sample(len(test_sample), nbins)
    mean_error = count_error_btw_two_samples(test_sample, predictions_sample)
    return mean_error
