# arc_pttcul

使用python爬虫爬取定数表，并进行b30等的存储与计算

随手做的小玩意，现在**还没做完**，懒，心情好就写点

## 导入用户数据

只是爬定数表，用户数据还是要自己输入。如果之前自己做了excel表，只要按`曲名 难度 定数 成绩 潜力值`的表头导出csv，再替换`user_data_table.csv`文件就行了。**注意**：`user_data_table.csv`中没有表头，且需要以`utf-8`的编码保存。

## 打包程序

使用`PyInstaller`进行单文件打包。打包好的程序在dist目录下。初次使用需要先生成两个表格。启动程序，先使用`1. 更新定数表`命令生成定数表`chart_constant_table.csv`。再使用`3. 添加新成绩`命令生成用户数据表`user_data_table.csv`。也可以自己导入用户数据，方法见上。

## 注意事项

* 在使用`1. 更新定数表`命令时，需要关闭代理，否则报错`requests.exceptions.SSLError`。
* 请按正常格式输入输出，没有做输入异常处理健壮性测试，非法输入只会boom。

## 待办事项

* Qtpy做图形化界面
* 更完善的用户引导
* 更全面的异常处理
* 更精简的代码复用
  