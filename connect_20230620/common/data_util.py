import os.path

import yaml

def readYaml(path):
    #实现yaml数据的读取
    with open(path,"r+",encoding='utf-8') as file:
        data=yaml.load(stream=file,Loader=yaml.FullLoader)
        return data

if __name__ == '__main__':
    #获取对应根目录路径
    rootPath=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    print(rootPath)
    #路径拼接
    path=os.path.join(rootPath,"config\config.yaml")
    print(readYaml(path))