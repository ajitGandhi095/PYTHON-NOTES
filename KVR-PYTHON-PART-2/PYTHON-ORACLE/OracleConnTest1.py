#Program for Demonstrating how to get Connection from Oracle Database
#OracleConnTest1.py
import oracledb as orc# Step-1
try:
    con=orc.connect("system/tiger@localhost/orcl") # Step-2
    print("Type of con=",type(con))
    print("Python Program Obtains Connection from Oracle DB")
except orc.DatabaseError as db:
    print("Problem in Data Base Connection: ",db)
