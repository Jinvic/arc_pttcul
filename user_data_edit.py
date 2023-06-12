import csv
from CCT_search import CCT_search
from ptt_culculation import ptt_cul


# 从定数表添加新行
def UDT_add():
    print('请输入关键词以查找曲目')
    st = input()

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
    print('已添加成绩：')
    print(new_row)

    # 写入用户数据表
    with open('user_data_table.csv', 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_row)

    UDT_sort()


# 列出用户数据表中所有曲目
def UDT_list():
    UDT_sort()

    with open('user_data_table.csv', 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]

        # 寻找曲名的最大宽度
        max_width = max([len(str(row[0])) for row in rows])
        max_widths = [max_width, 5, 5, 10, 10]
        head = ['曲名', '难度', '定数', '成绩', '潜力值']
        head_widths = [max_width-2, 3, 3, 8, 7]

        # 输出表头
        formatted_row = ''
        for i in range(len(head)):
            formatted_row += str(head[i]).ljust(head_widths[i] + 2)
        print(formatted_row)

        # 输出用户数据表
        for row in rows:
            formatted_row = ''
            for i in range(len(row)):
                formatted_row += str(row[i]).ljust(max_widths[i] + 2)
            print(formatted_row)


# 更新用户数据表的成绩
def UDT_update():
    print('请输入关键词以查找曲目')
    st = input()

    # 在用户数据表搜索
    with open('user_data_table.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
        res = []
        dic = {}  # 存查找结果到原表行数的映射
        row_no = 0  # 原表行数
        idx = 0  # 结果编号
        for row in rows:
            if(row[0].upper().find(st.upper()) != -1):
                res.append([idx]+row)
                dic[idx] = row_no
                idx += 1
            row_no += 1
        if(len(res) == 0):
            print('未查找到结果，请重新查找')
            return

    # 寻找曲名的最大宽度
    max_width = max([len(str(row[1])) for row in res])
    max_widths = [5, max_width, 5, 5, 10, 10]
    head = ['编号', '曲名', '难度', '定数', '成绩', '潜力值']
    head_widths = [3, max_width-2, 3, 3, 8, 7]

    # 输出表头
    formatted_row = ''
    for i in range(len(head)):
        formatted_row += str(head[i]).ljust(head_widths[i] + 2)
    print(formatted_row)

    # 输出用户数据表
    for row in res:
        formatted_row = ''
        for i in range(len(row)):
            formatted_row += str(row[i]).ljust(max_widths[i] + 2)
        print(formatted_row)

    input_check = False
    while input_check == False:
        print("选择修改的曲目，输入编号")
        idx = int(input())
        if(idx >= len(res) or idx < 0):
            print("编号不合法")
        else:
            input_check = True

    print('输入更新后的成绩')
    score = int(input())
    rows[dic[idx]][3] = score
    rows[dic[idx]][4] = ptt_cul(
        float(rows[dic[idx]][2]), rows[dic[idx]][3])
    print('已更新成绩：')
    print(rows[dic[idx]])

    with open('user_data_table.csv', 'w', encoding='utf-8', newline='') as new_csvfile:
        writer = csv.writer(new_csvfile)
        writer.writerows(rows)

    UDT_sort()


# 排序UDT方便计算b30
def UDT_sort():
    with open('user_data_table.csv', 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]

    sorted_rows = sorted(rows, key=lambda x: float(x[4]), reverse=True)

    with open('user_data_table.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sorted_rows)


# UDT_add('red')
# UDT_sort()
# UDT_update()
