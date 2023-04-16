# https://dmoj.ca/problem/ecoo12r1p2

# TODO : promoter 찾은 후에, 전사단위 시작위치 구하기 (TATAAT)
def find_transcription_index(dna):
    for i in range(0,len(dna)):
        if "TATAAT" == dna[i:i+6]:
            return i+10

# TODO : terminator 찾기
def find_terminator_index(string):
    for i in range(0,len(string)):
        candidate = string[i:i+6]
        candidate_opposite = converting_strings(candidate)
        
        if candidate_opposite in string[i+5:]:
            return i

# 주어진 문자열을 알맞게 변환해줌
def converting_strings(candidate):
    opposite_candidate = convert_opposite_dna(candidate)[::-1]
    return opposite_candidate

# TODO : 염기서열 짝으로 변환

def convert_opposite_dna(l):
    convert_dna = []
    for i in l:
        if i == 'A':
            convert_dna.append('T')
        if i == 'T':
            convert_dna.append('A')
        if i == 'C':
            convert_dna.append('G')
        if i == 'G':
            convert_dna.append('C')
    return "".join(convert_dna)

# TODO : 형식에 맞게 출력
def for_print_convert_opposite_dna(l):
    convert_dna = []
    for i in l:
        if i == 'A':
            convert_dna.append('U')
        if i == 'T':
            convert_dna.append('A')
        if i == 'C':
            convert_dna.append('G')
        if i == 'G':
            convert_dna.append('C')
    return "".join(convert_dna)

count = 0 

for i in range(5):
    count += 1
    dna_string = input()
    start_index = find_transcription_index(dna_string)
    transcription = dna_string[start_index:]

    terminator_index = find_terminator_index(transcription)
    
    answer = for_print_convert_opposite_dna(transcription[0:terminator_index])

    print(f"{count}: {answer}")