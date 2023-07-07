# Import statistics Library
import statistics

# Calculate harmonic mean
print(statistics.harmonic_mean([40, 60, 80]))
print(statistics.harmonic_mean([10, 30, 50, 70, 90]))


# statistics.harmonic_mean()	Calculates the harmonic mean (central location) of the given data
# statistics.mean()	Calculates the mean (average) of the given data
# statistics.median()	Calculates the median (middle value) of the given data
# statistics.median_grouped()	Calculates the median of grouped continuous data
# statistics.median_high()	Calculates the high median of the given data
# statistics.median_low()	Calculates the low median of the given data
# statistics.mode()	Calculates the mode (central tendency) of the given numeric or nominal data
# statistics.pstdev()	Calculates the standard deviation from an entire population
# statistics.stdev()	Calculates the standard deviation from a sample of data
# statistics.pvariance()	Calculates the variance of an entire population
# statistics.variance()	Calculates the variance from a sample of data


# Calculate average values
print(statistics.mean([1, 3, 5, 7, 9, 11, 13]))
print(statistics.mean([1, 3, 5, 7, 9, 11]))
print(statistics.mean([-11, 5.5, -3.4, 7.1, -9, 22]))


print(statistics.median([1, 3, 5, 7, 9, 11, 13]))
print(statistics.median([1, 3, 5, 7, 9, 11]))
print(statistics.median([-11, 5.5, -3.4, 7.1, -9, 22]))



print(statistics.median_grouped([1, 2, 3, 4]))
print(statistics.median_grouped([1, 2, 3, 4, 5]))
print(statistics.median_grouped([1, 2, 3, 4], 2))
print(statistics.median_grouped([1, 2, 3, 4], 3))
print(statistics.median_grouped([1, 2, 3, 4], 5))



# Inferential Statistics
# Stat Statistical Inference
# Stat Normal Distribution
# Stat Standard Normal Distribution
# Stat Students T-Distribution
# Stat Estimation
# Stat Population Proportion Estimation
# Stat Population Mean Estimation
# Stat Hypothesis Testing
# Stat Hypothesis Testing Proportion
# Stat Hypothesis Testing Mean
