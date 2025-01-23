import logging
import glob
from importlib.resources import files
from os.path import join
import os
import shutil
from typing import List, Dict,Union,Optional
from unicodedata import east_asian_width

import pandas as pd

class Samples:
    '''
    Class for working with samples in a directory or in cvs file.
    We assume that each sample are in a separate sub-directory or specified in separate line in cvs file.
    Directory name is unique id of the sample or we expect that csv file has a column with unique ids.
    '''
    def __init__(self, path:Optional[str]=None,
                 each_file_sample=False,
                 file_mask:str='*.fastq.gz',
                 attribute_pattern_dict:Optional[Dict[str,str]]=None,
                 cvs_file:Optional[str]=None,
                 verbose:bool=False,
                 log:Optional[logging.Logger]=None):
        if path is None and cvs_file is None:
            raise ValueError("Either path or cvs_file should be specified")
        self.path = None
        self.each_file_sample = each_file_sample
        self.file_mask = file_mask
        if path is not None:
            self.path = path
        self.attribute_pattern_dict = attribute_pattern_dict
        self.verbose = verbose
        self.log = log
        self.get_samples()
        self.metadata_table = self.__generate_file_list(self.samples,self.file_mask,self.each_file_sample)

    def get_samples(self)->None:
        self.samples = []
        if self.each_file_sample:
            self.samples = sorted(glob.glob(join(self.path,self.file_mask)))
        else:
            samples_list = [ f.path for f in os.scandir(self.path) if f.is_dir() ]
            for sample in samples_list:
                #check if sample has files coresponding file mask
                if len(glob.glob(join(sample,self.file_mask))) == 0:
                    warning_msg = f"No files with mask {self.file_mask} in {sample} sample skipped"
                    if self.log is not None:
                        self.log.warning(warning_msg)
                    else:
                        if verbose > 0:
                            warning(warning_msg)
                else:
                    self.samples.append(sample)

    @staticmethod
    def __generate_file_list(samples:List[str],file_mask:str,each_file_sample=False)->pd.DataFrame:
        file_list = {'sample':[],'file':[],'sample_dir':[]}
        for sample in samples:
            if each_file_sample:
                files = [sample]
            else:
                files = sorted(glob.glob(join(sample,file_mask)))
            for f in files:
                file_list['sample_dir'].append(sample)
                file_list['sample'].append(sample.split('/')[-1])
                file_list['file'].append(f)
        return pd.DataFrame(file_list)

    def add_bool_attribute(self,attribute_name:str,feature:str,attribute_source='sample',case_sensitive=True)->None:
        '''
        Add boolean attribute to metadata table based on feature presence in sample id or file name.
        :param attribute_name: name of the attribute to be added
        :param feature: feature to search for
        :param attribute_source: 'sample' or 'file'
        :param case_sensitive: if True search is case sensitive
        '''
        if self.metadata_table is None:
            if self.log is not None:
                self.log.error("metadata_table is not initialized")
                raise ValueError("metadata_table is not initialized")
            else:
                raise ValueError("metadata_table is not initialized")
        if attribute_source not in ['sample','file']:
            if self.log is not None:
                self.log.error(f"attribute_source should be 'sample' or 'file' but {attribute_source} was provided")
                raise ValueError(f"attribute_source should be 'sample' or 'file' but {attribute_source} was provided")
            else:
                raise ValueError(f"attribute_source should be 'sample' or 'file' but {attribute_source} was provided")
        for index,row in self.metadata_table.iterrows():
            if case_sensitive:
                self.metadata_table.loc[index,attribute_name] = feature in row[attribute_source]
            else:
                self.metadata_table.loc[index,attribute_name] = feature.lower() in row[attribute_source].lower()

    def get_info(self)->pd.DataFrame:
        return self.metadata_table
    def __str__(self):
        out_str = f"Number of samples is {len(self.samples)}\n"
        if self.verbose > 0:
            out_str += f"Samples in {self.path}: {self.samples}"
        return out_str