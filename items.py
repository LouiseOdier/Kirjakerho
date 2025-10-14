import db

def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER by id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    
    for title, value in result:
        classes[title].append(value)

    return classes

def add_item(title, writer, description, user_id, classes, stars):
    sql = "INSERT INTO items (title, writer, user_id) VALUES (?, ?, ?)"
    db.execute(sql, [title, writer, user_id])

    item_id = db.last_insert_id()

    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [item_id, title, value])
        
    sql = "INSERT INTO descriptions (item_id, user_id, description, stars) VALUES (?, ?, ?, ?)"
    db.execute(sql, [item_id, user_id, description, stars])



def add_description(item_id, user_id, new_description, stars):
    sql = "INSERT INTO descriptions (item_id, user_id, description, stars) VALUES (?, ?, ?, ?)"
    db.execute(sql, [item_id, user_id, new_description, stars])

def get_descriptions(item_id):
    sql = """SELECT descriptions.description, users.id user_id, users.username
            FROM descriptions, users
            WHERE descriptions.item_id = ? AND descriptions.user_id = users.id
            ORDER BY descriptions.id ASC"""
    return db.query(sql, [item_id])

def get_stars(item_id):
    sql = """SELECT descriptions.stars FROM descriptions WHERE descriptions.item_id = ?"""
    return db.query(sql, [item_id])

def get_classes(item_id):
    sql = "SELECT title, value FROM item_classes WHERE item_id=?"
    return db.query(sql, [item_id])

def get_items():
    sql = "SELECT id, title FROM items ORDER BY title DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id,
                    items.title,
                    items.writer,
                    users.id user_id,
                    users.username
            FROM items, users
            WHERE items.user_id=users.id AND
            items.id=?"""
    result = db.query(sql, [item_id])
    return result[0] if result else None

def get_stars_description(item_id):
    sql = """SELECT descriptions.item_id,
                    descriptions.stars,
                    descriptions.description,
                    users.id user_id,
                    users.username
            FROM descriptions, users
            WHERE descriptions.user_id=users.id AND
            descriptions.item_id=?"""
    result = db.query(sql, [item_id])
    return result[0] if result else None

def update_item(item_id, title, writer, classes, description, stars):
    sql = """UPDATE items SET title = ?, writer = ? WHERE id = ? """
    db.execute(sql, [title, writer, item_id])

    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])

    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [item_id, title, value])

    sql = "UPDATE descriptions SET description = ?, stars = ? WHERE id = ?"
    db.execute(sql, [description, stars, item_id])

def remove_item(item_id):
    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM descriptions WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM items WHERE id = ? "
    db.execute(sql, [item_id])

def find_author(query):
    sql ="""SELECT id, title
            FROM items
            WHERE writer LIKE ?
            ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like])

def find_book_name(query):
    sql = """SELECT id, title
            FROM items
            WHERE title LIKE ?
            ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like])