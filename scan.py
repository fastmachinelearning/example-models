import os
import json

def scan_subdir(model_type):
    """Scan a directory and return a list of example models."""
    
    #Create the path to the sub directory
    dir_path = model_type + "/"
    
    #List of available models
    available_models = []
    
    for filename in os.listdir(dir_path):
        
        if model_type == 'keras':
            if filename.endswith('.h5'):
                available_models.append(filename)
        elif model_type == 'pytorch':
            if filename.endswith('.pt'):
                available_models.append(filename)
        elif model_type == 'tensorflow':
            if filename.endswith('.pb'):
                available_models.append(filename)
        elif model_type == 'onnx':
            if filename.endswith('.onnx'):
                available_models.append(filename)
        
    return available_models
    
def scan():
    """Scan all directories that contain example models and write to a file."""
    
    available_types = ['keras', 'pytorch', 'onnx', 'tensorflow']
    
    model_dict = {}
    
    for model_type in available_types:
        model_dict[model_type] = scan_subdir(model_type)

    # Serialize data into file:
    json.dump(model_dict, open("available_models.json", 'w' ))
    
scan()