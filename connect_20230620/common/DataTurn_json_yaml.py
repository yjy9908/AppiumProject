import codecs
import json
import os.path

import yaml


class DataTurn:


    def read_data_from_json_yaml(data_file):
        return_value = [] #初始赋值return_value
        tuple_value = ()
        data_file_path = os.path.abspath(data_file) #获取文件路径
        print(data_file_path)
        _is_yaml_file = data_file_path.endswith((".yml", ".yaml"))#获取文件的后缀名

        #之所以使用with codes.open() as file的格式，目的是在对文件操作之后接着关闭文件，防止长时间占用内存。
        with codecs.open(data_file_path, 'r', 'utf-8') as f:
            if _is_yaml_file:
                data = yaml.safe_load(f)
                #yaml.safe_load()函数用于解析YAML格式的数据
            else:
                data = json.load(f)
                #从json文件对象中读取数据转抱为dict类型

        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标。
        for i, elem in enumerate(data):
            # isinstance()是用来判断一个对象的变量类型。dict字典类型
            if isinstance(data, dict):
                key, value = elem, data[elem]
                print(elem)
                if isinstance(value, dict):
                    case_data = [] #初始赋值case_data
                    #遍历value
                    for v in value.values():
                        case_data.append(v)
                    #创建元组tuple()
                    return_value.append(tuple(case_data))
                else:
                    tuple_value+=(value,)
                    if len(tuple_value)>1:
                        return_value.append(tuple_value)
                    print(return_value)
        return return_value


if __name__ == '__main__':
    DataTurn.read_data_from_json_yaml("../data/account.json")

