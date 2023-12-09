# import files
import os
from dotenv import load_dotenv
import requests
import json
import sqlite3
from assets import movieTracker

# loading env
load_dotenv()

# functionality
url = "https://api.themoviedb.org/3/search/movie?query=sarpatta&include_adult=false&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": os.environ.get("APITOKEN")
}

response = requests.get(url, headers=headers)
jsonData = json.loads(response.text)
for item in jsonData["results"]:
    print(item["id"])

# create db    
connection = sqlite3.connect("tracker.db")
cur = connection.cursor()
# table created
# cur.execute("CREATE TABLE movies(Movie, Director, Date, Rating)")

# update db
# cur.execute("""
# INSERT INTO movies VALUES
#             ('Pulp Fiction', 'Quentin Tarenteno', '20/01/2022', '***')
#             """)


# search for a movie
def searchMovie():
    pass

# add an entry in the tracker
def addMovie():
    pass

# print the movies in the terminal
def printMovies():
    firstRow = ["Number", "Movie Name", "Directed By", "Watched on", "Rating"]

    # Calculate the maximum lengths for formatting
    numbers = list(str(number + 1) for number in range(0, len(movies)))
    movieList = list(movie[0] for movie in movies)
    directorList = list(director[1] for director in movies)
    dateList = list(date[2] for date in movies)
    ratingList = list(rating[3] for rating in movies)

    biggest = [
        len(str(max(numbers + [firstRow[0]], key=len))),
        len(str(max(movieList + [firstRow[1]], key=len))),
        len(str(max(directorList + [firstRow[2]], key=len))),
        len(str(max(dateList + [firstRow[3]], key=len))),
        len(str(max(ratingList + [firstRow[4]], key=len)))
    ]

    # Create a list of movie information
    movieInfo = list([numbers[i], movieList[i], directorList[i], dateList[i], ratingList[i]] for i in range(0, len(movies)))

    rows = []
    for song in [firstRow] + movieInfo:
        row = []
        for i in range(0, len(song)):
            space = int((biggest[i] - len(str(song[i]))) / 2) + 1
            text = (" " * space + str(song[i]) + " " * space)

            if len(text) != biggest[i] + 2:
                text = text + " "

            row.append(text)

        rows.append("|" + "|".join(row) + "|")

    line = "\n|" + "-" * (len(rows[0]) - 2) + "|\n"
    print(line.replace("|", "+") + line.join(rows) + line.replace("|", "+"))

# clear the screen
def cls():
    os.system("clear")
    
# menu    
def menu():
    global movies
    options = {
        "Get your Movies" : printMovies,
        "Search" : searchMovie,
        "Add an entry" : addMovie
    }
    optionList = list((str(list(options).index(option) + 1) +". "+ option for option in list(options)))
    cls()
    while True:
        res = cur.execute("SELECT * FROM movies")
        movies = res.fetchall()
        
        print(movieTracker)
        print("\n".join(optionList))
        option = int(input())
        if option >= 0 and option <= len(options):
            cls()
            options[list(options)[int(option)-1]]()
            input("\nPress enter to continue")
        cls()

if __name__ == "__main__":
    menu()
            
            
            
            

