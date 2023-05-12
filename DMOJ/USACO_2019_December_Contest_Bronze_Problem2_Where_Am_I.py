# http://usaco.org/index.php?page=viewproblem2&cpid=964

input_file = open('whereami.in','r')
output_file = open('whereami.out','w')

n = int(input_file.readline().strip())
mails = input_file.readline()

def make_mail_list(x,mails):
    '''메일박스를 n개만큼 나눠서 리스트로 저장'''
    new_mail_list = []
    for i in range(0,len(mails)):
        new_mail_list.append(mails[i:i+x])
    return new_mail_list

#main
count = 0
while True:
    count += 1
    split_mail_list = make_mail_list(count,mails)
    if len(set(split_mail_list)) != len(split_mail_list):
        continue
    if len(set(split_mail_list)) == len(split_mail_list):
        break

output_file.write(str(count))
input_file.close()
output_file.close()
