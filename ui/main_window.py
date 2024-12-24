import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  # 用于加载图标
from db.utils import create_connection, fetch_data_with_join


class MainWindow(tk.Tk):
    def __init__(self,identity):
        super().__init__()
        self.identity = identity
        self.title("美国总统大选数据库系统")
        self.geometry("1500x900")  # 增大窗口尺寸
        self.config(bg='#f0f0f0')

        self.table_name = None  # 当前表名
        self.column_names = []  # 当前列名

        # 加载图标
        self.load_icons()

        self.create_widgets()

        # 添加状态栏
        self.status_bar = tk.Label(self, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="#e0e0e0", font=("Arial", 12))
        self.status_bar.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(10, 0))

    def load_icons(self):
        """加载图标"""
        self.add_icon = ImageTk.PhotoImage(Image.open("icons/add.png").resize((20, 20)))
        self.delete_icon = ImageTk.PhotoImage(Image.open("icons/delete.png").resize((20, 20)))
        self.update_icon = ImageTk.PhotoImage(Image.open("icons/update.png").resize((20, 20)))
        self.refresh_icon = ImageTk.PhotoImage(Image.open("icons/refresh.png").resize((20, 20)))

    def create_widgets(self):
        """创建界面控件"""
        # 左边按钮区域
        self.left_frame = tk.Frame(self, width=200, bg='#e0e0e0', relief="sunken")
        self.left_frame.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")

        # 配置比例，让按钮区占更少的空间
        self.grid_columnconfigure(0, weight=1, uniform="group1")  # 左边按钮区域
        self.grid_columnconfigure(1, weight=3, uniform="group1")  # 右侧数据区域

        self.buttons = [
            ("候选人信息", "Candidate"),
            ("参选情况", "CandidateList"),
            ("退选情况", "WithdrawnCandidates"),
            ("选举进程", "ElectionProcess"),
            ("选举事件", "Event"),
            ("候选人与事件", "ElectionEvent"),
            ("得票信息", "ElectionVotes"),
            ("财团信息", "Corporation"),
            ("财团支持", "CandidateSupport")
        ]

        # 按钮列表
        for i, (text, table_name) in enumerate(self.buttons):
            btn = tk.Button(self.left_frame, text=text, font=("Arial", 12), command=lambda tn=table_name: self.show_table(tn),
                            width=20, bg="#4CAF50", fg="white", relief="flat", activebackground="#45a049",
                            borderwidth=0)
            btn.grid(row=i, column=0, padx=10, pady=5, sticky="we")

        # 右边展示区域
        self.right_frame = tk.Frame(self, bg='#f0f0f0')
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # 配置右侧区域占据更大空间
        self.right_frame.grid_rowconfigure(0, weight=1)  # 数据展示区域占据更多空间
        self.right_frame.grid_columnconfigure(0, weight=1)  # 占据剩余的宽度

        # 数据展示表格区域
        self.canvas = tk.Canvas(self.right_frame, bg='#f0f0f0', highlightthickness=0)
        self.scrollbar_y = tk.Scrollbar(self.right_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar_x = tk.Scrollbar(self.right_frame, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

        self.canvas.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.scrollbar_y.grid(row=0, column=1, sticky="ns")
        self.scrollbar_x.grid(row=1, column=0, sticky="ew")

        self.treeview = None  # 占位符，稍后动态创建

        # 操作按钮区域
        self.action_buttons_frame = tk.Frame(self.right_frame, bg='#f0f0f0')
        self.action_buttons_frame.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        # 删除、添加、刷新、修改按钮
        self.delete_button = tk.Button(self.action_buttons_frame, image=self.delete_icon, compound=tk.LEFT,
                                       text="删除选中数据", font=("Arial", 12), command=self.delete_data, bg="#f44336",
                                       fg="white", relief="flat", activebackground="#d32f2f", borderwidth=0)
        self.delete_button.grid(row=0, column=0, padx=10, pady=5, sticky="w", ipadx=10)

        self.add_button = tk.Button(self.action_buttons_frame, image=self.add_icon, compound=tk.LEFT, text="添加记录",
                                    font=("Arial", 12), command=self.add_data, bg="#2196F3", fg="white", relief="flat",
                                    activebackground="#1976d2", borderwidth=0)
        self.add_button.grid(row=0, column=1, padx=10, pady=5, sticky="e", ipadx=10)

        self.update_button = tk.Button(self.action_buttons_frame, image=self.update_icon, compound=tk.LEFT,
                                       text="修改选中数据", font=("Arial", 12), command=self.update_data, bg="#FF9800",
                                       fg="white", relief="flat", activebackground="#ef6c00", borderwidth=0)
        self.update_button.grid(row=0, column=2, padx=10, pady=5, sticky="e", ipadx=10)

        self.refresh_button = tk.Button(self.action_buttons_frame, image=self.refresh_icon, compound=tk.LEFT, text="刷新",
                                        font=("Arial", 12), command=self.refresh_data, bg="#FFC107", fg="white",
                                        relief="flat", activebackground="#f9a825", borderwidth=0)
        self.refresh_button.grid(row=0, column=3, padx=10, pady=5, sticky="e", ipadx=10)

        # 配置Treeview样式
        style = ttk.Style()
        style.theme_use("clam")  # 使用clam主题
        style.configure("mystyle.Treeview", background="#ffffff", foreground="#000000", fieldbackground="#ffffff",
                        font=("Arial", 12))
        style.map('mystyle.Treeview', background=[('selected', '#ADD8E6')])  # 选中行背景色

    def show_table(self, table_name):
        """显示选定的表"""
        self.table_name = table_name

        # 清空现有的 TreeView
        if self.treeview:
            self.treeview.destroy()

        # 获取列名和数据
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # 获取列信息
            cursor.execute(f"DESCRIBE {table_name}")
            self.column_names = [column[0] for column in cursor.fetchall() if column[0] != "ID"]  # 排除主键
            cursor.close()

            # 获取数据并做外键映射
            data = fetch_data_with_join(table_name, self.column_names)

            # 创建 TreeView
            self.treeview = ttk.Treeview(self.canvas, columns=self.column_names, show="headings", height=15,
                                         style="mystyle.Treeview")
            self.canvas.create_window((0, 0), window=self.treeview, anchor="nw")

            # 动态设置表头
            for col in self.column_names:
                self.treeview.heading(col, text=col)
                self.treeview.column(col, width=150, anchor="center")

            # 插入数据
            for row in data:
                self.treeview.insert("", "end", values=row)

            # 更新滚动区域
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

            self.status_bar.config(text=f"Table '{table_name}' loaded successfully.")

        except Exception as e:
            self.show_error_message("错误", f"加载数据时发生错误: {str(e)}")

    def delete_data(self):
        """删除选中数据"""
        if not self.treeview:
            self.show_warning_message("警告", "请先选择一个表！")
            return

        selected_items = self.treeview.selection()
        if not selected_items:
            self.show_warning_message("警告", "请选择要删除的数据")
            return
        if self.identity == "user":
            messagebox.showerror("操作无效！", "您没有此权限")
            return
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # 删除选中的数据
            for item in selected_items:
                values = self.treeview.item(item, "values")
                primary_key_value = values[0]  # 假设第一列是主键
                cursor.execute(f"DELETE FROM {self.table_name} WHERE {self.column_names[0]} = %s", (primary_key_value,))
                connection.commit()

            self.show_success_message("成功", "数据已删除！")
            self.refresh_data()

        except Exception as e:
            self.show_error_message("错误", f"删除数据时发生错误: {str(e)}")

        finally:
            cursor.close()
            connection.close()

    def refresh_data(self):
        """刷新数据"""
        if not self.table_name:
            self.show_warning_message("警告", "请先选择一个表！")
            return

        self.show_table(self.table_name)

    def add_data(self):
        """添加新记录"""
        if not self.table_name:
            self.show_warning_message("警告", "请先选择一个表！")
            return
        if self.identity == "user":
            messagebox.showerror("操作无效！", "您没有此权限")
            return

        # 弹出新窗口，允许用户输入数据
        self.add_window = tk.Toplevel(self)
        self.add_window.title("添加记录")

        self.entries = {}
        frame = tk.Frame(self.add_window, bg='#f0f0f0')
        frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(frame, bg='#f0f0f0', highlightthickness=0)
        scrollbar_y = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar_x = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
        canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        inner_frame = tk.Frame(canvas, bg='#f0f0f0')
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        tk.Label(inner_frame, text="请输入新记录的数据：", font=("Arial", 12)).grid(row=0, column=0, columnspan=2, pady=10)

        self.manual_id_var = tk.BooleanVar()  # 这个变量决定是否允许手动输入主键
        tk.Checkbutton(inner_frame, text="手动输入主键", variable=self.manual_id_var, font=("Arial", 12)).grid(row=1, column=0, columnspan=2, pady=10)

        try:
            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute(f"DESCRIBE {self.table_name}")
            columns = cursor.fetchall()
            cursor.close()

            # 处理表结构
            for i, column in enumerate(columns):
                col_name = column[0]  # 获取列名
                if col_name != "ID":  # 排除主键列
                    tk.Label(inner_frame, text=col_name, font=("Arial", 12)).grid(row=i + 2, column=0, padx=10, pady=5)
                    entry = tk.Entry(inner_frame, font=("Arial", 12))
                    entry.grid(row=i + 2, column=1, padx=10, pady=5)
                    self.entries[col_name] = entry

                # 如果主键允许手动输入
                if col_name == "ID":
                    if self.manual_id_var.get():
                        tk.Label(inner_frame, text="主键 (ID)", font=("Arial", 12)).grid(row=i + 2, column=0, padx=10, pady=5)
                        id_entry = tk.Entry(inner_frame, font=("Arial", 12))
                        id_entry.grid(row=i + 2, column=1, padx=10, pady=5)
                        self.entries["ID"] = id_entry
                    else:
                        self.entries["ID"] = None

            submit_button = tk.Button(inner_frame, text="提交", font=("Arial", 12), command=self.insert_data, bg="#4CAF50", fg="white",
                                      relief="flat", activebackground="#45a049", borderwidth=0)
            submit_button.grid(row=len(columns) + 2, column=0, columnspan=2, pady=10)

            inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        except Exception as e:
            self.show_error_message("错误", f"加载表结构时发生错误: {str(e)}")

    def insert_data(self):
        """提交插入数据"""
        # 获取表单数据

        data = {col: entry.get() for col, entry in self.entries.items() if entry.get()}

        # 检查是否需要手动指定主键
        if self.manual_id_var.get() and "ID" in data and not data["ID"]:
            del data["ID"]  # 如果没有填写主键，就删除主键字段，允许数据库自动生成

        columns = ", ".join(data.keys())
        values = ", ".join([f"'{v}'" for v in data.values()])

        try:
            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute(f"INSERT INTO {self.table_name} ({columns}) VALUES ({values})")
            connection.commit()

            self.show_success_message("成功", "数据已成功插入！")
            self.add_window.destroy()
            self.refresh_data()

        except Exception as e:
            self.show_error_message("错误", f"插入数据时发生错误: {str(e)}")

        finally:
            cursor.close()
            connection.close()

    def update_data(self):
        """修改选中数据"""
        if not self.treeview:
            self.show_warning_message("警告", "请先选择一个表！")
            return

        selected_item = self.treeview.selection()
        if not selected_item:
            self.show_warning_message("警告", "请选择要修改的数据")
            return
        if self.identity == "user":
            messagebox.showerror("操作无效！", "您没有此权限")
            return
        # 弹出新窗口，允许用户输入数据
        self.update_window = tk.Toplevel(self)
        self.update_window.title("修改记录")

        self.entries = {}
        frame = tk.Frame(self.update_window, bg='#f0f0f0')
        frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(frame, bg='#f0f0f0', highlightthickness=0)
        scrollbar_y = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar_x = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
        canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        inner_frame = tk.Frame(canvas, bg='#f0f0f0')
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        tk.Label(inner_frame, text="请输入新记录的数据：", font=("Arial", 12)).grid(row=0, column=0, columnspan=2, pady=10)

        current_values = self.treeview.item(selected_item[0], "values")
        self.current_primary_key = current_values[0]

        try:
            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute(f"DESCRIBE {self.table_name}")
            columns = cursor.fetchall()
            cursor.close()

            # 处理表结构
            for i, column in enumerate(columns):
                col_name = column[0]  # 获取列名
                tk.Label(inner_frame, text=col_name, font=("Arial", 12)).grid(row=i + 1, column=0, padx=10, pady=5)
                entry = tk.Entry(inner_frame, font=("Arial", 12))
                entry.grid(row=i + 1, column=1, padx=10, pady=5)
                entry.insert(0, current_values[i])  # 设置当前值
                self.entries[col_name] = entry

            submit_button = tk.Button(inner_frame, text="提交", font=("Arial", 12), command=self.submit_update, bg="#4CAF50", fg="white",
                                      relief="flat", activebackground="#45a049", borderwidth=0)
            submit_button.grid(row=len(columns) + 1, column=0, columnspan=2, pady=10)

            inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        except Exception as e:
            self.show_error_message("错误", f"加载表结构时发生错误: {str(e)}")

    def submit_update(self):
        """提交更新数据"""
        # 获取表单数据
        data = {col: entry.get() for col, entry in self.entries.items()}

        set_clause = ", ".join([f"{col} = '{data[col]}'" for col in data])
        condition = f"{self.column_names[0]} = '{self.current_primary_key}'"

        try:
            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute(f"UPDATE {self.table_name} SET {set_clause} WHERE {condition}")
            connection.commit()

            self.show_success_message("成功", "数据已成功更新！")
            self.update_window.destroy()
            self.refresh_data()

        except Exception as e:
            self.show_error_message("错误", f"更新数据时发生错误: {str(e)}")

        finally:
            cursor.close()
            connection.close()

    def show_success_message(self, title, message):
        """显示成功的消息框"""
        messagebox.showinfo(title, message)
        self.status_bar.config(text=message)

    def show_warning_message(self, title, message):
        """显示警告的消息框"""
        messagebox.showwarning(title, message)
        self.status_bar.config(text=message)

    def show_error_message(self, title, message):
        """显示错误的消息框"""
        messagebox.showerror(title, message)
        self.status_bar.config(text=message)


def main_window(identity):
    app = MainWindow(identity)
    app.mainloop()


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()


