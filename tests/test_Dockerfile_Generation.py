import os

import UVengine

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

FM_MODEL_PATH = os.path.join( 'feature models', 'Dockerfile', 'Dockerfile_fm.uvl')

# Entrada Para el Test Variable
CONFIGURATION_PATH = os.path.join('configurations','FrontEnd','Test_1','Dockerfile_fm.uvl.json')
DOCKERFILE_PATH = os.path.join('configurations','FrontEnd','Test_1','Dockerfile')

# Entrada no variable 
TEMPLATE_PATH = os.path.join(CURRENT_PATH,'..','templates', 'Dockerfile', 'Dockerfile.jinja')
MAPPING_MODEL_PATH = os.path.join(CURRENT_PATH,'..','mapping models', 'Dockerfile', 'Dockerfile_mapping_model.csv')

def test_Dockerfile_Generation():
    fm_model_path = FM_MODEL_PATH
    configuration_path = CONFIGURATION_PATH
    dockerfile_path = DOCKERFILE_PATH
    template_path = TEMPLATE_PATH
    mapping_model_path = MAPPING_MODEL_PATH

    
    
    vengine = UVengine.VEngine()
    vengine.load_configuration(configuration_path)
    vengine.load_mapping_model(mapping_model_path)
    vengine.load_template(template_path)
#
    
    
    result = vengine.resolve_variability()
    
    
    with open(dockerfile_path, 'r', encoding="utf-8") as file:
        expected_result = file.read()
        generated_result = result
    
    assert generated_result == expected_result, f"Expected: {expected_result}, but got: {generated_result}"

test_Dockerfile_Generation()