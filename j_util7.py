##错误的过程
#  
# 方法一：
# 将art和abs都有size的文件存到/home/ddd/data/pc2/ad1_result/ad1_papers_json_abs6/
#               和/home/ddd/data/pc2/ad1_result/ad1_papers_json_abs6/中
#共7954个txt
#
# 方法二：
#第二次测abs3----yes_size_numbers_path='/home/ddd/data/pc2/ad1_result/3_yes_size_numbers2.txt'
#第二次测abs7----yes_size_numbers_path='/home/ddd/data/pc2/ad1_result/7_yes_size_numbers.txt'
#
# 方法三：
# 根据yes_size_numbers_path存在size的列表，将/home/ddd/data/pc2/ad1_result/ad1_papers_json_art3/复制文件到/home/ddd/data/pc2/ad1_result/cacul5/art1/
import os
from shutil import copyfile

def copy(index_list,src_paper_path,tar_paper_path):
    i=0
    no_copy_list=[]
    for index in index_list:
            #art_filename='%05d_art.txt'%index
            src_txt_path = os.path.join(src_paper_path, "%05d_abs.txt" % int(index)) 
            tar_txt_path = os.path.join(tar_paper_path, "%05d_abs.txt" % int(index)) 
            try:
               copyfile(src_txt_path, tar_txt_path)
            except Exception:
                no_copy_list.append(i)
            print('already get: '+str(i))
            i+=1
    return no_copy_list

def copy_art(index_list,src_paper_path,tar_paper_path):
    i=0
    no_copy_list=[]
    for index in index_list:
            #art_filename='%05d_art.txt'%index
            src_txt_path = os.path.join(src_paper_path, "%05d_art.txt" % int(index)) 
            tar_txt_path = os.path.join(tar_paper_path, "%05d_art.txt" % int(index)) 
            try:
               copyfile(src_txt_path, tar_txt_path)
            except Exception:
                no_copy_list.append(i)
            print('already get: '+str(i))
            i+=1
    return no_copy_list
#3-5-6 3-7-8
art_paper_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json_art3/'
abs_paper_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json_abs3/'
art2_paper_path='/home/ddd/data/pc2/ad1_result/cacul5/art1/'
abs2_paper_path='/home/ddd/data/pc2/ad1_result/cacul5/abs1/'
yes_size_numbers_path='/home/ddd/data/pc2/ad1_result/cacul5/all_yes_size_file.txt'
no_copy_list_path='/home/ddd/data/pc2/ad1_result/no_copy_list.txt'
all_num=[]
with open(yes_size_numbers_path,'r') as f:
    numbers=f.readlines()
for num in numbers:
    nums=num.strip()
    all_num.append(nums)

no_copy_list=copy_art(all_num,art_paper_path,art2_paper_path)

with open(no_copy_list_path,'w') as f_no:
    for a_no in no_copy_list:
        f_no.write(str(a_no)+'\n')

no_abs_list=copy(all_num,abs_paper_path,abs2_paper_path)
with open(no_copy_list_path,'w') as f_no:
    for a_no in no_abs_list:
        f_no.write(str(a_no)+'\n')
