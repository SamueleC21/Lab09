from database.DB_connect import DBConnect
from model.Connessione import Connessione
from model.aeroporto import Aeroporto


class DAO():

    @staticmethod
    def getAeroporti():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)

        res = []
        query = """select *
                    from airports a  """

        cursor.execute(query)

        for row in cursor:
            res.append(Aeroporto(**row))

        cursor.close()
        conn.close()
        return res


    @staticmethod
    def getEdge():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)

        res = []
        query = """select ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID, COUNT(*) AS numVoli, sum(DISTANCE) as sommaKm
                    from flights f
                    group by ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID """

        cursor.execute(query)

        for row in cursor:
            res.append(Connessione(**row))
            #res.append(ArtObject(object_id=row["object_id"], ...))

        cursor.close()
        conn.close()
        return res