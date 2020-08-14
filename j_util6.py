#错误的过程

# 将art有size的文件存到/home/ddd/data/pc2/ad1_result/ad1_papers_json_abs5/
#               和/home/ddd/data/pc2/ad1_result/ad1_papers_json_abs5/中
#共8300个txt
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


art_paper_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json_art3/'
abs_paper_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json_abs3/'
art2_paper_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json_art5/'
abs2_paper_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json_abs5/'
no_size_numbers_path='/home/ddd/data/pc2/ad1_result/yes_size_numbers.txt'
no_copy_list_path='/home/ddd/data/pc2/ad1_result/no_copy_list.txt'
all_num=[]
with open(no_size_numbers_path,'r') as f:
    numbers=f.readlines()
for num in numbers:
    nums=num.strip()
    all_num.append(nums)
no_copy_list=copy(all_num,art_paper_path,art2_paper_path)
no_abs_list=copy(all_num,abs_paper_path,abs2_paper_path)
with open(no_copy_list_path,'w') as f_no:
    for a_no in no_copy_list:
        f_no.write(str(a_no)+'\n')
with open(no_copy_list_path,'w') as f_no:
    for a_no in no_abs_list:
        f_no.write(str(a_no)+'\n')