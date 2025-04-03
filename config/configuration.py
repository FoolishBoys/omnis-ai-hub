#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from config.yaml_r import load_yaml


class Config:
    """_summary_
    单例
    Returns:
        _type_: _description_
    """
    _instance = None
    _settings = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance
    
    def _load_config(self) -> dict:
        self._settings = load_yaml(os.path.join(os.path.abspath(__file__), "..", "config.yaml"))
        # 添加omnis根目录
        self._settings['ProjRootPath'] = os.path.join(os.path.abspath(__file__), "..", "..")
    
    def get_all_config(self) -> dict:
        return self._settings
    
    def get_config_by_key(self, key: str, default=None):
        return self._settings.get(key, default)
    
        