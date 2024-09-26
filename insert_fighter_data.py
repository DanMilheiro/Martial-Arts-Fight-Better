import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('C:\\Users\\Service 2\\Martial-Arts-Fight-Better\\mma_fighters.db')
cursor = conn.cursor()

# Drop the fighters table if it exists
cursor.execute('DROP TABLE IF EXISTS fighters')

# Create the fighters table
cursor.execute('''
CREATE TABLE fighters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    real_name TEXT NOT NULL,
    nickname TEXT NOT NULL,
    weight_class TEXT NOT NULL,
    wins INTEGER DEFAULT 0,
    losses INTEGER DEFAULT 0,
    draws INTEGER DEFAULT 0,
    grappling_skill INTEGER DEFAULT 0,
    submission_skill INTEGER DEFAULT 0,
    striking_skill INTEGER DEFAULT 0,
    height INTEGER DEFAULT 0,
    reach INTEGER DEFAULT 0,
    age INTEGER DEFAULT 0,
    recent_activity INTEGER DEFAULT 0,
    stamina INTEGER DEFAULT 0,
    strength INTEGER DEFAULT 0
)
''')

# Function to insert fighter data
def insert_fighter(real_name, nickname, weight_class, wins=0, losses=0, draws=0):
    cursor.execute('''
    INSERT INTO fighters (real_name, nickname, weight_class, wins, losses, draws)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (real_name, nickname, weight_class, wins, losses, draws))
    conn.commit()

# Fighter data to insert (replace with your data)
fighter_data = [
    ("Zarrukh Adashev", "The Lion", "Flyweight", 4, 4, 0),
    ("Jesus Aguilar", "Jesus Aguilar", "Flyweight", 11, 2, 0),
    ("Amir Albazi", "The Prince", "Flyweight", 17, 1, 0),
    ("Asu Almabayev", "Zulfikar", "Flyweight", 20, 2, 0),
    ("Victor Altamirano", "El Magnifico", "Flyweight", 12, 4, 0),
    ("Jaime Alvarez", "Jaime Alvarez", "Flyweight", 7, 1, 0),
    ("Juan Andres Luna", "Juan Andres Luna", "Flyweight", 0, 1, 0),
    ("Adam Antolin", "Captain Chaos", "Flyweight", 13, 3, 0),
    ("Arman Ashimov", "Arman Ashimov", "Flyweight", 0, 0, 0),
    ("Askar Askarov", "Bullet", "Flyweight", 14, 1, 1),
    ("Ali Bagautinov", "Puncher", "Flyweight", 14, 5, 0),
    ("Daniel Barez", "Daniel Barez", "Flyweight", 16, 6, 0),
    ("Chris Beal", "The Real Deal", "Flyweight", 10, 3, 0),
    ("Marco Beltran", "Psycho", "Flyweight", 8, 7, 0),
    ("Joseph Benavidez", "Joseph Benavidez", "Flyweight", 28, 8, 0),
    ("Ryan Benoit", "Baby Face", "Flyweight", 10, 8, 0),
    ("Magomed Bibulatov", "Chaborz", "Flyweight", 14, 2, 0),
    ("Denys Bondar", "Psycho", "Flyweight", 14, 5, 0),
    ("Rogerio Bontorin", "Rogerio Bontorin", "Flyweight", 17, 4, 0),
    ("Kevin Borjas", "El Gallo Negro", "Flyweight", 9, 3, 0),
    ("Jarred Brooks", "The Monkey God", "Flyweight", 14, 2, 0),
    ("Felipe Bunes", "Felipinho", "Flyweight", 13, 7, 0),
    ("Ricky Calatayud", "Ricky Calatayud", "Flyweight", 0, 0, 0),
    ("Will Campuzano", "Will Campuzano", "Flyweight", 13, 6, 0),
    ("Chico Camus", "The King", "Flyweight", 14, 7, 0),
    ("Carlos Candelario", "The Cannon", "Flyweight", 8, 3, 0),
    ("Ronaldo Candido", "Pacman", "Flyweight", 5, 2, 0),
    ("Chris Cariaso", "Kamikaze", "Flyweight", 17, 8, 0),
    ("Clayton Carpenter", "Clayton Carpenter", "Flyweight", 7, 0, 0),
    ("Edgar Chairez", "Puro Chicali", "Flyweight", 11, 6, 0),
    ("SeungGuk Choi", "SeungGuk Choi", "Flyweight", 7, 3, 0),
    ("Mark Climaco", "Mark Climaco", "Flyweight", 1, 1, 0),
    ("Davi Costa", "Davi Costa", "Flyweight", 0, 0, 0),
    ("Alessandro Costa", "Nono", "Flyweight", 14, 4, 0),
    ("Emilio Cuellar", "Emilio Cuellar", "Flyweight", 0, 0, 0),
    ("Santo Curatolo", "Santo Curatolo", "Flyweight", 0, 1, 0),
    ("Peter Danesoe", "Peter Danesoe", "Flyweight", 1, 1, 0),
    ("Rafael de Freitas", "Barata (Cockroach)", "Flyweight", 0, 0, 0),
    ("Carls John De Tomas", "CJ", "Flyweight", 8, 2, 0),
    ("Wallen Del Rosario", "Wallen Del Rosario", "Flyweight", 0, 1, 0),
    ("Victor Dias", "Crazy Horse", "Flyweight", 8, 0, 0),
    ("Felipe dos Santos", "Lipe Detona", "Flyweight", 8, 2, 0),
    ("Oleksandr Doskalchuk", "Oleksandr Doskalchuk", "Flyweight", 10, 2, 0),
    ("Riley Dutro", "The Perfect Storm", "Flyweight", 14, 4, 0),
    ("David Dvorak", "The Undertaker", "Flyweight", 20, 6, 0),
    ("Roybert Echeverria", "The Unbroken", "Flyweight", 0, 1, 0),
    ("Joao Elias", "Joao Elias", "Flyweight", 0, 1, 0),
    ("Steve Erceg", "Astroboy", "Flyweight", 12, 3, 0),
    ("Jordan Espinosa", "Jordan Espinosa", "Flyweight", 15, 9, 0),
    ("Rafael Estevam", "Macapa", "Flyweight", 12, 0, 0),
    ("Shaun Etchell", "Shaun Etchell", "Flyweight", 0, 1, 0),
    ("Josh Ferguson", "Taz", "Flyweight", 7, 5, 0),
    ("Erisson Ferreira", "Erisson Ferreira", "Flyweight", 1, 1, 0),
    ("Francisco Figueiredo", "Sniper", "Flyweight", 13, 5, 1),
    ("Jafel Filho", "Pastor", "Flyweight", 16, 3, 0),
    ("Jimmy Flick", "The Brick", "Flyweight", 17, 8, 0),
    ("Jussier Formiga", "Jussier Formiga", "Flyweight", 23, 8, 0),
    ("Kai Kara-France", "Don't Blink", "Flyweight", 25, 11, 0),
    ("Gustavo Gabriel", "Gustavo Gabriel", "Flyweight", 0, 0, 0),
    ("Elias Garcia", "Elias Garcia", "Flyweight", 6, 2, 0),
    ("Azamat Gashimov", "Azamat Gashimov", "Flyweight", 10, 3, 0),
    ("Willie Gates", "Whoop Ass", "Flyweight", 12, 7, 0),
    ("Louis Gaudinot", "Goodnight", "Flyweight", 6, 4, 0),
    ("Ulysses Gomez", "Useless", "Flyweight", 9, 4, 0),
    ("Malcolm Gordon", "X", "Flyweight", 14, 8, 0),
    ("Kevin Gray", "Pocket Herc", "Flyweight", 9, 4, 0),
    ("CJ Hamilton", "CJ Hamilton", "Flyweight", 11, 5, 0),
    ("Phil Harris", "Billy", "Flyweight", 22, 12, 0),
    ("Jason Harris", "Jason Harris", "Flyweight", 0, 1, 0),
    ("Benny Horowitz", "Benny Horowitz", "Flyweight", 5, 2, 0),
    ("Michael Lentz", "Mikey", "Flyweight", 0, 1, 0),
    ("Jussier Formiga", "Jussier Formiga", "Flyweight", 23, 8, 0),
    ("Kyle Machado", "Kyle Machado", "Flyweight", 3, 1, 0),
    ("Marlon Moraes", "Magic", "Flyweight", 23, 11, 0),
    ("Justin Scoggins", "The Beast", "Flyweight", 12, 6, 0),
    ("Francisco Rivera", "Cisco", "Flyweight", 11, 7, 0),
    ("Yuri Alcantara", "Marajo", "Flyweight", 35, 12, 0),
    ("Zubaira Tukhugov", "Zubaira Tukhugov", "Flyweight", 21, 5, 0),
    ("Takashi Sato", "Takashi Sato", "Flyweight", 0, 1, 0),
    ("Luca Simoes", "Luca Simoes", "Flyweight", 4, 3, 0),
    ("Yuta Sasaki", "Yuta Sasaki", "Flyweight", 0, 2, 0),
    ("Daniel Teymur", "Daniel Teymur", "Flyweight", 0, 1, 0),
    ("Gabe Tuttle", "The Samoan", "Flyweight", 1, 2, 0),
    ("Luigi Vendramini", "The Italian", "Flyweight", 9, 4, 0),
    ("Artem Lobov", "The Russian Hammer", "Flyweight", 13, 15, 0),
    ("Danny Ruiz", "Danny Ruiz", "Flyweight", 0, 2, 0),
    ("Luis Santos", "Sapo", "Flyweight", 64, 11, 0),
    ("Rodolfo Vieira", "The Black Belt Hunter", "Flyweight", 8, 1, 0),
    ("Bobby Nash", "Bobby Nash", "Flyweight", 8, 6, 0),
    ("Matt Sayles", "The Dragon", "Flyweight", 10, 5, 0),
    ("Gunnar Nelson", "Gunni", "Flyweight", 18, 6, 1),
    ("Jorge Patino", "Macaco", "Flyweight", 29, 13, 0),
    ("Charles Rosa", "Boston Strong", "Flyweight", 15, 7, 0),
    ("Dylan Toomey", "Dylan Toomey", "Flyweight", 5, 2, 0),
    ("Mickey Gall", "The Gift", "Flyweight", 7, 6, 0),
    ("Daniel Velasquez", "El Chino", "Flyweight", 0, 1, 0),
    ("Anthony Rocco Martin", "Tony", "Flyweight", 17, 6, 0),
    ("Marcin Prachnio", "Marcin Prachnio", "Flyweight", 14, 6, 0),
    ("Yoshihiro Akiyama", "Sexyama", "Flyweight", 15, 6, 0),
    ("Elizeu Zaleski dos Santos", "Capoeira", "Flyweight", 23, 8, 0),
    ("Kevin Lee", "The Motown Phenom", "Flyweight", 19, 8, 0),
]

# Insert each fighter into the database
for fighter in fighter_data:
    insert_fighter(fighter[0], fighter[1], fighter[2], fighter[3], fighter[4], fighter[5])

# Close the database connection
conn.close()

print("Fighter data inserted successfully.")
