# https://dmoj.ca/problem/ccc00s2

stream_count = int(input())
stream = []

for i in range(stream_count):
    input_number = int(input())
    stream.append(input_number)

loop_stoper = 0

while loop_stoper != 77:
    input_number = int(input())

    if input_number == 99:
        stream_number = int(input())
        percent = int(input())

        split_stream = round((stream[stream_number-1] / 100) * percent)
        rest_stream = stream[stream_number-1] - split_stream

        stream[stream_number-1] = split_stream
        stream.insert(stream_number,rest_stream)
    
    if input_number == 88:
        stream_number = int(input())
        
        joining_stream = stream[stream_number-1] + stream[stream_number]

        stream.insert(stream_number-1,joining_stream)
        
        del stream[stream_number]
        del stream[stream_number]
    
    loop_stoper = input_number

for i in stream:
    print(i,end=' ')
