SELECT tr.Name, tr.Composer, tr.Bytes
    FROM Album AS al
    INNER JOIN Track as tr ON al.AlbumId = tr.AlbumId
    WHERE al.Title = "Mezmerize";

SELECT gr.Name, COUNT(*)
    FROM Genre as gr
    INNER JOIN Track as tr ON gr.GenreId = tr.GenreId
    GROUP BY gr.Name;
    
SELECT tr.*
    FROM InvoiceLine as inv
    INNER JOIN Track as tr ON inv.TrackId = tr.TrackId
    WHERE inv.InvoiceId = 40;

SELECT tr.*
    FROM Invoice as inv
    INNER JOIN Customer as cu ON inv.CustomerId = cu.CustomerId
    INNER JOIN InvoiceLine as invl ON invl.InvoiceId = inv.InvoiceId
    INNER JOIN Track as tr ON invl.TrackId = tr.TrackId
    WHERE cu.FirstName = "Marc" AND cu.LastName = "Dubois";

SELECT SUM(invl.UnitPrice)
    FROM Invoice as inv
    INNER JOIN Customer as cu ON inv.CustomerId = cu.CustomerId
    INNER JOIN InvoiceLine as invl ON invl.InvoiceId = inv.InvoiceId
    WHERE cu.FirstName = "Marc" AND cu.LastName = "Dubois";

SELECT cu.FirstName, cu.LastName, SUM(invl.UnitPrice) as "Montant dépensé"
    FROM Invoice as inv
    INNER JOIN Customer as cu ON inv.CustomerId = cu.CustomerId
    INNER JOIN InvoiceLine as invl ON invl.InvoiceId = inv.InvoiceId
    GROUP BY cu.FirstName
    ORDER BY SUM(invl.UnitPrice) DESC
/* Celui qui a dépensé le plus est Frank Harris (81.239)*/

SELECT tr.*
    FROM Playlist as pl 
    INNER JOIN PlaylistTrack as plt ON plt.PlaylistId = pl.PlaylistId
    INNER JOIN Track as tr ON tr.TrackId = plt.TrackId
    WHERE pl.Name = "Classical"