# https://dmoj.ca/problem/ccc06j1

burger_list = [461,431,420,0]
drink_list = [130,160,118,0]
side_list = [100,57,70,0]
dessert_list = [167,266,75,0]

burger_input = int(input()) - 1
side_input = int(input()) - 1
drink_input = int(input()) - 1
dessert_input = int(input()) - 1

calorie = burger_list[burger_input] + drink_list[drink_input] + side_list[side_input] + dessert_list[dessert_input]

print("Your total Calorie count is " + str(calorie) +".")
