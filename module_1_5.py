immutable_var = 1,2,3,4,5,6,True,'Hi'
print(immutable_var)
# immutable_var[1] = 500
# кортеж хранит ссылку на список, а не сам список
mutable_list = 1,2,3,[1,2,3,4,100]
mutable_list [3][4] = 5

print(mutable_list)