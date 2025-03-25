import yaml
import logging

logger = logging.getLogger()

def load_yaml(file_path) -> dict:
    try:
        logger.warning(f"Yaml file read: {file_path}")
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        logger.error(f"Yaml file not found: {file_path}")
    except yaml.YAMLError as e:
        logger.error(f"Error parsing yaml file: {file_path}, {e}")
    except Exception as e:
        logger.error(f"Error reading yaml file: {file_path}, {e}")
    
    return {}
