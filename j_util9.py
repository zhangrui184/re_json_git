#正确，在使用，处理数据第四步
#功能：文件名重新编码
#并复制/home/ddd/data/pc2/ad1_result/cacul5/art4/
#                   到/home/ddd/data2/ad5/art5/
#和复制/home/ddd/data/pc2/ad1_result/cacul5/art4/
#                   到/home/ddd/data2/ad5/abs5/
import os
from shutil import copyfile

def copy(index_list,src_paper_path,tar_paper_path):
    i=0
    no_copy_list=[]
    src_copy_no_size_list=[]
    tar_copy_no_size_list=[]
    for index in index_list:
            #art_filename='%05d_art.txt'%index
            src_txt_path = os.path.join(src_paper_path, "%05d_abs.txt" % int(index)) 
            tar_txt_path = os.path.join(tar_paper_path, "%05d_abs.txt" % int(i)) 
            try:
               copyfile(src_txt_path, tar_txt_path)
            except Exception:
                no_copy_list.append(index)
            print('already get: '+str(i))
            src_size=os.path.getsize(src_txt_path)
            if src_size==0:
                src_copy_no_size_list.append(index)
            tar_size=os.path.getsize(tar_txt_path)
            if tar_size==0:
                tar_copy_no_size_list.append(index)
            i+=1
    return no_copy_list,src_copy_no_size_list,tar_copy_no_size_list

def copy_art(index_list,src_paper_path,tar_paper_path):
    i=0
    no_copy_list=[]
    src_copy_no_size_list=[]
    tar_copy_no_size_list=[]#复制过来size为0的index
    for index in index_list:
            #art_filename='%05d_art.txt'%index
            src_txt_path = os.path.join(src_paper_path, "%05d_art.txt" % int(index)) 
            tar_txt_path = os.path.join(tar_paper_path, "%05d_art.txt" % int(i)) 
            try:
               copyfile(src_txt_path, tar_txt_path)
            except Exception:
                no_copy_list.append(index)
            print('already get: '+str(i))
            src_size=os.path.getsize(src_txt_path)
            if src_size==0:
                src_copy_no_size_list.append(index)
            tar_size=os.path.getsize(tar_txt_path)
            if tar_size==0:
                tar_copy_no_size_list.append(index)
            i+=1
    return no_copy_list,src_copy_no_size_list,tar_copy_no_size_list
#3-5-6 3-7-8

art_paper_path='/home/ddd/data/pc2/ad1_result/cacul5/art4/'
abs_paper_path='/home/ddd/data/pc2/ad1_result/cacul5/abs4/'
art2_paper_path='/home/ddd/data2/ad5/art5/'
abs2_paper_path='/home/ddd/data2/ad5/abs5/'
yes_size_numbers_path='/home/ddd/data/pc2/ad1_result/cacul5/all_yes_size_file.txt'
no_copy_list_path='/home/ddd/data2/ad5/result/no_copy_list.txt'
art_src_copy_no_size_list_path='/home/ddd/data2/ad5/result/art_src_copy_no_size_list.txt'
art_tar_copy_no_size_list_path='/home/ddd/data2/ad5/result/art_tar_copy_no_size_list.txt'
src_copy_no_size_list_path='/home/ddd/data2/ad5/result/src_copy_no_size_list.txt'
tar_copy_no_size_list_path='/home/ddd/data2/ad5/result/tar_copy_no_size_list.txt'
'''
abs_paper_path='/home/ddd/data/pc2/ad1_result/cacul5/abs2/'
abs2_paper_path='/home/ddd/data/pc2/ad1_result/cacul5/abs3/'
yes_size_numbers_path='/home/ddd/data/pc2/ad1_result/cacul5/src_copy_no_size_list.txt'
'''
all_num=[]
with open(yes_size_numbers_path,'r') as f:
    numbers=f.readlines()
for num in numbers:
    nums=num.strip()
    all_num.append(nums)

art_no_copy_list,art_src_copy_no_size_list,art_tar_copy_no_size_list=copy_art(all_num,art_paper_path,art2_paper_path)
art_no_copy_list_num=len(art_no_copy_list)
art_src_copy_no_size_list_num=len(art_src_copy_no_size_list)
art_tar_copy_no_size_list_num=len(art_tar_copy_no_size_list)

with open(no_copy_list_path,'w') as f_no:
    for a_no in art_no_copy_list:
        f_no.write(str(a_no)+'\n')

with open(art_src_copy_no_size_list_path,'w') as f_no:
    for a_no in art_src_copy_no_size_list:
        f_no.write(str(a_no)+'\n')
with open(art_tar_copy_no_size_list_path,'w') as f_no:
    for a_no in art_tar_copy_no_size_list:
        f_no.write(str(a_no)+'\n')


no_abs_list,src_copy_no_size_list,tar_copy_no_size_list=copy(all_num,abs_paper_path,abs2_paper_path)
no_abs_list_num=len(no_abs_list)
src_copy_no_size_list_num=len(src_copy_no_size_list)
tar_copy_no_size_list_num=len(tar_copy_no_size_list)

with open(no_copy_list_path,'w') as f_no:
    for a_no in no_abs_list:
        f_no.write(str(a_no)+'\n')
with open(src_copy_no_size_list_path,'w') as f_no:
    for a_no in src_copy_no_size_list:
        f_no.write(str(a_no)+'\n')
with open(tar_copy_no_size_list_path,'w') as f_no:
    for a_no in tar_copy_no_size_list:
        f_no.write(str(a_no)+'\n')
print('**************************************************************************************')
print('art_no_copy_list_num: '+str(art_no_copy_list_num))
print('art_src_copy_no_size_list_num: '+str(art_src_copy_no_size_list_num))
print('art_tar_copy_no_size_list_num: '+str(art_tar_copy_no_size_list_num))
print('---------------------------------------------------------------------------------------')
print('no_abs_list_num: '+str(no_abs_list_num))
print('src_copy_no_size_list_num: '+str(src_copy_no_size_list_num))
print('tar_copy_no_size_list_num: '+str(tar_copy_no_size_list_num))
