# http://usaco.org/index.php?page=viewproblem2&cpid=667

input_file = open("citystate.in","r")
output_file = open("citystate.out","w")

n = int(input_file.readline())

combo_dict = {}

for i in range(n):
    read_data = input_file.readline().split()
    combo = read_data[0][:2] + read_data[1]
    
    if read_data[0][:2] != read_data[1]:
        if combo not in combo_dict:
            combo_dict[combo] = 1
        else:
            combo_dict[combo] += 1

result = 0

for combo in combo_dict:
    pair_combo = combo[2:] + combo[:2]
    
    if pair_combo in combo_dict:
        result += combo_dict[pair_combo] * combo_dict[combo]

output_file.write(str(result//2)+"\n")