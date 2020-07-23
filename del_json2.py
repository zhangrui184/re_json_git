#使用名称把fileToList的信息用“重复名字”过滤成fileToList_result，只包含需要的信息。
#baidu_xueshu和google_shcolor内部自己检查是否重复，删除重复的
#根据前一个和下一个的DOI是否重复来判断
#coding=utf-8
import json

class OperationJson:
  def __init__(self,file_name=None):  
    if file_name:
      self.file_name = file_name
    else:
      self.file_name = './data.json'
  
  #找出DOI重复的pdf集合
  def get_keyList(self,fileToList):
    keyList=[]
    for index,a_dist in enumerate(fileToList):
        DOI= a_dist["DOI"]
        try:
            next_dist=fileToList[index+1]
            next_DOI=next_dist["DOI"]
        except:
            break
        ans =DOI in next_DOI
        if ans is True:
           keyList.append(a_dist["filename"])
    return keyList
  
  #读取json文件
  def convertList(self):
    with open(self.file_name,encoding="utf-8") as fp:
         data = json.load(fp)
         metadata=data["paper_list"]
    return metadata
  
  #清除文件不存在的那行信息
  def get_clean_result(self,fileToList,keyList):
    fileToList_result=[]
    for a_dist in fileToList:
        ans=None
        for k in keyList:
            ans=k in a_dist.values()
            if ans is True:
               print('no in'+k)
               break
        if ans is False:
           fileToList_result.append(a_dist)
    return fileToList_result


if __name__ == '__main__':
  #opers = OperationJson(file_name='./small_paperlist.json')
  opers = OperationJson(file_name='/home/ddd/data/sp3/sp3_papers/google_shcolor_all_2.2_clean_corre.json')
  fileToList=opers.convertList()
  #save_path="./save.json"
  save_path="/home/ddd/data/sp3/sp3_papers/google_shcolor_all_2.2_clean2.json"
  keyList=opers.get_keyList(fileToList)#keyList是不存在的pdf集合
  fileToList_result=opers.get_clean_result(fileToList=fileToList,keyList=keyList)
  with open(save_path, 'a', encoding='utf-8') as f:
        for paper in fileToList_result:
            f.write(json.dumps(paper, ensure_ascii=False) + ','+'\n')
  print('ss')