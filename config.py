import io
import json
import os

config = {'config': []}
config['config'].append({
    'DefaultSaveMethod': 'sqlite',
    'EncryptPassword': 'no',
})


def startup_check():
    if os.path.isfile('config.json') and os.access('config.json', os.R_OK):
        print("File exists and is readable")
    else:
        print("Either file is missing or is not readable, creating file...")
        with io.open(os.path.join('config.json', 'config.json'), 'w') as db_file:
            db_file.write(json.dumps(config))


def dump_file(ref):
    if os.path.isfile('config.json') and os.access('config.json', os.R_OK):
        with io.open(os.path.join('', 'config.json'), 'w') as db_file:
            db_file.write(json.dumps(ref))
            return 1


def check_dbtype():
    if os.path.isfile('config.json') and os.access('config.json', os.R_OK):
        with open('config.json') as json_file:
            file = json.load(json_file)
            for v in file['config']:
                if v['DefaultSaveMethod'] == 'sqlite':
                    return 1
                elif v['DefaultSaveMethod'] == 'mysql':
                    return 2
                else:
                    return 0
