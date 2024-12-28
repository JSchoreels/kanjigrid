JSON_DATA_FOLDER = "./data"

def test_config_update():
    import json

    import config_util

    config_v0 = json.load(open("./tests/config_v0.json", "r"))
    config_current = json.load(open("./config.json", "r"))

    config_migrated = config_util.migrate_config(config_v0)

    config_migrated_string = json.dumps(config_migrated, sort_keys = True, indent = 4)
    config_current_string = json.dumps(config_current, sort_keys = True, indent = 4)

    assert(config_migrated_string == config_current_string)

def test_data_load():
    import data
    data.load_from_folder(data.groups, JSON_DATA_FOLDER)

def test_data_parse():
    import jsonschema
    import json
    import os

    data_schema = json.load(open("./tests/data_schema.json", "r", encoding = "UTF8"))

    for file in os.listdir(JSON_DATA_FOLDER):
        filepath = JSON_DATA_FOLDER + "/" + file
        data_json = json.load(open(filepath, "r", encoding = "UTF8"))
        jsonschema.validate(instance = data_json, schema = data_schema)
