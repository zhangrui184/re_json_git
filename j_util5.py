#正确，在使用，处理数据第二步
# 目标：第二次，使用多个关键词提取introduction，使用关键词表keywords_path='/home/ddd/data/pc2/ad1_result/intro_keywords.txt'
#     处理/home/ddd/data/pc2/ad1_result/ad1_papers_json/内容 的introduction和abstract提取出来
#     存到/home/ddd/data/pc2/ad1_result/ad1_papers_json_art3/ 和/home/ddd/data/pc2/ad1_result/ad1_papers_json_abs3/中
#功能：处理第二次的数据集，获取introduction 和abstract  
#     记录重复的index是没有看是否已存在     
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
 
  #获取最终Introduction和abstract
  def get_content_list(self,file_metadata_list,art_paper_path,abs_paper_path,keywords):
    all_abstractText=[]#所有的abstract
    index=0
    all_Introduction=[]#所有的introduction
    all_art_filenames=[]
    all_abs_filenames=[]
    no_cor_txt=[]#获取introduction和abstract时候有误的index集合
    a=' '
    no_cor_txt.append(a)
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
           no_cor_txt.append(str(index))
        all_abstractText.append(a_abstractText)
        a_sections=a_file_metadata_list['sections']
        try:
           a_Introduction_section0=a_sections[0]
           a_Introduction_section0_title=a_Introduction_section0['heading']
           ans0 =self.get_ex_ans(keywords,str(a_Introduction_section0_title)) 
        except Exception:
           ans0 = False
        
        try:
           a_Introduction_section1=a_sections[1]
           a_Introduction_section1_title=a_Introduction_section1['heading']
           ans1 =self.get_ex_ans(keywords,str(a_Introduction_section1_title)) 
        except Exception:
           ans1 = False
        
        try:
           a_Introduction_section2=a_sections[2]
           a_Introduction_section2_title=a_Introduction_section2['heading']
           ans2 =self.get_ex_ans(keywords,str(a_Introduction_section2_title)) 
        except Exception:
           ans2 = False
        
        try:
           a_Introduction_section3=a_sections[3]
           a_Introduction_section3_title=a_Introduction_section3['heading']     
           ans3 =self.get_ex_ans(keywords,str(a_Introduction_section3_title)) 
        except Exception:
           ans3 = False
        
        try:
           a_Introduction_section4=a_sections[4]
           a_Introduction_section4_title=a_Introduction_section4['heading']     
           ans4 =self.get_ex_ans(keywords,str(a_Introduction_section4_title)) 
        except Exception:
           ans4 = False

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
        elif ans4 is True:
           this_section=a_Introduction_section4
           a_Introduction=this_section['text']
        else:
           a_Introduction=''
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
    return no_cor_txt,spe_file
  
  def write_txt(self,txt_path,content,index,spe_file):
    with open(txt_path,'w') as f1:
      try:
         f1.write(content)
      except Exception:
           spe_file.append(str(index))
    return spe_file

  def get_keywords(self,keywords_path):
      new_key=[]
      with open (keywords_path,'r') as f_k:
          keywords=f_k.readlines()
      for k in keywords:
          new=k.strip()
          new_key.append(new)
      return new_key

  def get_ex_ans(self,keywords,a_Introduction):
      for keyword in keywords:
          try:
             ans =keyword in a_Introduction
          except Exception:
              ans=False
          if ans is True:
              break
      return ans

if __name__ == '__main__':
  '''例子
  file_path='/home/ddd/data/re_json/test/'
  art_paper_path='/home/ddd/data/re_json/test_art2/'
  abs_paper_path='/home/ddd/data/re_json/test_abs2/'
  no_cor_txt_file='/home/ddd/data/re_json/no_cor_txt_file.txt'
  spe_file_file='/home/ddd/data/re_json/spe_file_file.txt'
  '''
  file_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json/'
  art_paper_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json_art3/'
  abs_paper_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json_abs3/'
  no_cor_txt_file='/home/ddd/data/pc2/ad1_result/no_cor_txt_file3.txt'
  spe_file_file='/home/ddd/data/pc2/ad1_result/spe_file_file3.txt'
  #'''
  keywords_path='/home/ddd/data/pc2/ad1_result/intro_keywords.txt'
  opers = OperationJson(file_path=file_path)#创建实例
  keywords=opers.get_keywords(keywords_path)
  file_path_list=opers.get_file_path_list()#获得存json的名称列表list
  file_metadata_list=opers.read_file(file_path_list)#获得每一行json信息的文件列表list
  no_cor_txt,spe_file=opers.get_content_list(file_metadata_list,art_paper_path,abs_paper_path,keywords)#获得最终的index和DOI列表list
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
