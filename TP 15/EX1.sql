SELECT * FROM Releves WHERE Date >= "2008-02-01" AND Date <= "2008-02-17";
SELECT AVG(Temperature) FROM Releves;
SELECT AVG(Temperature) FROM Releves WHERE Date >= "2014-10-01" AND Date <= "2014-10-31";
SELECT Temps, 
    AVG(Temperature) AS `Température Moyenne` 
    FROM Releves 
    GROUP BY Temps;
SELECT Temps, 
    AVG(Temperature) AS `Température Moyenne`,
    AVG(Pression) AS `Pression Moyenne`
    FROM Releves 
    GROUP BY Temps;
SELECT  Jour,
        Date,
        Heure,
        MAX(Temperature)
    FROM Releves;
SELECT  Jour,
        Date,
        Heure,
        MIN(Temperature)
    FROM Releves
    WHERE Date >= "2013-01-01" AND Date <= "2013-12-31";
SELECT Secteur_vent AS `Direction du vent`, SUM(Vitesse_vent)/COUNT(*) AS `Vitesse moyenne du vent`
    FROM Releves
    GROUP BY Secteur_vent
    ORDER BY Secteur_vent;
SELECT COUNT(*) FROM Releves;
SELECT COUNT(DISTINCT Temps) FROM Releves;
SELECT Temps, COUNT(*) FROM Releves GROUP BY Temps;
SELECT Temps, COUNT(*) FROM Releves GROUP BY Temps ORDER BY COUNT(*) DESC
SELECT Jour, AVG(Temperature)
    FROM Releves
    WHERE Date >= "2010-01-01" AND Date <="2010-12-31"
    GROUP BY Jour 
    ORDER BY AVG(Temperature) DESC