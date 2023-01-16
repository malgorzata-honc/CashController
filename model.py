import sqlite3

class Model:
    def __init__(self):
        self.conn = sqlite3.connect('cash_controler.db')
        self.cur = self.conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY, title TEXT, category TEXT, date DATETIME, price INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS categories (id_category INTEGER PRIMARY KEY, category_name TEXT)")

        self.conn.commit()

    def addExpense(self, title, category, date, price):
        self.cur.execute ("INSERT INTO expenses VALUES (NULL, ?,?,?,?)", (title, category, date, price))
        self.conn.commit()

    def addCategory(self, new_category):
        self.cur.execute ("INSERT INTO categories VALUES (NULL, ?)", (new_category,))
        self.conn.commit()

    def deleteExpense(self, id):
        self.cur.execute ("DELETE FROM expenses WHERE id=?", (id,))
        self.conn.commit()

    def getAllExpenses(self):
        self.cur.execute("SELECT * FROM expenses")
        all=self.cur.fetchall()
        self.conn.commit()
        return all

    def searchExpense(self, title="", category="", date="", price=""):
        self.cur.execute ("SELECT * FROM expenses WHERE title=? OR category=? OR date =? OR price =?", (title, category, date, price))
        result=self.cur.fetchall()
        return result

    def getCategories(self):
        self.cur.execute("SELECT DISTINCT category_name FROM categories")
        categories=self.cur.fetchall()
        return categories

    def getGraphData(self):
        self.cur.execute("SELECT date, sum(price) FROM expenses GROUP BY date ORDER BY date")
        result=self.cur.fetchall()
        return result

    def getExpensesSum(self):
        self.cur.execute("SELECT sum(price) FROM expenses")
        sum=self.cur.fetchall()
        return sum

    def getPieChartData(self):
        self.cur.execute("SELECT sum(price), category FROM expenses GROUP BY category ")
        pie_chart=self.cur.fetchall()
        return pie_chart

    def __del__ (self):
        self.conn.close()   
