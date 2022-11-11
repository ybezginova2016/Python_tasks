# Another alternative from statistics is bootstrapping, a method long used to estimate
# the sampling distribution of statistics, which are presumed not to follow a
# previously assumed distribution. Bootstrapping works by building a number (the
# more the better) of samples of size n (the original in-sample size) drawn with
# repetition. To draw with repetition means that the process could draw an example
# multiple times to use it as part of the bootstrapping resampling. Bootstrapping
# has the advantage of offering a simple and effective way to estimate the true error
# measure. In fact, bootstrapped error measurements usually have much less variance
# than cross-validation ones. On the other hand, validation becomes more
# complicated due to the sampling with replacement, so your validation sample
# comes from the out-of-bootstrap examples. Moreover, using some training samples
# repeatedly can lead to a certain bias in the models built with bootstrapping.
# If you’re using out-of-bootstrapping examples for your test, you’ll notice that the
# test sample can be of various sizes, depending on the number of unique examples
# in the in-sample, likely accounting for about a third of your original in-sample
# size. This simple Python code snippet demonstrates randomly simulating a certain
# number of bootstraps:

import numpy as np
n = 1000
results = list()
for j in range(10000):
    chosen = np.random.randint(0, n, size=n)
    results.append(len(np.unique(chosen)) / n)
    avg_oob = 1 - np.mean(results)

print(f"Avg out-of-boostrap: {avg_oob*100:0.3}%")

# The code creates a large number of trials, each one sampling with repetition
# (which means that a case can be reused multiple times in the sample) and then
# computes the number of unique examples and the portion of cases left out as
# out-of-sample each time. Finally, the portion of left-out samples is averaged
# through all the trials. Running the experiment may require some time, and your
# results may be different because of the random nature of the sampling. Here is
# some representative output:
#
# Out-of-boostrap: 36.8 %