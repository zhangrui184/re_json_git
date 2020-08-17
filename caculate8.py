#正确，计算18926和14890的对应数字  
#coding=utf-8
import json
import os
from collections import namedtuple

#获取json文件名称存为list
def get_file_path_list(file_path):
    file_path_list=[]
    files = os.listdir(file_path)
    # 获取json类型的文件放到一个列表里面
    wdfiles = [f for f in files if f.endswith((".txt"))]
    for wdfile in wdfiles:
        wdfile_path=file_path+wdfile
        file_path_list.append(wdfile_path)
    return file_path_list

def get_first_file_path_list(file_path):
    file_path_list=[]
    files = os.listdir(file_path)
    # 获取json类型的文件放到一个列表里面
    wdfiles = [f for f in files if f.endswith((".json"))]
    for wdfile in wdfiles:
        wdfile_path=file_path+wdfile
        file_path_list.append(wdfile_path)
    return file_path_list

def de_secon_title(secon_file_path_list):
    de_secon_str='/home/ddd/data2/ad5/art5/'
    de_secon_str2='_art.txt'
    all_secon_nums=[]
    for secon in secon_file_path_list:
        new_secon=secon.replace(de_secon_str,'')
        new_secon2=new_secon.replace(de_secon_str2,'')
        all_secon_nums.append(new_secon2)
    return all_secon_nums

def de_first_title(first_file_path_list):
    de_first_str='/home/ddd/data/pc2/ad1_result/ad1_papers_json/'
    de_first_str2='_papers.pdf.json'
    all_first_nums=[]
    for first in first_file_path_list:
        new_first=first.replace(de_first_str,'')
        new_first2=new_first.replace(de_first_str2,'')
        all_first_nums.append(new_first2)
    return all_first_nums


def de_four_title(first_file_path_list):
    de_first_str='/home/ddd/data/pc2/ad1_result/ad1_papers_json_art3/'
    de_first_str2='_art.txt'
    all_first_nums=[]
    for first in first_file_path_list:
        new_first=first.replace(de_first_str,'')
        new_first2=new_first.replace(de_first_str2,'')
        all_first_nums.append(new_first2)
    return all_first_nums

def get_content(third_path):
    all_third_nums=[]
    with open(third_path,'r') as f:
        numbers=f.readlines()
        for num in numbers:
            nums=num.replace('\n','')
            all_third_nums.append(nums)
    return all_third_nums


def write(num_to_num_file_path,a_name,all_a_nums,b_name,all_b_nums):
    with open(num_to_num_file_path,'w') as f:
        for i in range(len(all_a_nums)):
            num_to_num=a_name+' '+all_a_nums[i]+' '+b_name+' '+all_b_nums[i]
            f.write(num_to_num)

first_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json/'#就是14890对应的编码
first_path_name='ad1_papers_json'
four_path='/home/ddd/data/pc2/ad1_result/ad1_papers_json_art3/'
four_path_name='ad1_papers_json_art3'
secon_path='/home/ddd/data2/ad5/art5/'
secon_path_name='art5'
third_path='/home/ddd/data/pc2/ad1_result/cacul5/all_yes_size_file.txt'#就是7954对应的编码
#num_to_num_file_path='/home/ddd/data2/ad5_result/num_to_num_file.txt'错误，这是把序号重新排序了，所以对应不上了，错误
num_to_num_file_path='/home/ddd/data2/ad5_result/num_to_num_file2.txt'

first_file_path_list=get_first_file_path_list(first_path)
all_first_nums=de_first_title(first_file_path_list)#14890
'''帮助学习参数
secon_file_path_list=get_file_path_list(secon_path)
all_secon_nums=de_secon_title(secon_file_path_list)#7954 从0-7953

all_third_nums=get_content(third_path)#7954

four_file_path_list=get_file_path_list(four_path)
all_four_nums=de_four_title(four_file_path_list)#14890 从0-14889

write(num_to_num_file_path,all_first_nums,all_four_nums)#这行代码没写完

four_file_path_list=get_file_path_list(four_path)
all_four_nums=de_four_title(four_file_path_list)#14890 从0-14889
all_four_nums_s=list(map(int,all_four_nums))
all_four_nums_s.sort()
b=all_four_nums_s
'''
#all_first_nums_s=list(map(int,all_first_nums))
#all_first_nums_s.sort()
#a=all_first_nums_s
with open(num_to_num_file_path,'w') as f:
    for num in all_first_nums:
        f.write(str(num)+'\n')
