#计算共多少suc_pdf为true的文件
#coding=utf-8
import json

class OperationJson:
  def __init__(self,file_name=None):  
    if file_name:
      self.file_name = file_name
    else:
      self.file_name = './data.json'
  
  #读取json文件
  def convertList(self):
    with open(self.file_name,encoding="utf-8") as fp:
         data = json.load(fp)
         metadata=data["paper_list"]
    return metadata
  
  #清除文件不存在的那行信息
  def get_c(self,fileToList):
    cont=0
    for a_dist in fileToList:
        ans=a_dist["suc_pdf"]
        if ans is True:
            cont+=1
    return cont
  def save(self):
    for a_file in fileToList:
        if a_file["source"]=="google_shcolor":
              source = goo_ori_path+a_file["filejsonname"]
              target = goo_save_path+a_file["filejsonname"]
              # adding exception handling
              try:
                  copyfile(source, target)
              except IOError as e:
                  print("Unable to copy file. %s" % e)
                  #exit(1)
                  #break
              except:
                  print("Unexpected error:", sys.exc_info())
                  #exit(1)


if __name__ == '__main__':
  #goo_opers = OperationJson(file_name='./small_paperlist.json')
  goo_opers = OperationJson(file_name='/home/ddd/data/sp3/sp3_papers/google_shcolor_all_2.2.json')
  goo_fileToList=goo_opers.convertList()
  #save_path="./save.json"
  #bai_opers = OperationJson(file_name='./small_paperlist2.json')
  bai_opers = OperationJson(file_name='/home/ddd/data/sp3/sp3_papers/baidu_xueshu_all_2.2.json')
  bai_fileToList=bai_opers.convertList()
  c=goo_opers.get_c(goo_fileToList)
  b_c=bai_opers.get_c(bai_fileToList)
  print("google")
  print(c)
  print("baidu")
  print(b_c)
  print('ss')