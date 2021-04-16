import sqlite3

# ამყარებს კავშირს მონაცემთა ბაზასთან და ქმნის კურსორს
conn = sqlite3.connect('oscar_winners.sqlite')
c = conn.cursor()

# sql ბრძანებით oscar ცხრილიდან მოაქვს ყველა იმ მამაკაცი მსახიობის სახელი რომელმაც ოსკარი აიღო 25 წლამდე ასაკში
# და ბეჭდავს თითო სახელს თითო ხაზზე tuple–ის სახით
var = c.execute('''SELECT name FROM oscar WHERE age > 25 AND gender == "M";''').fetchall()
for each in var:
    print(each)


# იუზერს ეუბნება რომ შეიყვანოს სვეტების შესაბამისი მონაცემები და ამ მონაცემებს ამატებს insert ბრძანებით ცხრილში
try:
    year = int(input('enter a year: '))
except ValueError:
    year = None

try:
    age = int(input('enter actor age: '))
except ValueError:
    age = None

name = input('enter actor/actress name: ')
gender = input('enter actor/actress gender M or F: ')
if gender != 'M' or gender != 'F':
    gender = None

movie = input('enter a movie name: ')
c.execute('''INSERT INTO oscar (year, age, name, gender, movie)
VALUES (?, ?, ?, ?, ?);''', (year, age, name, gender, movie))

# იუზერს თხოვს შეიყვანოს ინდექსი და ფილმის სახელი რის შემდეგაც შეყვანილი ინდექსის სტრიქონზე ცვლის ფილმის სახელს
ind = int(input('enter an index from 1 to 178: '))
movie = input('enter a movie name: ')

c.execute('''UPDATE oscar SET movie = ? WHERE id = ?''', (movie, ind))

# მოცემული კოდი აგებს დიაგრამას მსახიობების ასაკის მიხედვით,
# დიაგრამაზე წარმოდგენილია რამდენმა მსახიობმა აიღო ოსკარი კოკრეტული ასაკის დიაპაზონში
import matplotlib.pyplot as plt
import numpy as np

ages1 = c.execute('''SELECT age FROM oscar WHERE age >= 18 AND age <= 30''').fetchall()
ages2 = c.execute('''SELECT age FROM oscar WHERE age > 30 AND age <= 45''').fetchall()
ages3 = c.execute('''SELECT age FROM oscar WHERE age > 45 AND age <= 60''').fetchall()
ages4 = c.execute('''SELECT age FROM oscar WHERE age > 60''').fetchall()

ages1 = len(ages1)
ages2 = len(ages2)
ages3 = len(ages3)
ages4 = len(ages4)

x = np.array(["18-30", "30-45", "45-60", "60+"])
y = np.array([ages1, ages2, ages3, ages4])

plt.bar(x, y)
plt.show()

c.close()
conn.close()
