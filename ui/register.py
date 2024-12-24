import tkinter as tk
from tkinter import messagebox
from db.utils import register_user  # 假设数据库操作方法已实现
from PIL import Image, ImageTk  # 导入Pillow库来处理图片

def register_window():
    """注册界面"""
    window = tk.Tk()
    window.title("注册")
    window.geometry("750x600")  # 设置窗口大小

    # 背景图片
    background_image = Image.open('./icons/background.jpg')  # 使用Pillow加载图片
    background_image = background_image.resize((750,600))  # 调整大小
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(window, image=background_photo)
    background_label.place(relwidth=1, relheight=1)  # 背景覆盖整个窗口

    # 标题
    title = tk.Label(window, text="注册", font=("Arial", 24, "bold"), bg="#f0f0f0")
    title.pack(pady=20)

    # 用户名输入框
    tk.Label(window, text="用户名", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
    username_entry = tk.Entry(window, font=("Arial", 12), width=30)
    username_entry.pack(pady=5)

    # 密码输入框
    tk.Label(window, text="密码", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
    password_entry = tk.Entry(window, show="*", font=("Arial", 12), width=30)
    password_entry.pack(pady=5)

    # 确认密码输入框
    tk.Label(window, text="确认密码", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
    confirm_password_entry = tk.Entry(window, show="*", font=("Arial", 12), width=30)
    confirm_password_entry.pack(pady=5)
    # 邮箱输入框
    tk.Label(window, text="邮箱", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
    email_entry = tk.Entry(window, font=("Arial", 12), width=30)
    email_entry.pack(pady=5)
    # 身份选择：军事迷和管理员
    identity_var = tk.StringVar(value="user")  # 默认为军事迷
    identity_label = tk.Label(window, text="请选择身份", font=("Arial", 12), bg="#f0f0f0")
    identity_label.pack(pady=5)

    radio_frame = tk.Frame(window, bg="#f0f0f0")
    tk.Radiobutton(radio_frame, text="军事迷", variable=identity_var, value="military", font=("Arial", 12), bg="#f0f0f0").pack(side="left", padx=20)
    tk.Radiobutton(radio_frame, text="管理员", variable=identity_var, value="admin", font=("Arial", 12), bg="#f0f0f0").pack(side="left", padx=20)
    radio_frame.pack(pady=5)

    def on_register():
        """注册按钮点击事件"""
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        identity = identity_var.get()  # 获取选中的身份

        if not username or not email or not password or not confirm_password:
            messagebox.showerror("注册失败", "请填写所有字段。")
            return

        if password != confirm_password:
            messagebox.showerror("注册失败", "两次密码输入不一致。")
            return

        if not validate_email(email):
            messagebox.showerror("注册失败", "请输入有效的邮箱地址。")
            return

        success = register_user(username, password, email,identity)
        if success:
            messagebox.showinfo("注册成功", "注册成功！请返回登录界面。")
            window.destroy()  # 关闭当前注册窗口
            import ui.login  # 导入登录界面
            ui.login.login_window()  # 显示登录界面
        else:
            messagebox.showerror("注册失败", "用户名已存在，注册失败。")

    def on_back_to_login():
        """返回登录界面"""
        window.destroy()  # 关闭注册窗口
        import ui.login  # 导入登录界面
        ui.login.login_window()  # 显示登录界面

    def validate_email(email):
        """简单邮箱验证"""
        return "@" in email and "." in email

    # 注册按钮
    register_button = tk.Button(window, text="注册", command=on_register, font=("Arial", 14), bg="#4CAF50", fg="white", width=20)
    register_button.pack(pady=20)

    # 返回按钮
    back_button = tk.Button(window, text="返回登录", command=on_back_to_login, font=("Arial", 14), bg="#FF5722", fg="white", width=20)
    back_button.pack(pady=10)

    window.mainloop()
