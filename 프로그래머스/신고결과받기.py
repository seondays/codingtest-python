# https://school.programmers.co.kr/learn/courses/30/lessons/92334

class User():
    def __init__(self,name):
        self.name = name
        self.report_count = 0
        self.reporter = []
        self.user_i_report = []
        
def solution(id_list, report, k):
    user_list = {}
    
    for i in id_list:
        user = User(i)
        user_list[user.name] = user

    for i in report:
        a,b = i.split()
        if a not in user_list[b].reporter:
            user_list[b].reporter.append(a)
            user_list[b].report_count += 1
        if b not in user_list[a].user_i_report:
            user_list[a].user_i_report.append(b)
        
    email = dict.fromkeys(id_list,0)
    
    for v in user_list.values():
        if v.report_count >= k:
            for i in v.reporter:
                email[i] += 1
        
    answer = [i for i in email.values()]
    
    return answer