import os
import json


def scan_data_config(model_name):
    """
    Take a model name and return a dictionary of whether the associated data and configuration files 
    are available for that model or not.
    """

    available_data_config = {
        'example_data': False,
        'example_config': False}

    #Check data availability
    for filename in os.listdir("./data/"):
        if filename.startswith(model_name):
            available_data_config['example_data'] = True
    
    #Check config file availability
    for filename in os.listdir("./config-files/"):
        if filename.startswith(model_name):
            available_data_config['example_config'] = True
    
    return available_data_config


def scan_subdir(model_type):
    """Scan a directory and return a list of example models, and a dictionary indicating
    whether each model has associated example data and example config file or not."""
    
    #Create the path to the sub directory
    dir_path = model_type + "/"
    
    #List of available models
    available_models = []

    #Dictionary to save data's and config's availability
    data_config_avai = {}
    
    for filename in os.listdir(dir_path):
        
        if model_type == 'keras':
            if filename.endswith('.json'):
                available_models.append(filename)
                data_config_avai[filename] = scan_data_config(filename[:-5])
        elif model_type == 'pytorch':
            if filename.endswith('.pt'):
                available_models.append(filename)
                data_config_avai[filename] = scan_data_config(filename[:-3])
        elif model_type == 'tensorflow':
            if filename.endswith('.pb'):
                available_models.append(filename)
                data_config_avai[filename] = scan_data_config(filename[:-3])
        elif model_type == 'onnx':
            if filename.endswith('.onnx'):
                available_models.append(filename)
                data_config_avai[filename] = scan_data_config(filename[:-5])
        
    return available_models, data_config_avai
    
def scan():
    """Scan all directories that contain example models and write to a file."""
    
    available_types = ['keras', 'pytorch', 'onnx', 'tensorflow']
    
    #Dictionary to save available model list
    model_dict = {}

    #Dictionary to check for data and configuration availability
    data_config_avai = {}
    
    for model_type in available_types:
        model_dict[model_type], temp_data_config_avai = scan_subdir(model_type)

        #Upate the availability of data and configuration for new scanned model
        data_config_avai.update(temp_data_config_avai)

    # Serialize data into file:
    json.dump(model_dict, open("available_models.json", 'w' ))
    json.dump(data_config_avai, open("available_data_config.json", 'w' ))

scan()