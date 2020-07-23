#根据baidu_xueshu_all_2.2.json和google_shcolor_all_2.2.json列表获取百度和谷歌分别的Json文件存到baidu_out_suc和google_out_suc位置
# Python Copy File - Sample Code
#coding=utf-8
import json
from shutil import copyfile
from sys import exit



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

  def save(self,fileToList,ori_path,save_path):
    for a_file in fileToList:
        if a_file["suc_pdf"] is True:
              source = ori_path+a_file["filename"]+".json"
              target = save_path+a_file["filename"]+".json"
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
  bai_opers = OperationJson(file_name='/home/ddd/data/sp3/sp3_papers/baidu_xueshu_all_2.2.json')
  bai_fileToList=bai_opers.convertList()
  goo_opers = OperationJson(file_name='/home/ddd/data/sp3/sp3_papers/google_shcolor_all_2.2.json')
  goo_fileToList=goo_opers.convertList()
  bai_ori_path="/home/ddd/data/sp3/sp3_papers/baidu/baidu_out/"
  goo_ori_path="/home/ddd/data/sp3/sp3_papers/google/google_out/"
  bai_save_path="/home/ddd/data/sp3/sp3_papers/baidu/baidu_out_suc/"
  goo_save_path="/home/ddd/data/sp3/sp3_papers/google/google_out_suc/"
  bai_opers.save(bai_fileToList,bai_ori_path,bai_save_path)
  goo_opers.save(goo_fileToList,goo_ori_path,goo_save_path)
  print("\nFile copy done!\n")
