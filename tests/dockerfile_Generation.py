import UVengine
import tests.constant as CONST
from pathlib import Path



def assert_Dockerfile_Generation(Folder:str,Test_Number:str) -> bool:
    configuration_path = CONST.CURRENT_PATH/'test_configurations'/Folder/Test_Number/'Dockerfile_fm.uvl.json'
    dockerfile_product_path = CONST.CURRENT_PATH/'test_configurations'/Folder/Test_Number/'Dockerfile'
    template_path = CONST.TEMPLATE_PATH
    mapping_model_path = CONST.MAPPING_MODEL_PATH

    vengine = UVengine.VEngine()
    vengine.load_configuration(configuration_path)
    vengine.load_mapping_model(mapping_model_path)
    vengine.load_template(template_path)
#

    result = vengine.resolve_variability()
    
    
    with open(dockerfile_product_path, 'r', encoding="utf-8") as file:
        expected_result = file.read()
        
    generated_result = result

    assert generated_result == expected_result, f"Expected: {expected_result}, but got: {generated_result}"

def list_test(Folder:str) -> list:
    ruta = Path(CONST.CURRENT_PATH/'test_configurations'/Folder)
    carpetas = [carpeta.name for carpeta in ruta.iterdir() if carpeta.is_dir()]
    return carpetas