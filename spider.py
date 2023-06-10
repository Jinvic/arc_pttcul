from pyquery import PyQuery as pq
import csv

def CCT_update():
    target_url = 'https://wiki.arcaea.cn/%E5%AE%9A%E6%95%B0%E8%AF%A6%E8%A1%A8'  # 定数详表页面
    doc = pq(url=target_url)
    chart_constant_table = doc('tbody')  # 定数表
    # print(list(chart_constant_table('th').text().split(' ')))

    with open('chart_constant_table.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item in chart_constant_table('tr').items():
            # print(item.text().split('\n'))
            writer.writerow(item.text().split('\n'))

# CCT_update()
