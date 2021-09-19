class Model:
    def __init(self, train_sample, test_sample):
        self.train_sample = train_sample
        self.test_sample = test_sample

    def sample(self, sample_size, nbins):
        probs, bins = get_hist(train_sample, nbins)