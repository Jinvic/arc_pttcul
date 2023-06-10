import csv


def CCT_search(st):
    # 读取csv并查询
    with open('chart_constant_table.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        head = next(reader)
        res = []
        for row in reader:
            if(row[0].upper().find(st.upper()) != -1):
                res.append(row)

        # 寻找曲名的最大宽度
        max_width = max([len(str(row[0])) for row in res])
        max_widths = [5, max_width, 5, 5, 5, 5]  # 编号和定数列宽度固定
        # print(max_widths)

        if(len(res) == 0):
            print('未查找到结果，请重新查找')
        else:

            # 输出表头
            head = ['编号']+head
            formatted_row = ''
            for i in range(len(head)):
                if(i < 2):  # 前两列为中文，宽度短一点不然对不齐
                    formatted_row += str(head[i]).ljust(max_widths[i])
                else:
                    formatted_row += str(head[i]).ljust(max_widths[i] + 2)
            print(formatted_row)

            # 输出定数表
            idx = 0
            for row in res:
                # print(f'', end=' ')
                row = [idx]+row
                formatted_row = ''
                for i in range(len(row)):
                    # print(f'{head[i]}:{row[i]}', end=' ')
                    formatted_row += str(row[i]).ljust(max_widths[i] + 2)
                print(formatted_row)
                idx += 1

        return res


# CCT_search('red')
