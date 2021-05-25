#Verify that the data for each year follows a normal distribution
import scipy.stats
import pandas as pd
import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from scipy.stats import wasserstein_distance
from scipy import stats
from scipy.stats import kstest
from scipy.stats import shapiro
disease_list = ['Coronary Heart Disease Prevalence', 'Stroke or Transient Ischaemic Attacks (TIA) Prevalence',
                   'Hypertension Prevalence', 'Diabetes Mellitus (Diabetes) Prevalence',
                   'Chronic Obstructive Pulmonary Disease Prevalence', 'Epilepsy Prevalence', 'Cancer Prevalence',
                   'Mental Health Prevalence', 'Asthma Prevalence', 'Heart Failure Prevalence',
                   'Palliative Care Prevalence', 'Dementia Prevalence', 'Depression Prevalence',
                   'Chronic Kidney Disease Prevalence', 'Atrial Fibrillation Prevalence', 'Obesity Prevalence',
                   'Learning Disabilities Prevalence', 'Cardiovascular Disease Primary Prevention Prevalence']

def Histogram(diease_id):
    print()
    df = pd.read_csv("./DATA/UK_Obesity.csv")
    for year in range(2008, 2018):

        col_list = [disease_list[diease_id] + "_" + str(year)]
        df2 = df[col_list]
        # print(df2)
        delete1 = df2[df2[col_list[0]] == 0].index.tolist()
        df2 = df2.drop(delete1)
        print(df2)
        x = list(df2[disease_list[diease_id] + "_" + str(year)])
        print(x)
        plt.figure()

        plt.hist(x)
        plt.grid(alpha=0.5, linestyle='-.')
        plt.title(year)
        #plt.show()
        plt.savefig("./image/" + "UK_Histogram.png", dpi=600, bbox_inches='tight')
        break

def QQplot(diease_id):
    print()
    df = pd.read_csv("./DATA/UK_Obesity.csv")

    for year in range(2008, 2018):
        col_list = [disease_list[diease_id] + "_" + str(year)]
        df2 = df[col_list]
        # print(df2)
        delete1 = df2[df2[col_list[0]] == 0].index.tolist()
        df2 = df2.drop(delete1)
        print(df2)
        x = list(df2[disease_list[diease_id] + "_" + str(year)])
        print(x)
        fig = plt.figure()
        res = stats.probplot(x, plot=plt)
        #plt.show()
        #plt.figure()  
        plt.grid(alpha=0.5, linestyle='-.')

        plt.tick_params(labelsize=18)
        plt.title("QQ-plot", fontdict={'weight': 'normal', 'size': 20})
        plt.xlabel("Theoretical quantiles", fontdict={'weight': 'normal', 'size': 20})
        plt.ylabel("Ordered Values", fontdict={'weight': 'normal', 'size': 20})

        plt.savefig("./image/" + "UK_QQplot.png", dpi=600, bbox_inches='tight')
        #plt.show()
        break

def KS_test(diease_id):
    print()
    df = pd.read_csv("./DATA/UK_Obesity.csv")

    for year in range(2008, 2018):

        col_list = [disease_list[diease_id] + "_" + str(year)]
        df2 = df[col_list]
        # print(df2)
        delete1 = df2[df2[col_list[0]] == 0].index.tolist()
        df2 = df2.drop(delete1)
        print(df2)
        x = list(df2[disease_list[diease_id] + "_" + str(year)])
        print(x)
        print(kstest(x, cdf="norm"))
        break

def SW_test(diease_id):
    #print()
    res = []
    x1 = []
    df = pd.read_csv("./DATA/UK_Obesity.csv")
    for year in range(2008, 2018):
        print(year)
        x1.append(str(year))
        col_list = [disease_list[diease_id] + "_" + str(year)]
        df2 = df[col_list]
        # print(df2)
        delete1 = df2[df2[col_list[0]] == 0].index.tolist()
        df2 = df2.drop(delete1)
        #print(df2)
        x = list(df2[disease_list[diease_id] + "_" + str(year)])
        #print(x)
        print(shapiro(x))
        res.append(shapiro(x)[0])
        #break
    print(res)
    print(x1)
    plt.bar(x1,res)
    plt.grid(alpha=0.5, linestyle='-.')  #
    plt.title("Shapiro-Wilk test",fontdict={'weight': 'normal', 'size': 20})
    plt.ylim(0, 1.1)
    plt.tick_params(labelsize=10)
    #plt.show()
    plt.savefig("./image/" + "UK_SWtest.png", dpi=600, bbox_inches='tight')

if __name__ == '__main__':
    diease_id = 15
    #Histogram(diease_id)
    #QQplot(diease_id)
    #KS_test(diease_id)
    SW_test(diease_id)