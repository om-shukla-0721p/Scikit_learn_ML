# many methods
# eg
#1) z score
# assumption that distribution is normal
# then we can use trimming(remove) or capping(with np.where) +-3 Zscore of the sample

# 2) boxplot method
# get the outliers and
# then we can use trimming(remove) or capping(with np.where)

# 3) percentile method
# select a threhold for eg 1
# any value above 99 percentile or below 1 percentile then be considered an outlier
# get the outliers apply trimming or capping(here its also called winsorization)

