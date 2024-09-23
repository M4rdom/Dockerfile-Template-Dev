from pathlib import Path


CURRENT_PATH = Path(__file__).resolve().parent

TEMPLATE_PATH = CURRENT_PATH.parent/'templates'/'Dockerfile'/'Dockerfile.jinja'
MAPPING_MODEL_PATH = CURRENT_PATH.parent/'mapping models'/'Dockerfile'/'Dockerfile_mapping_model.csv'

FRONTEND= 'FrontEnd'
BACKEND= 'BackEnd'
DATABASE= 'Database'
DATABASESERVER= 'DatabaseServer'
WEBSERVER= 'WebServer'