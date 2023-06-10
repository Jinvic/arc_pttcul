import csv
from CCT_search import CCT_search
from ptt_culculation import ptt_cul


# 从定数表添加新行
def UDT_add(st):

    res = CCT_search(st)
    if(len(res) == 0):
        return

    input_check = False
    while input_check == False:
        print("选择添加的曲目，输入编号")
        idx = int(input())
        if(idx >= len(res) or idx < 0):
            print("编号不合法")
        else:
            input_check = True

    input_check = False
    while input_check == False:
        print("选择难度[pst|prs|ftr|byd]")
        difficults = ['PST', 'PRS', 'FTR', 'BYD']
        difficult = input()
        dif_id = -1
        for i in range(4):
            if(difficults[i].upper() == difficult.upper()):
                dif_id = i
                break
        if(dif_id == -1):
            print('难度输入错误')
        else:
            input_check = True

    print("输入成绩")
    score = int(input())

    # 曲名 难度 定数 成绩 潜力值
    new_row = [res[idx][0],
               difficults[dif_id],
               res[idx][dif_id+1],
               score,
               ptt_cul(float(res[idx][dif_id+1]), score)]
    print(new_row)

    # 写入用户数据表
    with open('user_data_table.csv', 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_row)


# 列出用户数据表中所有曲目
def UDT_list():
    print()


# 在用户数据表搜索
def UDT_search():
    print()


# 更新成绩
def UDT_update():
    print()


UDT_add('red')
