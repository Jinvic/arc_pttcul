import os
import sys
import csv
import requests
from pyquery import PyQuery as pq

from PySide6.QtWidgets import QApplication, QWidget, QInputDialog, QHeaderView, QMessageBox
from PySide6 import QtGui
from arc_pttcul_ui import Ui_Form


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = QtGui.QStandardItemModel()
        self.ui.tableView.setModel(self.model)
        header = self.ui.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.ui.PB_init.clicked.connect(self.init_func)
        self.ui.PB_CCT_update.clicked.connect(self.CCT_update_func)
        self.ui.PB_UDT_list.clicked.connect(self.UDT_list_func)
        self.ui.PB_UDT_add.clicked.connect(self.UDT_add_func)
        self.ui.PB_UDT_update.clicked.connect(self.UDT_update_func)
        self.ui.PB_b30.clicked.connect(self.b30_func)
        self.ui.PB_r10.clicked.connect(self.r10_func)

        self.CCT = 'chart_constant_table.csv'
        self.UDT = 'user_data_table.csv'

        self.config_check()

    def config_check(self):
        if(os.path.exists(self.CCT) == False or os.path.exists(self.UDT) == False):
            QMessageBox.warning(self, "警告", "未检测到配置文件\n请先初始化")
            return False
        else:
            return True

    def init_func(self):
        btn = QMessageBox.warning(self, "警告", "初始化操作将清除已有数据\n确定要继续吗？",
                                  QMessageBox.Ok,
                                  QMessageBox.Cancel)
        if(btn != QMessageBox.Ok):
            self.send_message('取消初始化')
            return

        if self.CCT_update_func() == 'SSLError':
            return

        with open(self.UDT, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            UDT_head = ['曲名', '难度', '定数', '成绩', '潜力值']
            writer.writerow(UDT_head)

        self.send_message('初始化完成')

    def CCT_update_func(self):
        inputways = ['中文维基', '英文维基']
        inputway, okPressed = QInputDialog.getItem(
            self, '选择定数表获取方式',
            '中文维基: wiki.arcaea.cn/定数详表\n' +
            '英文维基: arcaea.fandom.com/wiki/Songs_by_Level',
            inputways, editable=False)
        if(okPressed == False):
            return

        QMessageBox.warning(self, "提示", "网页访问速度可能较慢，请耐心等待")

        if(inputway == '中文维基'):
            target_url = 'https://wiki.arcaea.cn/%E5%AE%9A%E6%95%B0%E8%AF%A6%E8%A1%A8'  # 定数详表页面
            target_url_test = "wiki_cn.html"
            try:
                doc = pq(url=target_url)
                # doc = pq(filename=target_url_test)
            except requests.exceptions.SSLError as e:
                self.send_message(['爬取定数表失败。\n',
                                   '错误类型：requests.exceptions.SSLError\n',
                                   '请关闭代理后重试。'])
                return 'SSLError'
            chart_constant_table = doc('tbody')  # 定数表

            with open(self.CCT, 'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for item in chart_constant_table('tr').items():
                    writer.writerow(item.text().split('\n'))
                self.send_message('定数表已更新')

        elif(inputway == '英文维基'):
            target_url = 'https://arcaea.fandom.com/wiki/Songs_by_Level'  # 定数表页面
            target_url_test = "wiki_en.html"
            try:
                doc = pq(url=target_url)
                # doc = pq(filename=target_url_test)
            except requests.exceptions.SSLError as e:
                self.send_message(['爬取定数表失败。\n',
                                   '错误类型：requests.exceptions.SSLError\n',
                                   '请关闭代理后重试。'])
                return 'SSLError'

            chart_constant_table_en = doc(
                '.tabberex-tab:nth-child(1) tbody')  # 定数表

            # 转换定数表格式，使其和原程序适配
            # 表头：曲目,PST,PRS,FTR,BYD
            chart_constant_table_cn = [['曲目', 'PST', 'PRS', 'FTR', 'BYD']]
            dic = {}
            cnt = 1
            first = True
            for item in chart_constant_table_en('tr').items():
                # 滤掉表头
                if(first == True):
                    first = False
                    continue
                row = item.text().split('\n')
                name = row[0]
                artist = row[1]
                difficulty = row[2]
                cc = row[3]
                if(name == 'Quon' or name == 'Genesis'):  # 同名曲消歧义
                    name = name+'('+artist+')'
                if(name in dic):  # 在表中，添加新难度定数
                    chart_constant_table_cn[dic[name]].append(cc)
                else:  # 不在表中，添加曲名和prs难度定数
                    dic[name] = cnt
                    cnt += 1
                    chart_constant_table_cn.append([name, cc])

            with open(self.CCT, 'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for row in chart_constant_table_cn:
                    writer.writerow(row)
                self.send_message('定数表已更新')

    def UDT_list_func(self):
        if(self.config_check() == False):
            return

        UDT_sort()

        with open('user_data_table.csv', 'r', encoding='utf-8', newline='') as csvfile:
            reader = csv.reader(csvfile)
            head = next(reader)
            rows = [row for row in reader]
            self.csv_list(head, rows)
            self.send_message('已列出全部成绩')

    def UDT_add_func(self):
        if(self.config_check() == False):
            return

        inputways = ['从定数表查找', '手动输入']
        inputway, okPressed = QInputDialog.getItem(
            self, '选择输入方式', '从定数表查找或者手动输入', inputways, editable=False)
        if(okPressed == False):
            return

        if(inputway == '从定数表查找'):
            # text, ok = QInputDialog.getText(parent, '标题', '标签')
            key_word, okPressed = QInputDialog.getText(
                self, "查找曲目", "请输入关键词以查找曲目")
            if(okPressed == False):
                return
            dic, head, res, errlog = csv_search(key_word, self.CCT)
            if(errlog != ''):
                self.send_message(errlog)
                return
            self.send_message(f'已列出包含“{key_word}”的曲目')

            self.csv_list(head, res)
            # num, ok = QInputDialog.getInt(parent, '标题', '标签', 0, min, max, step)
            idx, okPressed = QInputDialog.getInt(
                self, "选择曲目", "请输入对应曲目的序号", 0, 1, len(res), 1)
            if(okPressed == False):
                return
            row = res[idx-1]

            # items = ['选项1', '选项2', '选项3']
            # item, ok = QInputDialog.getItem(parent, '标题', '标签', items, editable=False)
            if(len(row) == 5):
                difficults = ['PST', 'PRS', 'FTR', 'BYD']
            else:
                difficults = ['PST', 'PRS', 'FTR']
            difficult, okPressed = QInputDialog.getItem(
                self, '选择难度', '选择对应的难度', difficults, editable=False)
            if(okPressed == False):
                return

            score, okPressed = QInputDialog.getInt(
                self, '输入成绩', '输入你的游玩成绩', 0, 0)
            if(okPressed == False):
                return

            name = row[0]
            cc = row[difficults.index(difficult)+1]
            ptt = ptt_cul(float(cc), score)
            # 曲名 难度 定数 成绩 潜力值
            new_row = [name, difficult, cc, score, ptt]

        elif(inputway == '手动输入'):
            # text, ok = QInputDialog.getText(parent, '标题', '标签')
            name, okPressed = QInputDialog.getText(
                self, "曲目名称", "请输入曲目名称")
            if(okPressed == False):
                return

            # items = ['选项1', '选项2', '选项3']
            # item, ok = QInputDialog.getItem(parent, '标题', '标签', items, editable=False)
            difficults = ['PST', 'PRS', 'FTR', 'BYD']
            difficult, okPressed = QInputDialog.getItem(
                self, '选择难度', '选择对应的难度', difficults, editable=False)
            if(okPressed == False):
                return

            cc, okPressed = QInputDialog.getDouble(
                self, '输入定数', '输入曲目的定数', 0, 0, decimals=1)
            if(okPressed == False):
                return

            score, okPressed = QInputDialog.getInt(
                self, '输入成绩', '输入你的游玩成绩', 0, 0)
            if(okPressed == False):
                return

            ptt = ptt_cul(float(cc), score)
            # 曲名 难度 定数 成绩 潜力值
            new_row = [name, difficult, cc, score, ptt]

        else:
            return

        with open('user_data_table.csv', 'a', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(new_row)
        UDT_sort()
        self.send_message(['已添加新成绩：\n', str(new_row)])

    def UDT_update_func(self):
        if(self.config_check() == False):
            return

        key_word, okPressed = QInputDialog.getText(self, "查找曲目", "请输入关键词以查找曲目")
        if(okPressed == False):
            return
        dic, head, res, errlog = csv_search(key_word, self.UDT)
        if(errlog != ''):
            self.send_message(errlog)
            return
        self.send_message(f'已列出包含“{key_word}”的曲目')

        self.csv_list(head, res)
        idx, okPressed = QInputDialog.getInt(
            self, "选择曲目", "请输入对应曲目的序号", 0, 1, len(res), 1)
        if(okPressed == False):
            return
        row = res[idx-1]

        score, okPressed = QInputDialog.getInt(
            self, '输入成绩', '输入你的游玩成绩', 0, 0)
        if(okPressed == False):
            return

        name = row[0]
        difficult = row[1]
        cc = row[2]
        ptt = ptt_cul(float(cc), score)
        # 曲名 难度 定数 成绩 潜力值
        new_row = [name, difficult, cc, score, ptt]

        UDT_row_update(dic[idx], new_row)
        self.send_message(['已更新成绩：\n', str(new_row)])

    def b30_func(self):
        if(self.config_check() == False):
            return

        head, rows, b30 = b30_cul()
        self.csv_list(head, rows)
        self.send_message(['已列出b30\n', f'你当前的b30为：{b30}'])

    def r10_func(self):
        if(self.config_check() == False):
            return

        # num, ok = QInputDialog.getDouble(parent, '标题', '标签', 0.00, min, max, decimals)
        ptt, okPressed = QInputDialog.getDouble(
            self, "输入ptt", "请输入你当前的ptt", 0.00, 0, 14, 2)
        if(okPressed == False):
            return

        head, rows, b30 = b30_cul()
        r10 = r10_cul(b30, ptt)
        self.send_message(f'你当前的r10为：{r10}')

    def send_message(self, msgs):
        self.ui.output_text.setPlainText(''.join(msgs))

    def csv_list(self, head, rows):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(head)
        for row in rows:
            items = [QtGui.QStandardItem(field) for field in row]
            self.model.appendRow(items)


def csv_search(st, filename):

    # 读取csv并查询
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        head = next(reader)
        rows = [row for row in reader]
        res = []
        dic = {}  # 存查找结果到原表行数的映射
        row_no = 0  # 原表行数
        idx = 1  # 结果编号
        for row in rows:
            if(row[0].upper().find(st.upper()) != -1):
                res.append(row)
                dic[idx] = row_no
                idx += 1
            row_no += 1

        if(len(res) == 0):
            errlog = '未查找到结果，请重新查找'
        else:
            errlog = ''

        return dic, head, res, errlog


def UDT_row_update(idx, new_row):
    with open('user_data_table.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        head = next(reader)
        rows = [row for row in reader]

    rows[idx] = new_row

    with open('user_data_table.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(head)
        writer.writerows(rows)


def UDT_sort():
    with open('user_data_table.csv', 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile)
        head = next(reader)
        rows = [row for row in reader]

    sorted_rows = sorted(rows, key=lambda x: float(x[4]), reverse=True)

    with open('user_data_table.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(head)
        writer.writerows(sorted_rows)


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
        head = next(reader)
        rows = []
        cnt = 0
        sum = 0
        for row in reader:
            rows.append(row)
            sum += float(row[4])
            cnt += 1
            if(cnt == 30):
                break
        return head, rows, sum/30


def r10_cul(b30, ptt):
    return (ptt*40-b30*30)/10


def main():
    app = QApplication(sys.argv)
    w = Widget()
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
