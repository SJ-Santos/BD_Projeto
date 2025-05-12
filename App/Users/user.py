def create_user(cursor,user):
    cursor.execute(f"CREATE USER '{user['username']}'@'{user['host']}' IDENTIFIED BY '{user['password']}' ")

