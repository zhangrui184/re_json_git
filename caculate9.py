#统计/home/ddd/data2/ad6/中含有doi和Corresponding author的有多少
#原文件：/home/ddd/data2/ad6/中的txt 
#保存到：/home/ddd/data2/test_my/中的txt
def all_content(ori_file_path):
    all_content=[]
    with open(ori_file_path,'r') as f:
       contents=f.readlines()
    for num in contents:
       nums=num.strip()
       all_content.append(nums)
    return all_content

def new_content(all_content):
    doi='doi'
    index =0
    doi_content=[]
    au_content=[]
    for con in all_content:
        ans =False
        try:
           ans=doi in con
        except Exception:
            ans =False
        if ans is True:
            index+=1
            doi_content.append(con)
    Corresponding_author_str='Corresponding author'
    au_index=0
    for con in all_content:
        ans =False
        try:
           ans=Corresponding_author_str in con
        except Exception:
            ans =False
        if ans is True:
            au_index+=1
            au_content.append(con)
    return index,au_index,doi_content,au_content

train_save_path='/home/ddd/data2/ad6/train.txt'
val_save_path='/home/ddd/data2/ad6/val.txt'
test_save_path='/home/ddd/data2/ad6/test.txt'
doi_content_path='/home/ddd/data2/test_my/doi_content.txt'
au_content_path='/home/ddd/data2/test_my/au_content.txt'
train_all_content=all_content(train_save_path)
train_index,train_au_index,doi_content,au_content=new_content(train_all_content)
with open(doi_content_path,'w') as f_doi:#将有doi的文件内容保存到文件
    for a_con in doi_content:
        f_doi.write(a_con+'\n')
with open(au_content_path,'w') as f_au:#将含有author的内容保存到文件
    for a_au_con in au_content:
        f_au.write(a_au_con+'\n')
print('finished')


val_all_content=all_content(val_save_path)
val_index,val_au_index,_,_=new_content(val_all_content)

test_all_content=all_content(test_save_path)
test_index,test_au_index,_,_=new_content(test_all_content)

print('train: '+str(train_index))#1984
print('val: '+str(val_index))#379
print('test: '+str(test_index))#619
print('train au: '+str(train_au_index))#1734
print('val au: '+str(val_au_index))#262
print('test au: '+str(test_au_index))#468
