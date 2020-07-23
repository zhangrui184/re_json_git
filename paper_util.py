#没写完
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
    ex_index_list=[]
    suc_pdf_list=[]
    filename_list=[]
    with open(self.file_name,encoding="utf-8") as fp:
         data = json.load(fp)
         metadata=data['paper_list']
         for i in range(len(metadata)):
              ex_index=metadata[i]['ex_index']
              suc_pdf=metadata[i]['suc_pdf']
              filename=metadata[i]['filename']
              ex_index_list.append(ex_index)
              suc_pdf_list.append(suc_pdf)
              filename_list.append(filename)
    fp.close()
    return data,ex_index_list,filename_list,suc_pdf_list
  
  #把suc_pdf为Flase的文件集合
  def get_ex_papers(self,ex_index_list,filename_list,suc_pdf_list):
    no_ex_filename=[]
    for i in range(len(ex_index_list)):
        if suc_pdf_list[i] is False:
            no_ex_filename.append(filename_list[i])
    return no_ex_filename
  
  #清除没有的论文信息
  def clean_paper(self,no_ex_filename,cl_filename):
    with open(cl_filename, 'a', encoding='utf-8') as f:
        for paper in json_papers:
            f.write(json.dumps(paper, ensure_ascii=False) + '\n')


if __name__ == '__main__':
  opers = OperationJson(file_name='/home/ddd/data/sp3/sp3_papers/baidu_xueshu_all_2.2.json')
  data,ex_index_list,filename_list,suc_pdf_list=opers.get_data()
  no_ex_filename=opers.get_ex_papers(ex_index_list,filename_list,suc_pdf_list)
  #for no_ex in no_ex_filename:
  #    print(no_ex)
  print('ss')
  # print(opers.get_value('name'))
  