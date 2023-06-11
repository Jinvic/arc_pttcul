import csv


def csv_search(st, filename):
    # 读取csv并查询
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        head = next(reader)
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
            errlog = '未查找到结果，请重新查找'
        else:
            errlog = ''

        return dic, head, res, errlog


# def csv_format(head, rows, flag):
#     # 寻找曲名的最大宽度
#     max_width = max([len(str(row[0])) for row in rows])
#     if(flag == 0):  # CCT 曲目,PST,PRS,FTR,BYD
#         max_widths = [5, max_width, 5, 5, 5, 5]
#         head_widths = [3, max_width-2, 3, 3, 3, 3]
#     else:  # UDT 曲名, 难度, 定数, 成绩, 潜力值
#         max_widths = [5, max_width, 5, 5, 10, 10]
#         head_widths = [3, max_width-2, 3, 3, 8, 7]

#     # 输出表头
#     head = ['编号']+head
#     formatted_row = ''
#     for i in range(len(head)):
#         if(i < 2):  # 前两列为中文，宽度短一点不然对不齐
#             formatted_row += str(head[i]).ljust(max_widths[i])
#         else:
#             formatted_row += str(head[i]).ljust(max_widths[i] + 2)
#     print(formatted_row)
