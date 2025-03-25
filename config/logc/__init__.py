'''
File Created: Monday, 24th March 2025 2:45:14 pm
Author: Csy (1391023795@qq.com)
Description: 
'''
import os
from config.yaml_r import load_yaml

log_config = load_yaml(os.path.join(os.path.abspath(__file__), "..", "log.yaml"))
