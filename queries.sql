INSERT INTO app_film (name, release_date, genre, rating) VALUES 
	('Avengers: Infinity War', '2018/04/23', 'ACC', 4),
	('Avengers: End Game', '2019/04/22', 'ACC', 3);

SELECT * FROM app_film ORDER BY name ASC;

SELECT genre, count(*) as films FROM app_film GROUP BY genre;

SELECT name AS "Nombre", length(name) AS "Longitud" FROM app_film ORDER BY "Longitud" ASC;