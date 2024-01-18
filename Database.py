# import pandas as pd
# from sqlalchemy import create_engine
#
#
# def SaveToDatabase(df):
#     server_name = 'DESKTOP-V5J0UI8'
#     database_name = 'PropertyManager'
#     table_name = 'QuickLook'
#     connection_string = f"mssql+pyodbc://{server_name}/{database_name}?driver=ODBC+Driver+17+for" \
#                                             f"+SQL+Server&Trusted_Connection=yes"
#     engine = create_engine(connection_string)
#     df.to_sql(name=table_name, con=engine, index=False, if_exists='append')
#
#
# def ReadFromDatabase():
#     server_name = 'DESKTOP-V5J0UI8'
#     database_name = 'PropertyManager'
#     table_name = 'QuickLook'
#     connection_string = f"mssql+pyodbc://{server_name}/{database_name}?driver=ODBC+Driver+17+for" \
#                         f"+SQL+Server&Trusted_Connection=yes"
#     engine = create_engine(connection_string, echo=True)
#     df = pd.read_sql(f'Select * FROM {table_name}', con=engine)
#     return df
