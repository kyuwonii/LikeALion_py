#lionqueen

def list_avg (score_list):
    x = len(score_list)
    sum = 0 

    for i in range(1,x,1):
        sum+=int((score_list[i]))

    avg = float(sum) / (x-1)

    return avg


def PassFail (avg):
    if avg>=60 :
        print('{} passed the class'.format(score_list[0]))
    else:
        print('{} failed the class'.format(score_list[0]))




print("이름과 점수를 입력해주세요")
name_score = input()
score_list=name_score.split()
print("평균 = ",list_avg(score_list))

result=''
for i in range(1,len(score_list),1):
    if (0>int(score_list[i]) or int(score_list[i])>100):
        print("wrong input")
        result = 'wrong'
        break
    
if(result!='wrong'):
    PassFail(list_avg(score_list)) 

