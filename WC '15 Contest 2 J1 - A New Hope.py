# https://dmoj.ca/problem/wc15c2j1

input_far_count = int(input())
prefix = "A long time ago in a galaxy "
suffix = "away..."
far = "far "
far_puls_comma = "far, "

print(prefix + far_puls_comma * (input_far_count-1) + far + suffix)