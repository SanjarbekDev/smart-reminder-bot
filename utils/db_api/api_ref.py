import sqlite3

class data_db:
    def __init__(self,path_db="main.db") -> None:
        self.path_db=path_db

    @property
    def db_connect(self):
        return sqlite3.connect(self.path_db)

    def execute(self,sql:str,parametrs:tuple=None,fetchall=False,fetchone=False,commit=False):
        if not parametrs:
            parametrs=()
        conn=self.db_connect
        # conn.set_trace_callback(logger)
        cur=conn.cursor()
        data=None
        cur.execute(sql,parametrs)

        if commit:
            conn.commit()
        if fetchall:
            data=cur.fetchall()
        if fetchone:
            data=cur.fetchone()
        return data

    def create_table(self,table_name,**kwargs):
        body=str()
        for column,datatype in kwargs.items():
            body+=" ".join([column,datatype,','])
        body=body[:-1]
        sql=f"""CREATE TABLE IF NOT EXISTS {table_name}(
            {body}
            );"""
        try:
            self.execute(sql,commit=True)
        except:
            raise 'syntax error:sql command not found'

    @staticmethod
    def format_args(sql, parameters: dict):
        #sql='CREATE TABLE Student'
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())
    
    def add_to_table(self,table_name,parametrs:dict=None):
        if not parametrs:
            parametrs={}
            raise "Error: parametrs is empty"
        que=",".join(list('?'*len(parametrs.keys())))
        sql=f"INSERT INTO {table_name}{tuple(parametrs.keys())} VALUES({que})"
        return self.execute(sql=sql,parametrs=tuple(parametrs.values()),commit=True)#sql,tuple(parametrs.values())

    def info(self,table_name:str):
        #sql="PRAGMA [database.]table_info( table_name );"
        sql=f"PRAGMA table_info( {table_name} );"
        result=''
        for No,col_name,data_type,size,place,count in self.execute(sql=sql,fetchall=True):
            result+=f"|| {No}, {col_name}, {data_type}, {size}, {place}, {count} ||\n"
        return result

    def get_all(self,table_name:str):
        sql=f"SELECT * FROM {table_name};"
        return self.execute(sql,fetchall=True)
    
    def drop_table(self,table_name:str):
        sql=f"DROP TABLE IF EXISTS {table_name};"
        return self.execute(sql,commit=True)

    def counter(self,table_name:str):
        sql=f"SELECT COUNT(*) FROM {table_name};"
        return self.execute(sql,fetchone=True)

    def filter(self,table_name:str, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = f"SELECT * FROM {table_name} WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql=sql,parametrs=parameters,fetchone=True)

    def get_filters(self,table_name:str,select:str, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = f"SELECT {select} FROM {table_name} WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql=sql,parametrs=parameters,fetchall=True)

    def select(self,collumn:str,table:str):
        sql=f"SELECT {collumn} FROM {table};"
        return self.execute(sql,fetchall=True)

    def update(self,table:str,set:str,where:str):
        sql=f"""
                UPDATE {table}
                SET {set}
                WHERE
                    {where}
            """
        return self.execute(sql,commit=True)

    def delete(self,table:str,where:str):
        sql=f"""
            DELETE FROM {table}
            WHERE {where};
        """
        return self.execute(sql,commit=True)
        
# def logger(statement):
#     print(f"""
# ##############################################################################################################       
# Executing: 
# {statement}
# ##############################################################################################################
# """)