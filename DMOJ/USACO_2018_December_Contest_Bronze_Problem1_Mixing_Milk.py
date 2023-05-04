# 우유 버켓 정보 가져오기
def read_bucket(input_file):
    buckets = []
    for line in input_file:
        bucket = list(map(int,line.split()))
        buckets.append(bucket)
        
    return buckets

# 버켓 섞기
def mix_bucket(first_bucket,secound_bucket):
    first_bucket_capacity = first_bucket[0]
    first_bucket_amount = first_bucket[1]
    secound_bucket_capacity = secound_bucket[0]
    secound_bucket_amount = secound_bucket[1]
    
    secound_bucket_amount += first_bucket_amount
    first_bucket_amount = 0
    
    if secound_bucket_amount > secound_bucket_capacity:
        overflow = secound_bucket_amount - secound_bucket_capacity
        first_bucket_amount += overflow
        secound_bucket_amount = secound_bucket_capacity
    after_mixed = [[first_bucket_capacity,first_bucket_amount],[secound_bucket_capacity,secound_bucket_amount]]
    return after_mixed
        
# Main
input_file = open('mixmilk.in','r')
output_file = open('mixmilk.out','w')

milk_buckets = read_bucket(input_file)

input_file.close
output_file.close
    