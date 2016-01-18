#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2


def connect():
    """Connect to the PostgreSQL database.  :returns: a database connection."""
    return psycopg2.connect("dbname=tournament")


def delete_tournaments():
    db_query("DELETE FROM tournament;")


def start_tournament():
    db_query("Insert INTO tournament DEFAULT VALUES;")


def delete_matches(tour_id):
    """Remove all the match records from the database.

    :param tour_id: the tournament the matches should be deleted from
    """
    db_query("DELETE FROM match_ups where tour_id = {0};".format(tour_id))


def delete_players(tour_id):
    """Remove all the player records from the database.

    :param tour_id: the tournament the players should be deleted from
    """
    db_query("DELETE FROM players where tour_id = {0};".format(tour_id))


def count_players(tour_id):
    """:returns: the number of players currently registered.

    :param tour_id: the tournament the players should be counted from
    """
    count = data_pull("SELECT count(*) as num FROM players where tour_id = "
                      "{0};".format(tour_id))
    return count[0][0]


def register_player(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    :param name: the player's full name (need not be unique).
    """
    query = "INSERT INTO players (name) VALUES ('{0}');".format(name)
    db_query(query)


def player_standings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player
    tied for first place if there is currently a tie.

    :returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    standings = data_pull("SELECT players.id, players.name, "
                          "player_stats.wins, player_stats.matches from "
                          "players, player_stats order by player_stats.wins, "
                          "player_stats.o_points, player_stats.draws")
    return standings


def report_match(winner, loser):
    """Records the outcome of a single match between two players.

    :param winner:  the id number of the player who won
    :param loser:  the id number of the player who lost
    """


def swiss_pairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    :returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


def db_query(query):
    """Function for querying the database

    Connects to db, selects cursor, passes query to db, commits, and closes
    the connection.

    :param query: A string to be passed as a query to the database
    """
    conn = connect()
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()


def data_pull(query):
    conn = connect()
    c = conn.cursor()
    c.execute(query)
    data = c.fetchall()
    conn.close()
    return data
