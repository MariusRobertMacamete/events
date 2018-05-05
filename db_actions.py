import sqlite3

class DbConnect():

    def create_event_table(self):
        conn=sqlite3.connect('events.db')
        c=conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS events (name TEXT, description TEXT)')
        c.close()

    def insert_event(self, name, description):
        n=name
        d=description
        conn=sqlite3.connect('events.db')
        c=conn.cursor()
        c.execute('INSERT INTO events (name, description) VALUES (?, ?)',(n,d))
        conn.commit()
        c.close()

    def select_event(self):
        events_list=[]
        conn=sqlite3.connect('events.db')
        c=conn.cursor()
        c.execute('SELECT nume FROM events')
        conn.commit()
        list=c.fetchall()
        for l in list:
            for col in l:
                events_list.append(col)
        c.close()
        return events_list
