from cliker import *
from world import *
from binary import *
from nonbinary import *
from logger import *
from model import *

def get_conditions_control_candidates(etalon_pic):
    X,Y = select_coord_on_pic(etalon_pic)
    conditions = []

    for e_rad in range(10,50,500):
        condition = BinaryUnit(etalon_pic, X[0], Y[0],sens_rad=0,u_rad=0,e_rad=e_rad,dx=0,dy=0)
        conditions.append(condition)

    dx = X[1]-X[0]
    dy = Y[1]-Y[0]
    control = NonBinaryUnit(etalon_pic,X[1],Y[1],sens_rad=0,u_rad=0,dx=dx,dy=dy)
    return conditions, control, X[0], Y[0]

def eval_error_nbins(train_sample, test_sample, nbins):
    probs, bins = get_hist(train_sample, nbins)
    predictions_sample = sample_from_hist(probs, bins, len(test_sample))
    mean_error = count_error_btw_two_samples(test_sample, predictions_sample)
    return mean_error

def eval_error(train_sample, test_sample):
    nbinses = list(range(2,20,3))
    errors = []
    for nbins in nbinses:
        error = eval_error_nbins(train_sample, test_sample, nbins)
        errors.append(error)
    minimal_error=min(errors)
    nbins = nbinses[errors.index(minimal_error)]
    return minimal_error, nbins

def draw(grid,error_with, error_without, condition, logger):
    fig, ax = plt.subplots()
    ax.plot(grid,error_with,  markerfacecolor='blue', markersize=12, color='#00bfff', linewidth=4, label='error_with')
    ax.plot(grid,error_without,  markerfacecolor='blue', markersize=12, color='#0080ff', linewidth=4, label='error_without')
    if condition is None:
        print("no best condition")
    else:
        plt.axvline(condition.e_rad, 0, 1, markersize=12,label='decision')
    ax.legend()
    logger.add_fig(fig)

def main():
    logger = HtmlLogger("exp18")
    world = World3()
    conditions, control, x,y = get_conditions_control_candidates(world.etalon_pic)
    base_train_sample = world.get_train_sample(control, None)
    errors_with = []
    errors_without = []
    grid = []
    best_condition = None
    for condition in conditions:
        test = world.get_test_sample(condition, control)
        train = world.get_train_sample(condition, control)
        error_with = eval_error_nbins(train, test, nbins=20)
        error_without = eval_error_nbins(base_train_sample, test, nbins=20)
        grid.append(condition.e_rad)
        errors_with.append(error_with)
        errors_without.append(error_without)
        if error_with>=error_without:
            if best_condition is None:
                best_condition = condition

    draw(grid, error_with, error_without, best_condition, logger)
    logger.close()

main()

