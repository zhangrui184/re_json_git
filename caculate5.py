#错误的过程
# 这里的index计算有误
# 计算paper_path_e和paper_path_e2中都存在size的文件列表，输出为all_yes_size_file
#
import os
#paper_path_e='/home/ddd/data/pc2/ad1_result/ad1_papers_json_art3/'
paper_path_e2='/home/ddd/data/pc2/ad1_result/ad1_papers_json_abs3/'

#paper_path_e='/home/ddd/data/pc2/ad1_result/cacul5/art1/'
#paper_path_e2='/home/ddd/data/pc2/ad1_result/cacul5/abs1/'

#获取json文件名称存为list
def get_numbers(file_path):
    file_path_list=[]
    files = os.listdir(file_path)
    # 获取json类型的文件放到一个列表里面
    wdfiles = [f for f in files if f.endswith((".txt"))]
    index=0
    all_size=[]
    no_size=[]
    yes_size=[]
    for wdfile in wdfiles:
        wdfile_path=file_path+wdfile
        size=os.path.getsize(wdfile_path)
        file_path_list.append(wdfile_path)
        all_size.append(size)
        if size ==0:
            no_size.append(str(index))
        else:
            yes_size.append(str(index))
        index +=1
    numbers=len(file_path_list)
    no_size_numbers=len(no_size)
    yes_size_numbers=len(yes_size)

    return numbers,no_size_numbers,no_size,yes_size,yes_size_numbers
def diff(art_yes_size,abs_yes_size):
    all_yes_size=[]
    for a_art_yes_size in art_yes_size:
        for a_abs_yes_size in abs_yes_size:
            ans =a_art_yes_size in a_abs_yes_size
            if ans is True:
                break
        if ans is True:
            all_yes_size.append(a_art_yes_size)
    return all_yes_size

def get_numbers(size_numbers_path):
    all_num=[]
    with open(size_numbers_path,'r') as f:
        numbers=f.readlines()
    for num in numbers:
        nums=num.strip()
        all_num.append(nums)
    return all_num

#用index查看原abs3中的size大小，发现index使用有误
def get_ex_numbers(all_num,file_path):
    all_size=[]
    no_size=[]
    yes_size=[]
    for index in all_num:
        src_txt_path = os.path.join(file_path, "%05d_abs.txt" % int(index))    
        size=os.path.getsize(src_txt_path)
        all_size.append(size)
        if size ==0:
            no_size.append(str(index))
        else:
            yes_size.append(str(index))
    numbers=len(all_num)
    no_size_numbers=len(no_size)
    yes_size_numbers=len(yes_size)

    return numbers,no_size_numbers,no_size,yes_size,yes_size_numbers
'''例子
a='/home/ddd/data/pc2/ad1_result/ad1_result.json'
a1=os.path.getsize(a)
if a1==0:
    a1='iii'
print(str(a1))
'''
size_numbers_path='/home/ddd/data/pc2/ad1_result/cacul5/abs_no_size_numbers.txt'
all_num=get_numbers(size_numbers_path)
art_numbers,art_no_size_numbers,art_no_size,art_yes_size,art_yes_size_numbers=get_numbers(paper_path_e)
abs_numbers,abs_no_size_numbers,abs_no_size,abs_yes_size,abs_yes_size_numbers=get_numbers(all_num,paper_path_e2)
all_yes_size=diff(art_yes_size,abs_yes_size)
all_yes_size_number=len(all_yes_size)
all_yes_size_file='/home/ddd/data/pc2/ad1_result/cacul5/all_yes_size_file.txt'

#with open(all_yes_size_file,'w') as f:
#    for a_all_yes_size in all_yes_size:
#        f.write(a_all_yes_size+'\n')
'''
print('art_numbers: '+str(art_numbers))  #共多少
print('art_no_size_numbers: '+str(art_no_size_numbers))  #size为0的有多少
print('art_yes_size_numbers: '+str(art_yes_size_numbers))  #size不为0的多少
'''
print('abs_numbers: '+str(abs_numbers))  #共多少
print('abs_no_size_numbers: '+str(abs_no_size_numbers))  #size为0的有多少
print('abs_yes_size_numbers: '+str(abs_yes_size_numbers))  #size不为0的多少
#print('all_yes_size_number: '+str(all_yes_size_number))  #size不为0的多少
abs_no_size_numbers_path='/home/ddd/data/pc2/ad1_result/cacul5/abs_no_size_numbers.txt'


'''-----------------------------------------------------------------------------------------------------------
帮助学习参数
art_no_size_numbers_path='/home/ddd/data/pc2/ad1_result/cacul5/art_no_size_numbers.txt'
abs_no_size_numbers_path='/home/ddd/data/pc2/ad1_result/cacul5/abs_no_size_numbers.txt'
with open(art_no_size_numbers_path,'w') as f_n_s:#size为0的index输出到文件no_size_numbers.txt中
    for a_size in art_no_size:
        f_n_s.write(str(a_size)+'\n')
with open(abs_no_size_numbers_path,'w') as f_n_s:#size为0的index输出到文件no_size_numbers.txt中
    for a_size in abs_no_size:
        f_n_s.write(str(a_size)+'\n')        

art_yes_size_numbers_path='/home/ddd/data/pc2/ad1_result/cacul5/art_yes_size_numbers.txt'
abs_yes_size_numbers_path='/home/ddd/data/pc2/ad1_result/cacul5/abs_yes_size_numbers.txt'
-----------------------
with open(art_yes_size_numbers_path,'w') as f_n_s:#size不为0的index输出到文件yes_size_numbers.txt中
    for a_size in art_yes_size:
        f_n_s.write(str(a_size)+'\n')
with open(abs_yes_size_numbers_path,'w') as f_n_s:#size不为0的index输出到文件yes_size_numbers.txt中
    for a_size in abs_yes_size:
        f_n_s.write(str(a_size)+'\n')
'''
