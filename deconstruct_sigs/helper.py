import pandas as pd
import numpy as np
import os
class SigHelper(object):
    def __init__(self):
        package_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), os.path.pardir)

        self.ordered_signatures_sample = pd.read_csv(
        os.path.join(package_path,'data/signatures_probabilities.txt'),
        sep='\t', usecols=np.arange(0, 33))

        self.input_signatures_sample = pd.read_csv(
        os.path.join(package_path,'data/signatures_probabilities.txt'),
        sep='\t', usecols=np.arange(3, 33))

        temdf = pd.DataFrame()
        signames = [col for col in  self.ordered_signatures_sample.columns.values
                    if 'Signature' in col]
        temdf['Signature'] = signames
        temdf['Association'] = 'no info'
        self.annotation_sample = temdf

    def get_ordered_df(self):
        return self.ordered_signatures_sample

    def get_signatures_sample(self):
        return self.input_signatures_sample

    def get_annotation_sample(self):
        return self.annotation_sample

SigHelper()