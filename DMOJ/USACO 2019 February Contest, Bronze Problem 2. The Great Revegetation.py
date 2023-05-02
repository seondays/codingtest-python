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
    

# TODO : 할당 가능한 풀 중 가장 작은 수의 풀 구하기

#main 
input_file = open('revegetate.in','r')
ouput_file = open('revegetate.out','w')

# TODO : 입력 처리
file_line = list(map(int,input_file.readline().split()))
num_pastures = file_line[0]
num_cows = file_line[1]

favorites = find_pasture_for_cows(input_file,num_cows)

grass_type = []

# TODO : 출력 처리
input_file.close()
ouput_file.close()