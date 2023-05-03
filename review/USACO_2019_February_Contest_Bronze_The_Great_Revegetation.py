# http://usaco.org/index.php?page=viewproblem2&cpid=916

# TODO : 소들이 좋아하는 목초지 구하기
def find_pasture_for_cows(input_file,num_cows):
    """파일에서 각 소들이 좋아하는 목초지를 찾아 리스트로 반환합니다"""
    favorites = []
    for i in range(num_cows):
        file_line = list(map(int,input_file.readline().split()))
        favorites.append(file_line)
    
    return favorites

def cows_favorite(favorites,pasture):
    """해당 목초지를 좋아하는 소의 번호를 리스트로 출력합니다"""
    cows_favorite = []
    for i in range(len(favorites)):
        if pasture in favorites[i]:
            cows_favorite.append(i)
    
    return cows_favorite

# TODO : 해당 목초지에 할당할 수 없는 풀(=중복) 구하기
def check_used(favorites,cows,grass):
    used = []
    for cow in cows:
        first = favorites[cow][0]
        second = favorites[cow][1]
        if first < len(grass):
            used.append(grass[first])
        if second < len(grass):
            used.append(grass[second])
    
    return used
    

# TODO : 할당 가능한 풀 중 가장 작은 수의 풀 구하기
def min_grass(ban_grass):
    grass_type = 1
    while grass_type in ban_grass:
        grass_type += 1
                
    return grass_type

#main 
input_file = open('revegetate.in','r')
ouput_file = open('revegetate.out','w')

# TODO : 입력 처리
file_line = list(map(int,input_file.readline().split()))
num_pastures = file_line[0]
num_cows = file_line[1]

#각 소들이 좋아하는 목초지 리스트
favorites = find_pasture_for_cows(input_file,num_cows)
#목초지에 심어져 있는 풀 번호 리스트
grass_list = [0]
#목초지를 순회하면서 계산한다.
for i in range(1,num_pastures+1):
    # i번 목초지를 좋아하는 소 리스트
    cows = cows_favorite(favorites,i)
    
    #i번 목초지에 들어가서는 안되는 풀 (i 목초지를 좋아하는 소가 좋아하는 또 다른 목초지에 이미 풀이 심어져 있다면, 해당 풀은 i 목초지에 심을 수 없다.)
    ban_grass = check_used(favorites,cows,grass_list)
    
    #i번 목초지에 들어가서는 안되는 풀을 제외하고 가장 작은 수의 풀을 할당하여 준다.
    grass_list.append(min_grass(ban_grass))

# TODO : 출력 처리
def write_pastures(output_file,grass_list):
    grass_str = list(map(str,grass_list))
    ouput_file.write(''.join(grass_str))

grass_list.pop(0)
write_pastures(ouput_file,grass_list)
    
input_file.close()
ouput_file.close()