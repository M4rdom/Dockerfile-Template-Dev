import os

from EVngine.models import VEngine

# CONSTANTS
FM_MODEL_PATH = os.path.join('feature models','Dockerfile','Dockerfile_fm.uvl')
CONFIGURATION_PATH = os.path.join('configurations','FrontEnd','Example_3','configuration.json')
TEMPLATE_PATH = os.path.join('templates','Dockerfile','dockerfile.jinja')
#TEMPLATE_PATH = os.path.join('templates','Configuration Files','Nginx','nginx.conf.jinja')
#MAPPING_MODEL_PATH = os.path.join(BASE_PATH, CASE_STUDY, 'mapping_models', f'{CASE_STUDY}_mapping.csv')


if __name__ == '__main__':
    fm_model_path = FM_MODEL_PATH
    configuration_path = CONFIGURATION_PATH
    template_path = TEMPLATE_PATH
    #mapping_model_path = MAPPING_MODEL_PATH
    vengine = VEngine()
    vengine.load_configuration(configuration_path)
    #vengine.load_mapping_model(mapping_model_path)
    vengine.load_template(template_path)
    result = vengine.resolve_variability()
    print(result)

    with open('Dockerfile', 'w' ,encoding="utf-8") as file:
        file.write(result)