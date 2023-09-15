import tkinter as tk
from tkinter import ttk, messagebox
import os
import rep_tag
import rep_problems
import rep_solutions

#创建容器
selected_folder = []
difficult = rep_tag.difficult
key = rep_tag.key
# print(difficult)
#print(key)

# 创建主窗口
window = tk.Tk()
window.title("洛谷题目筛选器")
window.resizable(False, False)
# 创建样式
style = ttk.Style()
style.theme_use("default")
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

def filter_window():

    #双击打开相应文件夹
    def open_selected_folder(event):
        # 获取双击时选定的文本行号
        line_number = int(selected_folder_text.index(tk.CURRENT).split('.')[0])

        # 检查行号是否在选定文件夹的范围内
        if line_number >= 1 and line_number <= len(selected_folder):
            folder_name = selected_folder[line_number - 1]  # 根据行号获取文件夹名字
            folder_path = "./data/" + str(folder_name)  # 拼接文件夹路径
            #print(folder_path)
            # 检查文件夹是否存在
            if os.path.exists(folder_path) and os.path.isdir(folder_path):
                folder_path = folder_path.replace('/', '\\')  # 将斜杠替换为反斜杠
                folder_path = os.path.abspath(folder_path)  # 获取绝对路径
                os.startfile(folder_path)
    #当点击筛选按钮
    def filter_button_clicked(difficulty='',keyword=''):
        global selected_folder
        selected_folder.clear()
        #获取文本框输入内容
        if difficulty == '':
            difficulty = difficulty_var.get()
            keyword = keyword_entry.get().split("-")
        else:
            keyword = keyword.split("-")
        #相应难度下没有题目
        if difficult.get(str(difficulty)) == None:
            selected_folder.append("暂无符合条件的题目")
            selected_folder_text.delete('1.0', tk.END)
            for i in range(len(selected_folder)):
                selected_folder_text.insert(tk.END, selected_folder[i] + '\n')
            return selected_folder
        else:
            #获取相应难度下的题目
            diff = list(difficult.get(str(difficulty)))
            for i in diff:
                i = str(i)
                flag = 1
                if keyword != ['']:
                    # 列表不为空，执行其他操作
                    #检查是否满足其他关键词
                    for k in keyword:
                        if not (i in key[str(k)]):
                            flag = 0
                #满足所有关键词则添加入列表元素
                if flag == 1:
                    selected_folder.append(i)
        # 判断是否有符合条件的题目
        if len(selected_folder) == 0:
            selected_folder.append("暂无符合条件的题目")
        # 更新文本框内容
        selected_folder_text.delete('1.0', tk.END)
        for i in range(len(selected_folder)):
            selected_folder_text.insert(tk.END, selected_folder[i] + '\n')
        print(selected_folder)
        return selected_folder


    window.update()
    # 难度选择
    difficulty_label = ttk.Label(window, text="难度:")
    difficulty_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

    difficulty_var = tk.StringVar()
    difficulty_option_menu = ttk.OptionMenu(window, difficulty_var, "", '暂无评定', '入门', '普及−', '普及/提高−', '普及+/提高',
                                            '提高+/省选−', '省选/NOI−', 'NOI/NOI+/CTSC')
    difficulty_option_menu.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

    # 关键词输入
    keyword_label = ttk.Label(window, text="关键词:")
    keyword_label.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)

    keyword_entry = ttk.Entry(window)
    keyword_entry.grid(row=0, column=3, padx=10, pady=10, sticky=tk.W)

    # 创建显示选定文件夹的多行文本框
    selected_folder_text = tk.Text(window, font=('Arial', 12), width=50, height=10)
    selected_folder_text.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

    # 筛选按钮
    filter_button = ttk.Button(window, text="筛选", command=filter_button_clicked)
    selected_folder_text.bind("<Double-Button-1>", open_selected_folder)
    filter_button.grid(row=0, column=4, padx=10, pady=10, sticky=tk.W)

#爬取函数
def reptle():
    global window,difficult,key
    window.update()
    def newreptile():
        global i, window
        # 更新标签列表
        difficult, key = rep_tag.main(int(problems.get()), int(problems2.get()))
        for i in range(int(problems.get()), int(problems2.get()) + 1):
            progress_text.insert(tk.END, '正在爬取第' + str(i) + '题')
            window.update()
            mark, timu = rep_problems.main(i)
            progress_text.insert(tk.END, '………………' + mark + '\n')
            window.update()
            # 滚动到最后一行
            progress_text.see(tk.END)
            # 爬完最后一题，显示完成
            if i == int(problems2.get()):
                progress_text.insert(tk.END, '正在爬取题解，请稍等……\n')
                mark2 = rep_solutions.main(int(problems.get()), int(problems2.get()), timu)
                if mark2:
                    messagebox.showinfo(title='提示', message='爬取完成')
                    window.destroy()
                    window = tk.Tk()
                    window.title("洛谷题目筛选器")
                    window.resizable(False, False)
                    window.update()
                    filter_window()
    timu = tk.Label(window, text="题目编号")
    timu.grid(row=0, sticky="w")
    problems = tk.Entry(window)
    problems.insert(0, "1000")#默认从1000开始
    problems.grid(row=0, column=1)
    gang = tk.Label(window, text="-")
    gang.grid(row=0, column=2)
    problems2 = tk.Entry(window)
    problems2.insert(0, "1049")#默认到1049
    problems2.grid(row=0, column=3)
    rep = tk.Button(window, text="爬取", command=newreptile)
    rep.grid(row=0, column=4, padx=10, pady=10, sticky=tk.W)

    # 创建显示进度的多行文本框
    progress_text = tk.Text(window, font=('Arial', 12), width=50, height=10)
    progress_text.grid(row=1, column=0, columnspan=5, padx=10, pady=10)


if __name__ == '__main__':
    reptle()
    # 运行主循环
    window.mainloop()
