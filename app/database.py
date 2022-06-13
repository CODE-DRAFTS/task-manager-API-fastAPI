from app import main


async def get_all_tasks():
    main.cursor.execute("""SELECT * FROM tbl_tasks""")
    return main.cursor.fetchall()

async def add_new_task( task):
    main.cursor.execute("""INSERT INTO tbl_tasks(title, completed) VALUES(%s, %s) RETURNING * """, (task.title, task.completed))
    main.conn.commit()
    return main.cursor.fetchone()

async def get_single_task( task_id: int):
    main.cursor.execute("""SELECT * FROM tbl_tasks WHERE task_id= %s""", (task_id,) )
    return main.cursor.fetchone()

async def update_task(task_id, title, completed):
    if title != None:
        main.cursor.execute("""UPDATE tbl_tasks SET title=%s WHERE task_id=%s RETURNING * """, (title,task_id))
    if completed != None:
         main.cursor.execute("""UPDATE tbl_tasks SET completed=%s WHERE task_id=%s RETURNING * """, (completed ,task_id))
    main.conn.commit()
    return main.cursor.fetchone()
    

async def delete_post( task_id: str):
    main.cursor.execute("""DELETE FROM tbl_tasks WHERE task_id=%s RETURNING * """, (task_id))
    main.conn.commit()
    return main.cursor.fetchone()
