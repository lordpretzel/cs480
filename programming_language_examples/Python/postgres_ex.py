import psycopg2

def exec_and_print_result(c,sql):
    """
    Execute a query sql using cursor c and print its results
    """
    try:
        print(80 * "=" + f"\nQUERY: {sql}\n")
        c.execute(sql)
        rows = c.fetchall() # here we use fetchall to get all results at once
        for r in rows:
            print(f"{r}")        
    except:
        print(f"execution of query {sql} did fail")

# modify this if you are using different connection parameters        
connection = {
    'dbname': 'university',
    'user': 'postgres',
    'host': '127.0.0.1',
    'password': 'test',
    'port': 5450
    }

def connect(connsettings=connection):
    try:
        conn = psycopg2.connect(**connsettings)
        return conn
    except Exception as e:
        print(f"I am unable to connect to the database with connection parameters:\n{connection}\n{e}")
        exit(1)
    
def connect_and_run_query(sql, connsettings=connection):
    conn = connect(**connsettings)
    print("Connected successfully")
    cur = conn.cursor()
    exec_and_print_result(cur, sql)
    cur.close()
    conn.close()
    


# Create a connection
conn = connect(connection)
# Create a curson
cur = conn.cursor()

# Execute a statements and fetch results
try:
    cur.execute("SELECT name FROM student")
except:
    print("I can't SELECT from student")

# now let's fetch all the rows and print them
rows = cur.fetchall()
print("\nResults: \n")
for row in rows:
    print(f"   {row}")

# now a query with more result columns
try:
    cur.execute("SELECT id, name, tot_cred FROM student ORDER BY name ASC")
except Exception as e:
    print(f"I can't SELECT from student:\n{e}")

rows = cur.fetchall()
print("\nResults: \n")
for row in rows:
    # Rows are encoded as tuples
    print(f"{row}")
    print(f" or to access a particular column (2nd one): {row[1]}")

# transactions are explicitely terminated by running con.rollback() or con.commit()
cur.execute("DELETE FROM student")
conn.rollback()
exec_and_print_result(cur, "SELECT count(*) FROM student")

# close the connection
cur.close()

# close the connection
conn.close()
