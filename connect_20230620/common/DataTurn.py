import codecs
import json
import os.path

import yaml


class DataTurn:


    def read_data_from_json_yaml(data_file):
        return_value = []
        data_file_path = os.path.abspath(data_file)
        print(data_file_path)
        _is_yaml_file = data_file_path.endswith((".yml", ".yaml"))

        with codecs.open(data_file_path, 'r', 'utf-8') as f:
            if _is_yaml_file:
                data = yaml.safe_load(f)
            else:
                data = json.load(f)

        for i, elem in enumerate(data):
            if isinstance(data, dict):
                key, value = elem, data[elem]
                if isinstance(value, dict):
                    case_data = []
                    for v in value.values():
                        case_data.append(v)
                    return_value.append(tuple(case_data))
                else:
                    return_value.append((value,))
        return return_value
