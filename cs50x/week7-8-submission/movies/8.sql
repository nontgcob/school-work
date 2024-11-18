--list the names of all people who starred in Toy Story
SELECT name FROM people
JOIN stars ON stars.person_id = people.id
JOIN movies ON stars.movie_id = movies.id
WHERE movies.title LIKE "%toy story%";