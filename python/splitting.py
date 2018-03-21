""" This module contains methods related to splitting databases. """

import enum

import numpy as np


class EmptyDataSet(Exception):
    pass


class WrongDimension(Exception):
    pass


class DataSet:
    """ A labeled dataset

    Attributes:
        data: np.array[np.array], The vector containing all unlabeled data.
        labels: np.array[str], The vector containing all labels.
        dimension: The dimension of one sample of the data;
        possible_labels: set[str], All existing labels in the database
    """

    def __init__(self, data: iter, label_index: int = -1):
        self.data, self.labels = np.array(), np.array()

        try:
            self.dimension = len(data[0])
        except IndexError:
            raise EmptyDataSet()

        for example in data:
            self.add_data(data, label_index=label_index)

    def __len__(self):
        return len(self.data)

    def add_data(data: iter, label_index: int = -1):
        if self.dimension != len(data) - 1:
            raise WrongDimension(expected=self.dimension, actual=len(data) - 1)
        example = data[:label_index] + data[label_index + 1:]
        label = data[label_index]
        self.data.append(example)
        self.labels.append(label)
        self.possible_labels.add(label)

    def shuffle(self):
        """ Shuffle the examples and labels randomly. """
        new_indexes = shuffle(range(len(self)))


@enum.unique
class SplittingMethod(enum.IntEnum):
    SLICING = 0
    SAME_LABEL_DISTRIBUTION = 1


def split(*, dataset: DataSet,
          percentage_train: float = None,
          number_of_dataset: int = None,
          splitting_method: SplittingMethod = SplittingMethod.SAME_LABEL_DISTRIBUTION):
    pass


def _split_train_test(dataset: DataSet, percentage_train: float):
    pass


def _split_multiple_datasets(dataset: DataSet, number_of_dataset: int,
                             splitting_method: SplittingMethod):
    pass


if __name__ == '__main__':
    pass
