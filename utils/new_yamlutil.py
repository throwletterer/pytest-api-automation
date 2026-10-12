import yaml

class YamlReader:
    #保存实例化对象时 传入的路径  如Reader=YmalReader('login.yaml')
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file
    #读取yaml   data=reader.data()

#     @utils.mark.parametrize(
#     "case",
#     YamlReader("login.yaml").data()
# )
    def data(self):
        with open(self.yaml_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
