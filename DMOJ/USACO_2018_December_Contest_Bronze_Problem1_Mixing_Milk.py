# 우유 버켓 정보 가져오기
def read_bucket(input_file):
    buckets = []
    for line in input_file:
        bucket = list(map(int,line.split()))
        buckets.append(bucket)
        
    return buckets

# 버켓 섞기
def mix_bucket(first_bucket,secound_bucket):
    first_bucket_amount = first_bucket[1]
    secound_bucket_capacity = secound_bucket[0]
    secound_bucket_amount = secound_bucket[1]
    
    milk = min(first_bucket_amount,secound_bucket_capacity-secound_bucket_amount)
    first_bucket_amount -= milk
    secound_bucket_amount += milk
    after_mixed = [first_bucket_amount,secound_bucket_amount]
    
    return after_mixed
        
# Main
input_file = open('mixmilk.in','r')
output_file = open('mixmilk.out','w')

milk_buckets = read_bucket(input_file)

for i in range(100):
    first_number = i % 3
    secound_number = (i+1) % 3
    
    after_mixed = mix_bucket(milk_buckets[first_number],milk_buckets[secound_number])
    milk_buckets[first_number][1] = after_mixed[0]
    milk_buckets[secound_number][1] = after_mixed[1]

for i in range(3):
    output_file.write(str(milk_buckets[i][1])+'\n')

input_file.close
output_file.close
    