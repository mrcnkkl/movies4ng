## movies4ng
Basic movie database interacting with external API, exposing own API

base url: https://movies4ng.herokuapp.com/ 

POST /movies:

        ​Request body should contain only movie title, and its presence should be validated.
        Based on passed title, other movie details should be fetched from http://www.omdbapi.com/ (or other similar, public movie database) - and saved to application database.
        Request response should include full movie object, along with all data fetched from external API.
        example:
        {"title":"Edge of Tomorrow"}
        

GET /movies:

        ​Should fetch list of all movies already present in application database.
        Additional filtering, sorting is fully optional - but some implementation is a bonus.

POST /comments:

        ​Request body should contain ID of movie already present in database, and comment text body.
        Comment should be saved to application database and returned in request response.
        example:
        {
        "content": "this is a comment for a movie with the db id = 4",
        "movie_id": 4
        }

GET /comments:

        ​Should fetch list of all comments present in application database.
        Should allow filtering comments by associated movie, by passing its ID.
        (example: /comments?movie_id=10)

GET /top:

        ​Should return top movies already present in the database ranking based on a number of comments added to the movie (as in the example) in the specified date range. The response should include the ID of the movie, position in rank and total number of comments (in the specified date range).
        Movies with the same number of comments should have the same position in the ranking.
        
        Not implemented yet:
        - requires specifying a date range for which statistics should be generated.


