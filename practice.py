from flask import Flask #The FLASK framework (the webserver)
from flask import render_template  # For opening and read the HTML file and showing them as the webpage
from flask import redirect
from cs50 import SQL
from objects import *
import sqlite3

def getDictList_DB():
    con = sqlite3.connect('HandTrucks.db')
    cursorObj = con.cursor()

    rowSTRING2 = "["

    cursorObj.execute('SELECT * FROM Customer;')
    rows = cursorObj.fetchall()
    for row in rows:
        newRow = []
        c = Customer(row[0], row[1],row[2],row[3],row[4],row[5],row[6])
        rowSTRING2 += "{" + c.getDict() + "},"
    rowSTRING2 = rowSTRING2[0:-1]
    rowSTRING2 = rowSTRING2 + "]"
    # rowSTRING2 = eval(rowSTRING2)
    return rowSTRING2
print(getDictList_DB())

def getPDictList_DB():
    con = sqlite3.connect('HandTrucks.db')
    cursorObj = con.cursor()

    rowSTRING2 = "["

    cursorObj.execute('SELECT * FROM Product;')
    rows = cursorObj.fetchall()
    for row in rows:
        newRow = []
        p = Product(row[0], row[1],row[2],row[3])
        rowSTRING2 += "{" + p.getDict() + "},"
    rowSTRING2 = rowSTRING2[0:-1]
    rowSTRING2 = rowSTRING2 + "]"
    rowSTRING2 = eval(rowSTRING2)
    return rowSTRING2
print(getPDictList_DB())
    
    
    

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()

    todo = conn.execute('SELECT i.id, i.list_id, i.done, i.content, l.title \
                         FROM items i JOIN lists l \
                         ON i.list_id = l.id WHERE i.id = ?', (id,)).fetchone()

    lists = conn.execute('SELECT title FROM lists;').fetchall()

    if request.method == 'POST':
        content = request.form['content']
        list_title = request.form['list']

        if not content:
            flash('Content is required!')
            return redirect(url_for('edit', id=id))

        list_id = conn.execute('SELECT id FROM lists WHERE title = (?);',
                                 (list_title,)).fetchone()['id']

        conn.execute('UPDATE items SET content = ?, list_id = ?\
                      WHERE id = ?',
                     (content, list_id, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('edit.html', todo=todo, lists=lists)