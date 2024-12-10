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