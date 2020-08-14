#正确，在使用，处理数据第一步
# 目标：/home/ddd/data/pc2/v1_2的json文件加了表头后为文件夹ad1
#功能：获取的DOI去重       
#coding=utf-8
import json
import os
from collections import namedtuple

class OperationJson:
  def __init__(self,file_path=None):  
    if file_path:
      self.file_path = file_path
    else:
      self.file_path = '/home/ddd/data/pc2/test_data/'
  
  #读取json文件
  def convertList(self,file_name):
    with open(file_name,encoding="utf-8") as fp:
         data = json.load(fp)
         metadata=data["doi_list"]
    return metadata
 
  #比较当前的DOI是否已经存储
  def diff(self,fileToList,all_fileToList,index,all_index):
    for a_dist in fileToList:
      if len(all_fileToList)==0:
        all_fileToList.append(a_dist['DOI'])
        all_index.append(index)
        index +=1
      for a_all_dist in all_fileToList:
        ans=a_dist["DOI"] in a_all_dist
        if ans is True: 
           break
      if ans is False:
          all_fileToList.append(a_dist['DOI'])
          all_index.append(index)
          index +=1
    return index,all_index,all_fileToList
   
  #获取json文件名称存为list
  def get_file_path_list(self):
    file_path_list=[]
    files = os.listdir(self.file_path)
    # 获取json类型的文件放到一个列表里面
    wdfiles = [f for f in files if f.endswith((".json"))]
    for wdfile in wdfiles:
        wdfile_path=self.file_path+wdfile
        file_path_list.append(wdfile_path)
    return file_path_list
  
  #读取json每一行信息，获得一个file_list的信息
  def read_file(self,filepath_list):
    file_metadata_list=[]
    for filename in filepath_list:
         metadata=self.convertList(file_name=filename)
         file_metadata_list.append(metadata) 
    return file_metadata_list  
 
  #获取最终的index和DOI
  def get_doi_list(self,file_metadata_list):
    all_fileToList=[]
    index=0
    all_index=[]
    for a_file_metadata_list in file_metadata_list:
        index,all_index,all_fileToList=self.diff(a_file_metadata_list,all_fileToList,index,all_index)
    return all_index,all_fileToList
  
  #namedtuple()是产生具有命名字段的元组的工厂函数。命名元组赋予元组中每个位置的意义，并更易读、代码更易维护。
  # 它们可以使用在通常元组使用的地方，并添加了通过名称访问字段的能力，而不是位置索引
  def set_paper(self,all_ex_indexs,all_DOIs,paper):
    try:
        papers = [paper(all_ex_indexs[i],all_DOIs[i]) for i in range(len(all_ex_indexs))]
        return papers
    except Exception:
        a='all_times incorrectly'
        return a

  #将index和DOI转换成字典保存，使用json进行存储
  def save_data(self,papers,save_path):
    json_papers = []
    for paper in papers:
        each_data = {
            'ex_index':paper[0],
            'DOI':paper[1]  
        }
        json_papers.append(each_data)

    with open(save_path, 'a', encoding='utf-8') as f:
        for paper in json_papers:
            f.write(json.dumps(paper, ensure_ascii=False) +','+ '\n')

if __name__ == '__main__':
  file_path='/home/ddd/data/pc2/ad1/'
  opers = OperationJson(file_path=file_path)#创建实例
  file_path_list=opers.get_file_path_list()#获得存json的名称列表list
  file_metadata_list=opers.read_file(file_path_list)#获得每一行json信息的文件列表list
  all_index,all_fileToList=opers.get_doi_list(file_metadata_list)#获得最终的index和DOI列表list
  paper = namedtuple('paper',['ex_index','DOI'])#构建paper函数
  papers=opers.set_paper(all_index,all_fileToList,paper)#创建papers
  save_path='/home/ddd/data/pc2/ad1_result.json'#保存地址
  opers.save_data(papers,save_path)#保存papers成json文件
  print('保存成功')