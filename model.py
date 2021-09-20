from utils import *

class Model:
    def __init(self, train_sample):
        self.train_sample = train_sample

    def sample(self, sample_size, nbins):
        probs, bins = get_hist(self.train_sample, nbins)
        return sample_from_hist(probs, bins, sample_size)

