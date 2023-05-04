# 우유 버켓 정보 가져오기
def read_bucket(input_file):
    buckets = []
    for line in input_file:
        bucket = list(map(int,line.split()))
        print(bucket)
        buckets.append(bucket)
        
    return buckets

# 버켓 섞기

# Main
input_file = open('mixmilk.in','r')
output_file = open('mixmilk.out','w')

milk_buckets = read_bucket(input_file)


