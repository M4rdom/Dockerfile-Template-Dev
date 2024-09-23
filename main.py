import os

import UVengine

# CONSTANTS
FM_MODEL_PATH = os.path.join('feature models','Dockerfile','Dockerfile_fm.uvl')

#Entrada Para Dockerfile
CONFIGURATION_PATH = os.path.join('Dockerfile_fm.uvl.json')

TEMPLATE_PATH = os.path.join('templates','Dockerfile','Dockerfile.jinja')
MAPPING_MODEL_PATH = os.path.join('mapping models','Dockerfile','Dockerfile_mapping_model.csv')


if __name__ == '__main__':
    fm_model_path = FM_MODEL_PATH


    configuration_path = CONFIGURATION_PATH
    template_path = TEMPLATE_PATH
    mapping_model_path = MAPPING_MODEL_PATH
    
    
    
    vengine = UVengine.VEngine()
    vengine.load_configuration(configuration_path)
    vengine.load_mapping_model(mapping_model_path)
    vengine.load_template(template_path)

    
    
    result = vengine.resolve_variability()
    
    
    
    
    print(result)
    with open('Dockerfile', 'w' ,encoding="utf-8") as file:
        file.write(result)