import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ui.register  # 导入注册界面
from db.utils import login_user  # 使用更新后的数据库操作函数

def login_window():
    """登录界面"""
    window = tk.Tk()
    window.title("美国大选数据库管理系统！")
    window.geometry("750x600")  # 设置窗口大小

    # 背景图片
    background_image = Image.open('./icons/background.jpg')  # 使用Pillow加载图片
    background_image = background_image.resize((750, 600))  # 调整大小
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(window, image=background_photo)
    background_label.place(relwidth=1, relheight=1)  # 背景覆盖整个窗口

    # 标题
    title = tk.Label(window, text="欢迎来到美国大选数据库管理系统！", font=("Arial", 24, "bold"), bg="#f0f0f0")
    title.pack(pady=20)

    # 用户名和密码输入框
    tk.Label(window, text="用户名", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
    username_entry = tk.Entry(window, font=("Arial", 12), width=30)
    username_entry.pack(pady=5)

    tk.Label(window, text="密码", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
    password_entry = tk.Entry(window, show="*", font=("Arial", 12), width=30)
    password_entry.pack(pady=5)

    # 身份选择：普通用户和管理员
    identity_var = tk.StringVar(value="user")  # 默认为普通用户
    identity_label = tk.Label(window, text="请选择身份", font=("Arial", 12), bg="#f0f0f0")
    identity_label.pack(pady=5)

    radio_frame = tk.Frame(window, bg="#f0f0f0")
    tk.Radiobutton(radio_frame, text="普通用户", variable=identity_var, value="user", font=("Arial", 12), bg="#f0f0f0").pack(side="left", padx=20)
    tk.Radiobutton(radio_frame, text="管理员", variable=identity_var, value="admin", font=("Arial", 12), bg="#f0f0f0").pack(side="left", padx=20)
    radio_frame.pack(pady=5)

    def on_login():
        """登录按钮点击事件"""
        username = username_entry.get()
        password = password_entry.get()
        identity = identity_var.get()  # 获取选中的身份

        if not username or not password:
            messagebox.showerror("登录失败", "请输入用户名和密码")
            return

        # 调用 login_user 来验证用户
        flag = login_user(username, password, identity)
        if flag == 1:
            shenfen = "普通用户" if identity=="user" else "管理员"
            messagebox.showinfo("登录成功!", f"欢迎 {shenfen} 用户！")
            window.destroy()
            # 跳转到主界面
            import ui.main_window
            ui.main_window.main_window(identity)
        elif flag == -1:
            messagebox.showerror("登录失败！", "您的用户名或密码不正确")
        else :
            messagebox.showerror("登录失败！", "您没有此权限")

    # 登录按钮
    login_button = tk.Button(window, text="登录", command=on_login, font=("Arial", 14), bg="#4CAF50", fg="white", width=20)
    login_button.pack(pady=20)

    # 注册按钮，点击后跳转到注册界面
    def on_register():
        """跳转到注册界面"""
        window.destroy()  # 关闭当前窗口
        ui.register.register_window()  # 显示注册界面

    register_button = tk.Button(window, text="注册", command=on_register, font=("Arial", 14), bg="#2196F3", fg="white", width=20)
    register_button.pack(pady=10)

    window.mainloop()
