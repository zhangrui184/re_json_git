#读取json中的titles,abstractTexts
#coding=utf-8
import json

class OperationJson:
  def __init__(self,file_name=None):  
    if file_name:
      self.file_name = file_name
    else:
      self.file_name = './s1_out_qqy.json'
   # self.data = self.get_data()
    
  def get_data(self):
    titles=[]
    abstractTexts=[]
    with open(self.file_name,encoding="utf-8") as fp:
         data = json.load(fp)
         metadata=data['metadata']
         title=metadata['title']
         sections=metadata['sections']
         abstractText=metadata['abstractText']
         titles.append(title)
         abstractTexts.append(abstractText)
    fp.close()
    return data,titles,abstractTexts
  
 # def get_value(data,id):
 #   return data[id]


if __name__ == '__main__':
  opers = OperationJson()
  data,titles,abstractTexts=opers.get_data()
  print('ss')
 # print(opers.get_value('name'))
  