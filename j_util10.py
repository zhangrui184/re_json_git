#正确，在使用，处理数据第五步
#功能：把
#      Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. SBCARS 2017, September 18–19, 2017, Fortaleza, CE, Brazil © 2017 Association for Computing Machinery. ACM ISBN 978-1-4503-5325-0/17/09. . . $15.00 https://doi.org/10.1145/3132498.3132510.
#      去掉
#      复制/home/ddd/data2/ad5_result/到/home/ddd/data2/ad6/
import os

def all_content(ori_file_path):
    all_content=[]
    with open(ori_file_path,'r') as f:
       contents=f.readlines()
    for num in contents:
       nums=num.strip()
       all_content.append(nums)
    return all_content


Corresponding_author_str='Corresponding author'

def get_new_content(all_content):
    Permission_str='Permission to make digital or hard copies'
    doi_str='doi'
    new_all_content=[]
    index=0
    for con in all_content:
       Permission_str_position=con.find(Permission_str)
       doi_str_position=con.find(doi_str)
       new_con=con
       if doi_str_position !=-1:
          doi_str_all=doi_str_position+32
       if doi_str_position!=-1 & Permission_str_position!=-1:
          de_str=con[Permission_str_position:doi_str_all]
          new_con=con.replace(de_str,'')
          index+=1
       new_all_content.append(new_con)
    return new_all_content,index

def write_file(new_all_content,new_file_name):
    with open(new_file_name,'w') as f:
        for new_con in new_all_content:
            f.write(new_con+'\n')
'''例子
test_my_path='/home/ddd/data2/test_my/test_small.txt'
test_my_save_path='/home/ddd/data2/test_my/test_small_cor.txt'
'''
train_path='/home/ddd/data2/ad5_result/train_cor.txt'
val_path='/home/ddd/data2/ad5_result/val.txt'
test_path='/home/ddd/data2/ad5_result/test.txt'
train_save_path='/home/ddd/data2/ad6/train.txt'
val_save_path='/home/ddd/data2/ad6/val.txt'
test_save_path='/home/ddd/data2/ad6/test.txt'
'''例子
all_content=all_content(test_my_path)
new_all_content=get_new_content(all_content)
write_file(new_all_content,test_my_save_path)
'''
train_all_content=all_content(train_path)
train_new_all_content,train_index=get_new_content(train_all_content)

write_file(train_new_all_content,train_save_path)

val_all_content=all_content(val_path)
val_new_all_content,val_index=get_new_content(val_all_content)
write_file(val_new_all_content,val_save_path)

test_all_content=all_content(test_path)
test_new_all_content,test_index=get_new_content(test_all_content)
write_file(test_new_all_content,test_save_path)
print('train change: '+str(train_index))#544
print('val change: '+str(val_index))#0
print('test change: '+str(test_index))#7