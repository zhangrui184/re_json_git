#使用名称把fileToList的信息用“重复名字”过滤成fileToList_result，只包含需要的信息。
#baidu_xueshu和google_shcolor内部自己检查是否重复，删除重复的
#根据前一个和下一个的DOI是否重复来判断
#保存时候增加dict键值对source:baidu_xueshu or google_shcolor
#                   和filejsonname:         
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

  def diff(self,goo_fileToList,bai_fileToList):
    all_list=[]
    for a_bai_dist in goo_fileToList:
      for a_goo_dist in bai_fileToList:
        ans=a_bai_dist["DOI"] in a_goo_dist["DOI"]
        if ans is True:
          ex_ans=self.get_ex_ans(all_list,a_bai_dist)
          if ex_ans is False:
             a_bai_dist["source"]="baidu_xueshu"
             a_bai_dist["filejsonname"]=a_bai_dist["filename"]+".json"
             all_list.append(a_bai_dist)
        else:
          ex_ans2=self.get_ex_ans(all_list,a_bai_dist)
          ex_ans3=self.get_ex_ans(all_list,a_goo_dist)
          if ex_ans2 is False:
            if ex_ans3 is False:                
              a_bai_dist["source"]="baidu_xueshu"
              a_bai_dist["filejsonname"]=a_bai_dist["filename"]+".json"
              a_goo_dist["source"]="google_shcolor"
              a_goo_dist["filejsonname"]=a_goo_dist["filename"]+".json"
              all_list.append(a_bai_dist)
              all_list.append(a_goo_dist)
    return all_list
   
  def get_ex_ans(self,all_list,a_list):
    ans =a_list in all_list
    return ans



if __name__ == '__main__':
  #goo_opers = OperationJson(file_name='./small_paperlist.json')
  goo_opers = OperationJson(file_name='/home/ddd/data/sp3/sp3_papers/google_shcolor_all_2.2_clean2_corre.json')
  goo_fileToList=goo_opers.convertList()
  #save_path="./save.json"
  #bai_opers = OperationJson(file_name='./small_paperlist2.json')
  bai_opers = OperationJson(file_name='/home/ddd/data/sp3/sp3_papers/baidu_xueshu_all_2.2_clean2_corre.json')
  bai_fileToList=bai_opers.convertList()
  save_path="/home/ddd/data/sp3/sp3_papers/all2.json"
  all_list=goo_opers.diff(goo_fileToList,bai_fileToList)
  with open(save_path, 'a', encoding='utf-8') as f:
        for paper in all_list:
            f.write(json.dumps(paper, ensure_ascii=False) + ','+'\n')
  print('ss')