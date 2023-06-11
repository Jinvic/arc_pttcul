import sys
from spider import CCT_update
from user_data_edit import UDT_add, UDT_list, UDT_update
from ptt_culculation import b30_cul, r10_cul


def main():
    print('选择你要进行的操作：')
    print('0. 退出程序')
    print('1. 更新定数表')
    print('2. 列出用户成绩')
    print('3. 添加新成绩')
    print('4. 更新现有成绩')
    print('5. 计算b30')
    print('6. 计算r10')

    input_check = False
    while input_check == False:
        idx = int(input())
        if(idx > 6 or idx < 0):
            print("编号不合法")
        else:
            input_check = True

    if(idx == 0):
        sys.exit()
    elif(idx == 1):
        CCT_update()
    elif(idx == 2):
        UDT_list()
    elif(idx == 3):
        UDT_add()
    elif(idx == 4):
        UDT_update()
    elif(idx == 5):
        print(b30_cul())
    else:
        print('输入你现在的ptt')
        ptt = input()
        print(r10_cul(b30_cul(), float(ptt)))


if __name__ == '__main__':
    while(True):
        print()
        main()
