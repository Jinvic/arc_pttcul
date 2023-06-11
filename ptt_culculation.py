import csv


def ptt_cul(cc, score):
    if(score > 10000000):
        return cc+2
    elif(score >= 9800000):
        return cc+1+(score-9800000)/200000
    else:
        return max(cc+(score-9500000)/300000, 0)


def b30_cul():

    with open('user_data_table.csv', 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile)
        cnt = 0
        sum = 0
        for row in reader:
            sum += float(row[4])
            cnt += 1
            if(cnt == 30):
                break
        return sum/30


def r10_cul(b30, ptt):
    return (ptt*40-b30*30)/10
