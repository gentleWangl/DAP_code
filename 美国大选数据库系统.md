# 美国大选数据库系统设计报告
**—————————基于tkinter库的数据库应用程序开发**




| 成员 | 相关工作 |
| ---- | ---- |
| [成员姓名1] | 需求分析与功能规划 |
| [成员姓名2] | 数据库架构设计 |
| [成员姓名3] | 数据采集与整理 |
| [成员姓名4] | 界面设计与用户体验优化 |
| [成员姓名5] | 代码编写与系统实现 |
| [成员姓名6] | 测试与调试 |
| [成员姓名7] | 文档撰写与项目管理 |



---

- [美国大选数据库系统设计报告](#美国大选数据库系统设计报告)
  - [一、数据库开发背景](#一数据库开发背景)
  - [二、需求分析](#二需求分析)
    - [2.1项目设计目标](#21项目设计目标)
    - [2.2功能需求分析](#22功能需求分析)
    - [2.3数据需求分析](#23数据需求分析)
    - [2.4数据流图](#24数据流图)
      - [2.4.1 顶层数据流图](#241-顶层数据流图)
      - [2.4.2 具体数据流图](#242-具体数据流图)
  - [三、概念设计](#三概念设计)
    - [3.1全局ER图](#31全局er图)
    - [3.2具体实体ER图](#32具体实体er图)
  - [四、逻辑设计](#四逻辑设计)
    - [4.1关系模式](#41关系模式)
    - [4.2构建表格](#42构建表格)
    - [4.3范式检验](#43范式检验)
    - [4.4完整性约束](#44完整性约束)
    - [4.5安全性约束](#45安全性约束)
  - [五、系统实现](#五系统实现)
    - [5.1系统功能一览表](#51系统功能一览表)
    - [5.2功能详细介绍及实现](#52功能详细介绍及实现)
    - [5.3关键代码](#53关键代码)
  - [六、设计亮点](#六设计亮点)
    - [6.1全面的数据记录](#61全面的数据记录)
    - [6.2规范的数据管理](#62规范的数据管理)
    - [6.3用户友好的界面设计](#63用户友好的界面设计)
  - [七、结束语](#七结束语)
    - [7.1遇到的障碍和解决的方式](#71遇到的障碍和解决的方式)
    - [7.2遗憾和存在的问题](#72遗憾和存在的问题)
    - [7.3心得体会](#73心得体会)
    - [7.4参考文献](#74参考文献)
---
## 一、数据库开发背景
美国总统大选是美国政治生活中的重要事件，涉及众多候选人、选举进程、财团支持以及各类相关事件等复杂信息。对这些信息进行有效的管理和分析，对于研究美国政治格局、选举动态以及政治与经济的相互关系具有重要意义。因此，我们构建了美国大选数据库系统，旨在全面、系统地记录和处理美国大选相关数据，为政治研究、选举分析等提供有力的数据支持。

## 二、需求分析
以下是本项目的用例图：
<img src="./icons/usecase.png">
### 2.1项目设计目标
本数据库系统旨在满足对美国大选相关信息的全面管理和分析需求。为研究人员、政治学者、选举观察者等提供准确、详细且结构化的数据，以便深入研究大选过程中的候选人表现、选举趋势、财团影响等方面。通过系统，用户能够方便地查询候选人基本信息、选举进程、得票情况，以及财团与候选人之间的支持关系等，为分析美国大选的政治生态和决策机制提供数据依据。

### 2.2功能需求分析
1. **数据录入功能**
    - 能够录入候选人的详细信息，包括姓名、别名、性别、种族、出生地、出生日期、毕业院校、党派、学历、教育经历、工作经历、成就、净资产等。
    - 记录候选人参选时间、退选原因及时间。
    - 输入选举进程中的关键事件及时间。
    - 登记财团的基本信息，如名称、历史、成员、财富等，以及财团对候选人的支持情况，包括支持金额和日期。
2. **数据查询功能**
    - 根据候选人姓名、党派等条件查询候选人基本信息。
    - 按选举时间查询候选人参选或退选情况。
    - 查看选举进程中的具体事件。
    - 统计候选人在不同地区的得票信息。
    - 检索财团对候选人的支持记录。
3. **数据更新功能**
    - 实时更新候选人的最新动态，如工作成果、净资产变化等。
    - 修正选举进程中的事件信息。
    - 调整财团财富数据及支持情况。
4. **数据删除功能**
    - 删除错误或过期的候选人信息（在合理权限下）。
    - 清除不再相关的选举事件记录。
    - 移除无效的财团支持数据。

### 2.3数据需求分析
1. **候选人相关数据**
    - 基本信息：姓名、别名、性别、种族、出生地、出生日期、毕业院校、党派、学历、教育经历、工作经历、成就、净资产等，用于全面描述候选人背景。
    - 参选与退选：参选时间、退选原因及时间，跟踪候选人选举历程。
    - 选举进程：在选举过程中的关键事件及时间，记录候选人活动轨迹。
2. **选举事件数据**
    - 事件基本信息：事件ID、开始时间、结束时间、内容，涵盖各类选举相关活动。
    - 候选人关联：候选人参与事件的记录，明确事件与候选人的关系。
3. **财团相关数据**
    - 财团信息：名称、历史、成员、财富，展示财团基本情况。
    - 支持关系：对候选人的支持金额和日期，反映财团对选举的影响。
4. **得票信息数据**
    - 候选人得票：候选人ID、投票时间、地区、票数、结果，统计选举投票情况。

### 2.4数据流图
#### 2.4.1 顶层数据流图
<img src="./icons/dfd1.png"></img>
#### 2.4.2 具体数据流图
<img src="./icons/dfd2.png"></img>
## 三、概念设计
### 3.1全局ER图
据以上的需求分析，经过仔细考虑，我们设计了如下 ER 关系图；
<img src="./icons/ER.png">


### 3.2具体实体ER图
1. **候选人实体及其属性**
    <img src="./icons/ER1.png">
2. **候选人名单实体及其属性**
    <img src="./icons/ER2.png">
3. **退选人名单实体及其属性**
    <img src="./icons/ER3.png">
4. **选举进程实体及其属性**
    <img src="./icons/ER4.png"> 
5. **事件实体及其属性**
    <img src="./icons/ER5.png">

6. **选举得票信息实体及其属性**

    <img src="./icons/ER6.png">
7. **财团实体及其属性**
    <IMG SRC="./icons/ER7.png"> 

## 四、逻辑设计
### 4.1关系模式
1. 候选人（Candidate）（<u>CandidateID</u>, Name, Alias, Gender, Ethnicity, Birthplace, Birthdate, University, Party, Degree, Education, Works, Achievements, NetWorth）
2. 候选人名单（CandidateList）（<u>CandidateList_ID</u>,CandidateID, ElectionDate）
3. 退选人名单（WithdrawnCandidates）（<u>WithdrawnCandidates_ID</u>,CandidateID,ElectionDate, WithdrawReason, WithdrawDate）
4. 选举进程（ElectionProcess）（<u>ProcessID</u>, CandidateID, Time, ProcessDescription）
5. 事件（Event）（<u>EventID</u>, StartTime, EndTime, Content）
6. 选举事件（ElectionEvent）（<u>ElectionEvent_ID</u>,EventID, CandidateID）
7. 选举得票信息（ElectionVotes）（<u>VoteID</u>, CandidateID, Time, Region, Votes_count, Result）
8. 财团（Corporation）（<u>CorporationID</u>, Name, History, Members, Wealth）
9. 候选人财团支持（CandidateSupport）（<u>SupportID</u>, CandidateID, CorporationID, SupportAmount, SupportDate）
根据以上关系模式，可在数据库软件 SQL 中分析出如下关系表：
<img src="./icons/database1.png">
###  4.2构建表格  
候选人表
    <IMG SRC="./icons/TAB1.png">
候选人名单表
    <IMG SRC="./icons/TAB1.png">
候选人支持表
    <IMG SRC="./icons/TAB1.png">  
财团表    
  <IMG SRC="./icons/TAB1.png">  
竞选事件表
    <IMG SRC="./icons/TAB1.png">  
竞选进程表
  <IMG SRC="./icons/TAB1.png">
选举得票表
      <IMG SRC="./icons/TAB1.png"> 
事件表
   <IMG SRC="./icons/TAB1.png">
竞选人退选表
    <IMG SRC="./icons/TAB1.png">

### 4.3范式检验

1. **初始表结构**
    - 根据实际情况，我们可以得到初始表如下：
        - Candidate(<u>CandidateID</u>, Name, Alias, Gender, Ethnicity, Birthplace, Birthdate, University, Party, Degree, Education, Works, Achievements, NetWorth)
        - CandidateList(<u>CandidateList_ID</u>,CandidateID, ElectionDate)
        - WithdrawnCandidates(<u>WithdrawnCandidates_ID</u>,CandidateID,ElectionDate, WithdrawReason, WithdrawDate)
        - ElectionProcess(<u>ProcessID</u>, CandidateID, Time, ProcessDescription)
        - Event(<u>EventID</u>, StartTime, EndTime, Content)
        - ElectionEvent(<u>ElectionEvent_ID</u>,EventID, CandidateID)
        - ElectionVotes(<u>VoteID</u>, CandidateID, Time, Region, Votes_count, Result)
        - Corporation(<u>CorporationID</u>, Name, History, Members, Wealth)
        - CandidateSupport(<u>SupportID</u>, CandidateID, CorporationID, SupportAmount, SupportDate)

2. 分析各关系模式中的函数依赖关系，判断是否满足范式要求。例如，在候选人关系模式中，候选人ID决定了其他所有属性，不存在部分依赖和传递依赖，满足第三范式（3NF）。
3. 检查其他关系模式，如候选人名单关系模式中，候选人名单ID为主键，候选人ID为外键参照候选人关系模式，不存在非主属性对码的部分依赖和传递依赖，也满足3NF。同理，其他关系模式经分析也满足相应范式要求，确保了数据的规范性和减少数据冗余。





### 4.4完整性约束
1. **实体完整性约束**
    - 每个关系模式中的主键（如候选人关系模式中的CandidateID等）不能为空且唯一，确保每个实体的唯一性和可识别性。
2. **参照完整性约束**
    - 外键（如候选人名单关系模式中的CandidateID参照候选人关系模式中的CandidateID等）必须在被参照关系的主键值中存在，保证数据的一致性和关联性。
3. **用户定义完整性约束**
    - 对属性值的范围、格式等进行约束，例如出生日期必须符合日期格式，净资产应为非负数等，确保数据的有效性和合理性。

### 4.5安全性约束
1. **用户权限管理**
    - 定义不同用户角色，如管理员、普通查询用户等，为其分配不同的操作权限。管理员拥有对数据的插入、更新、删除和查询全部权限，普通查询用户仅具有查询权限，防止非法操作和数据泄露。
2. **数据加密**
    - 对敏感数据（如候选人的净资产等财务信息）进行加密存储，保障数据的保密性，防止数据在存储和传输过程中被窃取或篡改。

## 五、系统实现
本系统数据库构建使用**Mysql8.5.3**,编程语言使用**python3**,界面绘制使用**tkinter**库
### 5.1系统功能一览表
<img src="./icons/SystemFunction.png">

1. **数据管理功能**
    - 数据录入：支持各类数据的添加，包括候选人、选举事件、财团等信息。
    - 数据更新：允许对已有数据进行修改，确保信息的准确性。
    - 数据删除：可删除无用或错误数据，维护数据库的精简性。
2. **数据查询功能**
    查询各个表的信息
3. **界面交互功能**
    - 用户友好界面：提供直观、简洁的操作界面，方便用户操作。
    - 操作反馈：及时显示操作结果，如数据添加成功提示、查询结果展示等。

### 5.2功能详细介绍及实现
1. **主界面**
    <img src="./icons/mainpage.png">
2. **数据查询功能,点击左侧绿色按钮即可查询相应数**
   <img src="./icons/query.png">

3. **数据导入**
   点击**添加记录**按钮，即可向相应的表(左边选中的)插入记录
   <img src="./icons/insert.png">
4. **数据删除功能**
   选中想要删除的记录，点击**删除选中记录**按钮，即可成功删除
   <img src="./icons/delete1.png">
   删除成功！
   <img src="./icons/delete2.png">
5. **数据更改**
    点击**修改选中记录**按钮，即可修改记录
   <img src="./icons/update1.png">
   修改成功！
   <img src="./icons/update2.png">
### 5.3关键代码
1. **界面生成函数(构造函数部分)**
   ```python
   class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

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
   ```
2. **数据库操作相关函数**
   ```python
     # db/utils.py

    import mysql.connector
    from mysql.connector import Error
    from db.entity import Candidate, CandidateList, WithdrawnCandidates, ElectionProcess, Event, ElectionEvent, ElectionVotes, Corporation, CandidateSupport


    def create_connection():
        """创建并返回数据库连接"""
        try:
            connection = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='1234',
                database='presidentialelection'
            )
            if connection.is_connected():
                return connection
        except Error as e:
            raise Exception(f"数据库连接错误: {str(e)}")


    def insert_data(table, data):
        """向指定表中插入数据"""
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            columns = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            try:
                cursor.execute(query, tuple(data.values()))
                connection.commit()
            except Error as e:
                connection.rollback()
                raise Exception(f"插入数据时发生错误: {str(e)}")
            finally:
                cursor.close()
                connection.close()


    def update_data(table, data, where_clause):
        """更新表中的数据"""
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
            query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
            try:
                cursor.execute(query, tuple(data.values()))
                connection.commit()
            except Error as e:
                connection.rollback()
                raise Exception(f"更新数据时发生错误: {str(e)}")
            finally:
                cursor.close()
                connection.close()


    def delete_data(table, where_clause):
        """删除表中的数据"""
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = f"DELETE FROM {table} WHERE {where_clause}"
            try:
                cursor.execute(query)
                connection.commit()
            except Error as e:
                connection.rollback()
                raise Exception(f"删除数据时发生错误: {str(e)}")
            finally:
                cursor.close()
                connection.close()
    def fetch_data_with_join(table_name, columns):
        """执行带JOIN的查询并返回结果"""
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                # 生成查询语句，处理外键
                if table_name == "CandidateList":
                    query = """
                        SELECT CandidateList_ID, Candidate.Name, ElectionDate
                        FROM CandidateList
                        JOIN Candidate ON CandidateList.CandidateID = Candidate.CandidateID
                    """
                elif table_name == "WithdrawnCandidates":
                    query = """
                        SELECT WithdrawnCandidates_ID, Candidate.Name, ElectionDate, WithdrawReason, WithdrawDate
                        FROM WithdrawnCandidates
                        JOIN Candidate ON WithdrawnCandidates.CandidateID = Candidate.CandidateID
                    """
                elif table_name == "ElectionProcess":
                    query = """
                        SELECT ProcessID, Candidate.Name, Time, ProcessDescription
                        FROM ElectionProcess
                        JOIN Candidate ON ElectionProcess.CandidateID = Candidate.CandidateID
                    """
                elif table_name == "ElectionEvent":
                    query = """
                        SELECT ElectionEvent_ID, Event.Content, Candidate.Name
                        FROM ElectionEvent
                        JOIN Event ON ElectionEvent.EventID = Event.EventID
                        JOIN Candidate ON ElectionEvent.CandidateID = Candidate.CandidateID
                    """
                elif table_name == "ElectionVotes":
                    query = """
                        SELECT VoteID, Candidate.Name, Time, Region, Votes_count, Result
                        FROM ElectionVotes
                        JOIN Candidate ON ElectionVotes.CandidateID = Candidate.CandidateID
                    """
                elif table_name == "Corporation":
                    query = """
                        SELECT CorporationID, Name, History, Members, Wealth
                        FROM Corporation
                    """
                elif table_name == "CandidateSupport":
                    query = """
                        SELECT SupportID, Candidate.Name, Corporation.Name, SupportAmount, SupportDate
                        FROM CandidateSupport
                        JOIN Candidate ON CandidateSupport.CandidateID = Candidate.CandidateID
                        JOIN Corporation ON CandidateSupport.CorporationID = Corporation.CorporationID
                    """
                else:
                    query = f"SELECT {', '.join(columns)} FROM {table_name}"

                cursor.execute(query)
                result = cursor.fetchall()
                return result
            except Error as e:
                raise Exception(f"查询数据时发生错误: {str(e)}")
            finally:
                cursor.close()
                connection.close()
   ```
3. **数据插入代码示例（以候选人信息插入为例）**
```sql
INSERT INTO Candidate (Name, Alias, Gender, Ethnicity, Birthplace, Birthdate, University, Party, Degree, Education, Works, Achievements, NetWorth)
VALUES
('Joe Biden','Biden', 'Male','Caucasian', 'Scranton', '1942-11-20', 'University of Delaware','Democratic', 'BA', 'Undergraduate', 'Infrastructure Bill','46th President', [具体净资产数值]);
```
4. **数据查询代码示例（查询所有候选人信息）**
```sql
SELECT * FROM Candidate;
```
5. **数据更新代码示例（更新财团财富数据）**
```sql
UPDATE Corporation SET Wealth = Wealth + [增加的金额] WHERE CorporationID = [指定财团ID];
```
6. **数据删除代码示例（删除指定候选人记录）**
```sql
DELETE FROM Candidate WHERE CandidateID = [指定候选人ID];
```

## 六、设计亮点
### 6.1全面的数据记录
系统涵盖了美国大选从候选人到选举进程、财团支持等全方位的信息，能够为深入研究美国大选提供丰富的数据基础，有助于全面分析选举背后的政治、经济等多方面因素。

### 6.2规范的数据管理
在逻辑设计阶段遵循范式理论，确保数据的规范性，减少数据冗余和更新异常。同时，严格的完整性和安全性约束保障了数据的准确性、一致性和保密性，提高了系统的可靠性和稳定性。

### 6.3用户友好的界面设计
简洁直观的操作界面，易于上手，无论是专业研究人员还是普通选举观察者都能轻松使用，降低了使用门槛，提高了系统的可用性和实用性。

## 七、结束语
### 7.1遇到的障碍和解决的方式
1. **数据复杂性处理**：美国大选相关数据繁多且关系复杂，在概念设计阶段准确梳理实体与关系遇到困难。通过参考大量政治选举资料，深入了解大选流程和相关因素，多次讨论和修改ER图，最终确定了合理的实体关系模型。
2. **数据准确性保障**：在数据录入过程中，确保数据的准确性是一大挑战。为此，增加了详细的数据验证机制，对输入数据进行严格的格式检查、范围限制和逻辑校验，同时对部分重要数据进行人工核对，提高了数据的质量。

### 7.2遗憾和存在的问题
1. **实时数据更新的局限性**：虽然系统能够实现数据的更新，但在实时获取最新大选动态并及时更新到数据库方面存在一定滞后性，主要依赖人工录入更新，无法实现自动化的实时数据抓取。
2. **数据分析功能深度不足**：目前系统主要侧重于数据的管理和查询，在数据分析功能上相对薄弱，缺乏一些高级的数据分析算法和可视化工具，无法为用户提供更深入的数据洞察和直观的数据分析结果展示。

### 7.3心得体会
1. **数据库设计的重要性**：通过本次项目，深刻体会到数据库设计是整个系统的基石。合理的概念设计能够准确反映现实世界中的复杂关系，逻辑设计的规范性直接影响数据的质量和系统的性能。在设计过程中，每一个决策都需要权衡数据的完整性、一致性、冗余度和查询效率等多方面因素，确保系统的稳定性和可用性。
2. **实践能力的提升**：从需求分析到系统实现，每个环节都锻炼了实际动手能力。学会了运用数据库理论知识解决实际问题，掌握了数据库设计工具和开发技术，提高了编程能力和解决实际工程问题的能力。同时，也认识到在项目开发过程中团队协作的重要性，成员之间的沟通和协作能够有效提高工作效率，解决遇到的各种问题。

### 7.4参考文献
[1]施伯乐等. 数据库系统教程. 高等教育出版社.
[2]明日科技. 张跃廷等. ASP.NET程序开发范例宝典.
[3]闪四清. SQL Server 2008基础教程. 清华大学出版社.
[4]《Visual C#.NET 2008程序设计案例集锦》. 中国水利水电出版社.
[5]邱李华,李晓黎,张玉花. SQL Server 2000数据库应用教程. 人民邮电出版社, 2007.
[6]Abraham Silberschatz,Henry F.Korth,S.Sudarshan. 数据库系统概念. 高等教育出版社. 2006.
[7]孙一林,彭波.《JSP数据库编程实例》. 清华大学出版社. 2002年8月:30 - 120.