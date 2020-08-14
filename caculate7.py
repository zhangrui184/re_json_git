# 正确，可运行，帮助计算
# 将all_num的数字，去除all_num_de后，得到all_num2列表

yes_size_numbers_path='/home/ddd/data/pc2/ad1_result/cacul5/src_copy_no_size_list.txt'
all_num_de=[]
all_num=[]
all_num2=[]
with open(yes_size_numbers_path,'r') as f:
    numbers=f.readlines()
for num in numbers:
    nums=num.strip()
    all_num_de.append(nums)
all_yes_size_file='/home/ddd/data/pc2/ad1_result/cacul5/all_yes_size_file.txt'
all_yes_size_file2='/home/ddd/data/pc2/ad1_result/cacul5/all_yes_size_file2.txt'
with open(all_yes_size_file,'r') as f:
    numbers=f.readlines()
for num in numbers:
    nums=num.strip()
    all_num.append(nums)

for n in all_num:
    ans=False
    for n_de in all_num_de:
        if n == n_de:
          ans = True
          break
    if ans is False:
       all_num2.append(n)

with open(all_yes_size_file2,'w') as f:
    for a_n in all_num2:
        f.write(str(a_n)+'\n')
all_num2_num=len(all_num2)
print(str(all_num2_num))