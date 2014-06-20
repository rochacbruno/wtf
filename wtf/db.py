# coding: utf-8
from os import path
from flask import current_app
import dataset

def get_table(tablename):
    database_name = current_app.config['DATABASE_NAME']
    database_path = path.join(current_app.instance_path, database_name)
    db = dataset.connect('sqlite:///{0}'.format(database_path))
    return db[tablename]