#目标：处理/home/ddd/data/pc2/ad1_result/ad1_papers_json/内容 的introduction和abstract提取出来
#     存到/home/ddd/data/pc2/ad1_result/ad1_papers_json_art2/ 和/home/ddd/data/pc2/ad1_result/ad1_papers_json_abs2/中
#功能：处理第二次的数据集，获取introduction 和abstract       
#coding=utf-8
import json
import os
from collections import namedtuple

class OperationJson:
  def __init__(self,file_path=None):  
    if file_path:
      self.file_path = file_path
    else:
      self.file_path = '/home/ddd/data/re_json/test/'#测试的数据集
  
  #读取json文件
  def convertList(self,file_name):
    with open(file_name,encoding="utf-8") as fp:
         data = json.load(fp)
         metadata=data["metadata"]
    return metadata
 
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
  def get_content_list(self,file_metadata_list,art_paper_path,abs_paper_path):
    all_abstractText=[]#所有的abstract
    index=0
    all_Introduction=[]#所有的introduction
    all_art_filenames=[]
    all_abs_filenames=[]
    no_cor_txt=[]#获取introduction和abstract时候有误的index集合
    spe_file=[]#存写文件时候有误的index集合
    Introduction_str='Introduction'
    for a_file_metadata_list in file_metadata_list:
        try:
           a_abstractText=a_file_metadata_list['abstractText']
        except Exception:
           a_abstractText=''
           no_cor_txt.append(str(index))
        if a_abstractText is None:
           a_abstractText=''
           for a_no in no_cor_txt:#判断此index是否已经被写入
               ans_no =str(index) in a_no
               if ans_no is False:
                   no_cor_txt.append(str(index))
        all_abstractText.append(a_abstractText)
        a_sections=a_file_metadata_list['sections']
        try:
           a_Introduction_section0=a_sections[0]
           a_Introduction_section0_title=a_Introduction_section0['heading']
           ans0 =Introduction_str in str(a_Introduction_section0_title) 
        except Exception:
           ans0 = False
        try:
           a_Introduction_section1=a_sections[1]
           a_Introduction_section1_title=a_Introduction_section1['heading']
           ans1 =Introduction_str in str(a_Introduction_section1_title)
        except Exception:
           ans1 = False
        try:
           a_Introduction_section2=a_sections[2]
           a_Introduction_section2_title=a_Introduction_section2['heading']
           ans2 =Introduction_str in str(a_Introduction_section2_title) 
        except Exception:
           ans2 = False
        try:
           a_Introduction_section3=a_sections[3]
           a_Introduction_section3_title=a_Introduction_section3['heading']     
           ans3 =Introduction_str in str(a_Introduction_section3_title) 
        except Exception:
           ans3 = False
          
        if ans0 is True:
           this_section=a_Introduction_section0
           a_Introduction=this_section['text']
        elif ans1 is True:
           this_section=a_Introduction_section1
           a_Introduction=this_section['text']
        elif ans2 is True:
           this_section=a_Introduction_section2
           a_Introduction=this_section['text']
        elif ans3 is True:
           this_section=a_Introduction_section3
           a_Introduction=this_section['text']
        else:
           a_Introduction=''
           for a_no in no_cor_txt:
               ans_no =str(index) in a_no#判断此index是否已经被写入
               if ans_no is False:
                   no_cor_txt.append(str(index))
        all_Introduction.append(a_Introduction)
        art_txt_path = os.path.join(art_paper_path, "%05d_art.txt" % index)
        spe_file=self.write_txt(art_txt_path,a_Introduction,index,spe_file)
        art_filename='%05d_art.txt'%index
        all_art_filenames.append(art_filename)
        abs_txt_path = os.path.join(abs_paper_path, "%05d_abs.txt" % index)
        spe_file=self.write_txt(abs_txt_path,a_abstractText,index,spe_file)
        abs_filename='%05d_abs.txt'%index
        all_abs_filenames.append(abs_filename)
        if index % 1==0:
             print('already get: '+str(index)+' txt')
        index +=1
    return all_abstractText,all_Introduction,all_art_filenames,all_abs_filenames,no_cor_txt,spe_file
  
  def write_txt(self,txt_path,content,index,spe_file):
    with open(txt_path,'w') as f1:
      try:
         f1.write(content)
      except Exception:
           spe_file.append(str(index))
    return spe_file



if __name__ == '__main__':
  '''例子
  file_path='/home/ddd/data/re_json/test/'
  art_paper_path='/home/ddd/data/re_json/test_art/'
  abs_paper_path='/home/ddd/data/re_json/test_abs/'
  '''
  file_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json/'
  art_paper_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json_art2/'
  abs_paper_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json_abs2/'
  #'''
  no_cor_txt_file='/home/ddd/data/pc2/ad1_result/no_cor_txt_file.txt'
  spe_file_file='/home/ddd/data/pc2/ad1_result/spe_file_file.txt'
  opers = OperationJson(file_path=file_path)#创建实例
  file_path_list=opers.get_file_path_list()#获得存json的名称列表list
  file_metadata_list=opers.read_file(file_path_list)#获得每一行json信息的文件列表list
  all_abstractText,all_Introduction,all_art_filenames,all_abs_filenames,no_cor_txt,spe_file=opers.get_content_list(file_metadata_list,art_paper_path,abs_paper_path)#获得最终的index和DOI列表list
  print('-------------------------------------------------------------------------------------------------------------------------------------------')
  with open(no_cor_txt_file,'w') as f2:
       for line in no_cor_txt:
           f2.write(line+'\n')
           print('no_cor_txt: '+str(line))
  print('*****************************************************************************************************************************************')
  with open(spe_file_file,'w') as f2:
       for line in spe_file:
           f2.write(line+'\n')
           print('spe_file: '+str(line))
  print('保存成功')  
