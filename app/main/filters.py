#coding=utf-8
from app.main import main

@main.app_template_filter('replace_none')
def replace_none(data):
    if not data:
        return ""
    return data