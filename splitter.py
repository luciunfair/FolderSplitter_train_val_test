import os 
import random
import shutil

def split(main_folder, split_folder, have_test=True, have_label=False, main_folder_label="", split_folder_label="", train_ratio=0.8, val_ratio=0.1):
    """
    This function is designed to take a folder containing files and another empty folder to create training, validation, and optional test datasets.
    You can also choose to include corresponding label folders for splitting.

    Arguments:
        main_folder (str): The main folder address that contains the files you want to split.
        split_folder (str): The target folder where you want to split the data into training, validation, and optionally, testing.
        have_test (bool): Determines whether you want to include a test dataset (default is True). Set it to False if you don't need test data.
        have_label (bool): Determines whether you want corresponding label folders. Default is False; set it to True if needed.
        main_folder_label (str): The address of the main folder for labels if 'have_label' is set to True.
        split_folder_label (str): The target folder for labels where the split data will be placed if 'have_label' is set to True.
        train_ratio (float): The proportion of data to be allocated to the training dataset.
        val_ratio (float): If 'have_test' is set to False, this ratio is automatically calculated as 1 - train_ratio, and you don't need to specify it.
                           If 'have_test' is True, set 'val_ratio' so that the test ratio becomes 1 - (train_ratio + val_ratio).
    """
    all_files = os.listdir(main_folder)
    if have_label == True:
        all_files_label = os.listdir(main_folder_label)
    index_shuf = list(range(len(all_files)))
    random.seed(10)
    random.shuffle(index_shuf)

    all_files_list = []
    all_files_label_list = []
    for i in index_shuf:
        all_files_list.append(all_files[i])
        if have_label == True:
            all_files_label_list.append(all_files_label[i])
    all_files = all_files_list
    if have_label == True:
        all_files_label = all_files_label_list
        
        
    if have_label == False:
        if have_test == True:
            
            all_files_len = len(all_files)
            train_size = int((train_ratio) * all_files_len)
            val_size = int((val_ratio) * all_files_len)
            test_size = all_files_len - (train_size + val_size)
            train = all_files[:train_size]
            val = all_files[train_size:train_size + val_size]
            test = all_files[train_size + val_size:]
            split_folder_train_name = split_folder + "/" + "train"
            split_folder_val_name = split_folder + "/" + "val"
            split_folder_test_name = split_folder + "/" + "test"

            split_folder_train = os.makedirs(split_folder_train_name)
            split_folder_val = os.makedirs(split_folder_val_name)
            split_folder_test = os.makedirs(split_folder_test_name)
            for i_train in train:
                train_main_addr =  main_folder + "/" + i_train
                train_target_addr = split_folder_train_name + "/" + i_train
                shutil.copy(train_main_addr, train_target_addr)
            for i_val in val:
                val_main_addr =  main_folder + "/" + i_val
                val_target_addr = split_folder_val_name + "/" + i_val
                shutil.copy(val_main_addr, val_target_addr)
            for i_test in test:
                test_main_addr =  main_folder + "/" + i_test
                test_target_addr = split_folder_test_name + "/" + i_test
                shutil.copy(test_main_addr, test_target_addr)
        else:
            
            all_files_len = len(all_files)
            train_size = int((train_ratio) * all_files_len)

            train = all_files[:train_size]
            val = all_files[train_size:]

            split_folder_train_name = split_folder + "/" + "train"
            split_folder_val_name = split_folder + "/" + "val"
            

            split_folder_train = os.makedirs(split_folder_train_name)
            split_folder_val = os.makedirs(split_folder_val_name)
            
            for i_train in train:
                train_main_addr =  main_folder + "/" + i_train
                train_target_addr = split_folder_train_name + "/" + i_train
                shutil.copy(train_main_addr, train_target_addr)
            for i_val in val:
                val_main_addr =  main_folder + "/" + i_val
                val_target_addr = split_folder_val_name + "/" + i_val
                shutil.copy(val_main_addr, val_target_addr)
    else: # it means that have_label is True
        
        if have_test == True:
            
            all_files_len = len(all_files)
            train_size = int((train_ratio) * all_files_len)
            val_size = int((val_ratio) * all_files_len)
            test_size = all_files_len - (train_size + val_size)
            train = all_files[:train_size]
            val = all_files[train_size:train_size + val_size]
            test = all_files[train_size + val_size:]
            train_label = all_files_label[:train_size]
            val_label = all_files_label[train_size:train_size + val_size]
            test_label = all_files_label[train_size + val_size:]
            split_folder_train_name = split_folder + "/" + "train"
            split_folder_val_name = split_folder + "/" + "val"
            split_folder_test_name = split_folder + "/" + "test"
            split_folder_train_label_name = split_folder_label + "/" + "train"
            split_folder_val_label_name = split_folder_label + "/" + "val"
            split_folder_test_label_name = split_folder_label + "/" + "test"

            split_folder_train = os.makedirs(split_folder_train_name)
            split_folder_val = os.makedirs(split_folder_val_name)
            split_folder_test = os.makedirs(split_folder_test_name)
            split_folder_train_label = os.makedirs(split_folder_train_label_name)
            split_folder_val_label = os.makedirs(split_folder_val_label_name)
            split_folder_test_label = os.makedirs(split_folder_test_label_name)
            
            
            for i_train in train:
                train_main_addr =  main_folder + "/" + i_train
                train_target_addr = split_folder_train_name + "/" + i_train
                shutil.copy(train_main_addr, train_target_addr)
            for i_train in train_label:
                train_main_addr =  main_folder_label + "/" + i_train
                train_target_addr = split_folder_train_label_name + "/" + i_train
                shutil.copy(train_main_addr, train_target_addr)   
            for i_val in val:
                val_main_addr =  main_folder + "/" + i_val
                val_target_addr = split_folder_val_name + "/" + i_val
                shutil.copy(val_main_addr, val_target_addr)            
            for i_val in val_label:
                val_main_addr =  main_folder_label + "/" + i_val
                val_target_addr = split_folder_val_label_name + "/" + i_val
                shutil.copy(val_main_addr, val_target_addr)
            for i_test in test:
                test_main_addr =  main_folder + "/" + i_test
                test_target_addr = split_folder_test_name + "/" + i_test
                shutil.copy(test_main_addr, test_target_addr)
                
            for i_test in test_label:
                test_main_addr =  main_folder_label + "/" + i_test
                test_target_addr = split_folder_test_label_name + "/" + i_test
                shutil.copy(test_main_addr, test_target_addr)
        else:
            
            all_files_len = len(all_files)
            train_size = int((train_ratio) * all_files_len)

            train = all_files[:train_size]
            val = all_files[train_size:]
            
            train_label = all_files_label[:train_size]
            val_label = all_files_label[train_size:]
            
            split_folder_train_name = split_folder + "/" + "train"
            split_folder_val_name = split_folder + "/" + "val"
            
            split_folder_train_label_name = split_folder_label + "/" + "train"
            split_folder_val_label_name = split_folder_label + "/" + "val"
            
            split_folder_train = os.makedirs(split_folder_train_name)
            split_folder_val = os.makedirs(split_folder_val_name)

            split_folder_train_label = os.makedirs(split_folder_train_label_name)
            split_folder_val_label = os.makedirs(split_folder_val_label_name)

            
            
            for i_train in train:
                train_main_addr =  main_folder + "/" + i_train
                train_target_addr = split_folder_train_name + "/" + i_train
                shutil.copy(train_main_addr, train_target_addr)
            for i_train in train_label:
                train_main_addr =  main_folder_label + "/" + i_train
                train_target_addr = split_folder_train_label_name + "/" + i_train
                shutil.copy(train_main_addr, train_target_addr)               
            for i_val in val:
                val_main_addr =  main_folder + "/" + i_val
                val_target_addr = split_folder_val_name + "/" + i_val
                shutil.copy(val_main_addr, val_target_addr)
            for i_val in val_label:
                val_main_addr =  main_folder_label + "/" + i_val
                val_target_addr = split_folder_val_label_name + "/" + i_val
                shutil.copy(val_main_addr, val_target_addr)        
                
                
"""  ****** example ******

if __name__ == "__main__":
    main_folder = "E:/project_s/test/sigil_of_lucifer_all/data/images"
    split_folder = "E:/project_s/test/sigil_of_lucifer_split_all/data/images"
    main_folder_label = "E:/project_s/test/sigil_of_lucifer_all/data/labels"
    split_folder_label = 'E:/project_s/test/sigil_of_lucifer_split_all/data/labels'

    split(main_folder, split_folder, have_test=True, have_label=True, main_folder_label=main_folder_label, split_folder_label=split_folder_label)
    
"""
