#正确
# 统计heading的类型
#计算第二次下载的论文的json文件中，heading类型有多少
#/home/ddd/data/pc2/ad1_result/all_heading_file.txt取content的第一个、第二个、第三个heading
#/home/ddd/data/pc2/ad1_result/all_heading_file2.txt取content的第一个、第二个heading
#/home/ddd/data/pc2/ad1_result/all_heading_file3.txt取content的第一个heading
#/home/ddd/data/pc2/ad1_result/all_heading_file4.txt取content的第二个heading
import os
import json
#paper_path_e='/home/ddd/data/pc2/ad1_result/ad1_papers/'
#art_paper_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json_art2/'
#abs_paper_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json_abs2/'

class OperationJson:
  def __init__(self,file_path=None):  
    if file_path:
      self.file_path = file_path
    else:
      self.file_path = '/home/ddd/data/re_json/test/'#测试的数据集
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

  #读取json文件
  def convertList(self,file_name):
    with open(file_name,encoding="utf-8") as fp:
         data = json.load(fp)
         metadata=data["metadata"]
    return metadata

  #读取json每一行信息，获得一个file_list的信息
  def read_file(self,filepath_list):
    file_metadata_list=[]
    for filename in filepath_list:
         metadata=self.convertList(file_name=filename)
         file_metadata_list.append(metadata) 
    return file_metadata_list  

  def get_heading_list(self,file_metadata_list):
    all_heading=[]#所有的abstract
    all_heading.append('Introduction')
    index=0
    for a_file_metadata_list in file_metadata_list:
        a_section=a_file_metadata_list['sections']
        '''
        try:
           a_section0=a_section[0]
           a_section0_heading=a_section0['heading']
           if a_section0_heading is None:
               a_section0_heading='Y'
        except Exception:
           a_section0_heading='I'

        '''
        try:
           a_section1=a_section[1]
           a_section1_heading=a_section1['heading']
           if a_section1_heading is None:
               a_section1_heading='Y'
        except Exception:
           a_section1_heading='I'
        
        '''
        try:
           a_section2=a_section[2]
           a_section2_heading=a_section2['heading']
           if a_section2_heading is None:
               a_section2_heading='Y'
        except Exception:
           a_section2_heading='I'
        '''
        '''
        for a_all_heading in all_heading:
            try:
               ans0=a_section0_heading in a_all_heading
            except Exception:
                ans0=False
            if ans0 is True:
                break
        if ans0 is False:
           all_heading.append(a_section0_heading)
        
        '''
        for a_all_heading in all_heading:
            try:
               ans1=a_section1_heading in a_all_heading
            except Exception:
                ans1=False
            if ans1 is True:
                break
        if ans1 is False:
               all_heading.append(a_section1_heading)
        
        '''
        for a_all_heading in all_heading:
            try:
               ans2=a_section2_heading in a_all_heading
            except Exception:
                ans2=False
            if ans2 is True:
                break
        if ans2 is False:
               all_heading.append(a_section2_heading)
        '''
        #print('already:'+str(index))
        index +=1
    return all_heading


if __name__ == '__main__':
  file_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json/'
  all_heading_file='/home/ddd/data/pc2/ad1_result/all_heading_file4.txt'
  opers = OperationJson(file_path=file_path)#创建实例
  file_path_list=opers.get_file_path_list()#获得存json的名称列表list
  file_metadata_list=opers.read_file(file_path_list)#获得每一行json信息的文件列表list
  all_heading=opers.get_heading_list(file_metadata_list)#获得最终的index和DOI列表list
  with open(all_heading_file,'w') as f2:
       for line in all_heading:
           f2.write(line+'\n')
           print('all_heading: '+str(line))  
