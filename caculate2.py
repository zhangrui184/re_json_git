#正确
# 计算第二次下载的论文有多少篇，14905篇pdf
import os
paper_path_e='/home/ddd/data/pc2/ad1_result/ad1_papers/'



#获取json文件名称存为list
def get_numbers(file_path):
    file_path_list=[]
    files = os.listdir(file_path)
    # 获取json类型的文件放到一个列表里面
    wdfiles = [f for f in files if f.endswith((".pdf"))]
    for wdfile in wdfiles:
        wdfile_path=file_path+wdfile
        file_path_list.append(wdfile_path)
    numbers=len(file_path_list)
    return numbers

numbers=get_numbers(paper_path_e)
print(str(numbers))  #14905篇pdf