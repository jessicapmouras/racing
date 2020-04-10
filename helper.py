
import math
import pandas as pd
import numpy as np
import seaborn as sns
import scipy as stats
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.power import TTestIndPower

#helper function group jockey weights into 10 groups of 3 lbs

def group_jockweight(row):
    if row['actual_weight'] >= 130:
        return "10_class"
    if row['actual_weight'] < 130 and row['actual_weight'] >= 127:
        return "9_class"
    if row['actual_weight'] < 127 and row['actual_weight'] >= 124:
        return "8_class"
    if row['actual_weight'] < 124 and row['actual_weight'] >= 121:
        return "7_class"
    if row['actual_weight'] < 121 and row['actual_weight'] >= 118:
        return "6_class"
    if row['actual_weight'] < 118 and row['actual_weight'] >= 115:
        return "5_class"
    if row['actual_weight'] < 115 and row['actual_weight'] >= 112:
        return "4_class"
    if row['actual_weight'] < 112 and row['actual_weight'] >= 109:
        return "3_class"
    if row['actual_weight'] < 109 and row['actual_weight'] >= 106:
        return "2_class"
    if row['actual_weight'] < 106 and row['actual_weight'] >= 103:
        return "1_class"
    return "other"

#helper function group jockey weights into 8 groups of 100 lbs

def group_horseweight(row):
    if row['declared_weight'] >= 1350:
        return "8_class"
    if row['declared_weight'] < 1350 and row['declared_weight'] >= 1250:
        return "7_class"
    if row['declared_weight'] < 1250 and row['declared_weight'] >= 1150:
        return "6_class"
    if row['declared_weight'] < 1150 and row['declared_weight'] >= 1050:
        return "5_class"
    if row['declared_weight'] < 1050 and row['declared_weight'] >= 950:
        return "4_class"
    if row['declared_weight'] < 950 and row['declared_weight'] >= 850:
        return "3_class"
    if row['declared_weight'] < 850 and row['declared_weight'] >= 750:
        return "2_class"
    if row['declared_weight'] < 750 and row['declared_weight'] >= 650:
        return "1_class"
    return "other"

# Welsh's t-test Helper Function
def welch_test_statistic(sample_1, sample_2):
    numerator = np.mean(sample_1) - np.mean(sample_2)
    denominator_sq = (np.var(sample_1) / len(sample_1)) + \
                        (np.var(sample_2) / len(sample_2))
    return numerator / np.sqrt(denominator_sq)


def welch_satterhwaithe_df(samp_1, samp_2):
    ss1 = len(samp_1)
    ss2 = len(samp_2)
    df = (((np.var(samp_1)/ss1 + np.var(samp_2)/ss2)**(2.0)) / 
        ((np.var(samp_1)/ss1)**(2.0)/(ss1 - 1)
         + (np.var(samp_2)/ss2)**(2.0)/(ss2 - 1)))
    return df