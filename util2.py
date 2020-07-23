#读取json中的name_list,url_list
#coding=utf-8
import json

class OperationJson:
  def __init__(self,file_name=None):  
    if file_name:
      self.file_name = file_name
    else:
      self.file_name = './data.json'
   # self.data = self.get_data()
    
  def get_data(self):
    name_list=[]
    url_list=[]
    with open(self.file_name,encoding="utf-8") as fp:
         data = json.load(fp,strict=False)
         metadata=data['links']
         for i in range(len(metadata)):
             name=metadata[i]['name']
             url=metadata[i]['url']
             name_list.append(name)
             url_list.append(url)
    fp.close()
    return data,name_list,url_list
  
 # def get_value(data,id):
 #   return data[id]


if __name__ == '__main__':
  opers = OperationJson()
  data,name_list,url_list=opers.get_data()
  print('ss')
 # print(opers.get_value('name'))
  