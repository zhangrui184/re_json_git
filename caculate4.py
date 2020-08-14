#正确
# 计算第二次去掉size为0的json的论文paper_path_e中size为0的多少
#计算第二次去掉size为0的json的论文paper_path_e2中size为0的多少
import os
paper_path_e='/home/ddd/data/pc2/ad1_result/ad1_papers_json_art3/'#计算size为0的多少
paper_path_e2='/home/ddd/data/pc2/ad1_result/ad1_papers_json_abs5/'#计算size为0的多少
paper_path_e3='/home/ddd/data/pc2/ad1_result/ad1_papers_json_art6/'
paper_path_e4='/home/ddd/data/pc2/ad1_result/ad1_papers_json_art8/'
paper_path_e5='/home/ddd/data/pc2/ad1_result/cacul5/abs1/'
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

'''
a='/home/ddd/data/pc2/ad1_result/ad1_result.json'
a1=os.path.getsize(a)
if a1==0:
    a1='iii'
print(str(a1))
'''
numbers,no_size_numbers,no_size,yes_size,yes_size_numbers=get_numbers(paper_path_e5)
print(str(numbers))  #共多少
print(str(no_size_numbers))  #size为0的有多少
print(str(yes_size_numbers))  #size不为0的多少
'''
no_size_numbers_path='/home/ddd/data/pc2/ad1_result/8_no_size_numbers.txt'
with open(no_size_numbers_path,'w') as f_n_s:#size为0的index输出到文件no_size_numbers.txt中
    for a_size in no_size:
        f_n_s.write(str(a_size)+'\n')

yes_size_numbers_path='/home/ddd/data/pc2/ad1_result/8_yes_size_numbers.txt'
with open(yes_size_numbers_path,'w') as f_n_s:#size不为0的index输出到文件yes_size_numbers.txt中
    for a_size in yes_size:
        f_n_s.write(str(a_size)+'\n')
'''