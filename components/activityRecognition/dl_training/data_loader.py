# encoding: utf-8

"""
code credits https://github.com/huguyuehuhu/HCN-pytorch
credits: huguyuehuhu
huguyuehuhu@gmail.com
"""
import torch
from feeder.feeder import Feeder
import numpy as np

def fetch_dataloader(types, params, cad_env='all'):
    """
    Fetch and return train/dev
    """
    if 'NTU-RGB-D' in params.dataset_name :
        if 'CV' in params.dataset_name:
            params.train_feeder_args["data_path"] = params.dataset_dir+'/NTU-RGB-D'+'/xview/train_data.npy'
            params.train_feeder_args["num_frame_path"] = params.dataset_dir+'/NTU-RGB-D'+'/xview/train_num_frame.npy'
            params.train_feeder_args["label_path"] = params.dataset_dir + '/NTU-RGB-D' + '/xview/train_label.pkl'
            params.test_feeder_args["data_path"] = params.dataset_dir + '/NTU-RGB-D' + '/xview/val_data.npy'
            params.test_feeder_args["num_frame_path"] = params.dataset_dir + '/NTU-RGB-D' + '/xview/val_num_frame.npy'
            params.test_feeder_args["label_path"] = params.dataset_dir + '/NTU-RGB-D' + '/xview/val_label.pkl'

        if 'CS' in params.dataset_name:
            params.train_feeder_args["data_path"] = params.dataset_dir + '/NTU-RGB-D' + '/xsub/train_data.npy'
            params.train_feeder_args["num_frame_path"] = params.dataset_dir + '/NTU-RGB-D' + '/xsub/train_num_frame.npy'
            params.train_feeder_args["label_path"] = params.dataset_dir + '/NTU-RGB-D' + '/xsub/train_label.pkl'
            params.test_feeder_args["data_path"]= params.dataset_dir + '/NTU-RGB-D' + '/xsub/val_data.npy'
            params.test_feeder_args["num_frame_path"] = params.dataset_dir + '/NTU-RGB-D' + '/xsub/val_num_frame.npy'
            params.test_feeder_args["label_path"] = params.dataset_dir + '/NTU-RGB-D' + '/xsub/val_label.pkl'

    if 'CAD-60' in params.dataset_name :
        params.train_feeder_args["data_path"] = params.dataset_dir+'/CAD-60'+ '/' + cad_env + '/' + params.cad_fold + '/train_data.npy'
        params.train_feeder_args["num_frame_path"] = params.dataset_dir+'/CAD-60' +'/' + cad_env + '/' + params.cad_fold + '/train_num_frame.npy'
        params.train_feeder_args["label_path"] = params.dataset_dir + '/CAD-60' +'/' + cad_env + '/' + params.cad_fold + '/train_label.pkl'
        params.test_feeder_args["data_path"] = params.dataset_dir + '/CAD-60' +'/' + cad_env + '/' + params.cad_fold + '/val_data.npy'
        params.test_feeder_args["num_frame_path"] = params.dataset_dir + '/CAD-60' +'/' + cad_env + '/' + params.cad_fold + '/val_num_frame.npy'
        params.test_feeder_args["label_path"] = params.dataset_dir + '/CAD-60' +'/' + cad_env + '/' + params.cad_fold + '/val_label.pkl'

    if types == 'train':
        if not hasattr(params,'batch_size_train'):
            params.batch_size_train = params.batch_size

        loader = torch.utils.data.DataLoader(
            dataset=Feeder(**params.train_feeder_args),
            batch_size=params.batch_size_train,
            shuffle=True,
            num_workers=params.num_workers,pin_memory=params.cuda)

    if types == 'test':
        if not hasattr(params,'batch_size_test'):
            params.batch_size_test = params.batch_size

        loader = torch.utils.data.DataLoader(
            dataset=Feeder(**params.test_feeder_args),
            batch_size=params.batch_size_test ,
            shuffle=False,
            num_workers=params.num_workers,pin_memory=params.cuda)

    return loader

if __name__ == '__main__':

    pass
