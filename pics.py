import os
from data_base.functions import Datafunc
from data_base.models import PicturesAction, PicturesTruth


all_files = os.listdir('pictures/truths')
for name in all_files:
    file_name = f'pictures/truths/{name}'
    obj = Datafunc.search_truth(file_name)
    if obj == None:
        truth = PicturesTruth(filename=file_name)
        Datafunc.add(truth)

all_files = os.listdir('pictures/acts')
for name in all_files:
    file_name = f'pictures/acts/{name}'
    obj = Datafunc.search_act(file_name)
    if obj == None:
        act = PicturesAction(filename=file_name)
        Datafunc.add(act)
    