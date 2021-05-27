class Data:
    def __init__(self, high):
        self.high = high
        import sqlite3
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT * FROM game")
        
        values = c.fetchall()
        for value in values:
            let = value[0]
            if self.high > let:
                c.execute(f"""UPDATE game SET score = {self.high} WHERE score = {let}""")
                c.execute("SELECT * FROM game")
                print(f'You have beat the high score\nThe high score was {let}\nYou have made {self.high}')
                conn.commit()
            else:
                print('You dont made enough score to beat this high score {}'.format(value[0]))

        conn.commit()
        conn.close()


if __name__ == '__main__':
    Data(12563)