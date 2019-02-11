#!/usr/bin/python

import math

def get_mean(dataset):
    return sum(dataset) / len(dataset)

def get_stddev(dataset):
    mean = get_mean(dataset)
    acc = 0.0
    for x in dataset:
        acc += (x - mean) ** 2
    return math.sqrt(acc / float(len(dataset)-1))

def get_median(dataset):
    return get_n_percentile(50, dataset)

def get_n_quartile(n, dataset):
    if n == 1:
        return get_n_percentile(25, dataset)
    elif n == 2:
        return get_n_percentile(50, dataset)
    elif n == 3:
        return get_n_percentile(75, dataset)
    else:
        print("Not valid N quartile")
    return None

def get_n_percentile(n, dataset):
    dataset = sorted(dataset)
    pos = len(dataset)*n/100
    if not pos % 2:
        return (dataset[int(pos)] + dataset[int(pos)-1])/2
    return dataset[int(pos)]
