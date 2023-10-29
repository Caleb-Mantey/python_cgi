#!/usr/bin/python3

import cgi
import cgitb
import sqlite3  

try: 
    cgitb.enable()  # Enable CGI error reporting

    # Set the content type to HTML
    print("Content-type: text/html\n")

    # Parse the form data
    form = cgi.FieldStorage()
    sql_query = form.getvalue("sql_query")

    # Connect to the database (SQLite in this example)
    connection = sqlite3.connect("canvec_231027_433481.gpkg")
    cursor = connection.cursor()

    # SELECT * FROM road_segments
    # WHERE ST_Intersects(geom, ST_MakeEnvelope(x_min, y_min, x_max, y_max, srid));

    # SELECT *
    # FROM road_segments
    # ORDER BY ST_Length(geom) DESC
    # LIMIT 1;

    # SELECT * FROM waterbodies
    # WHERE ST_Intersects(geom, ST_MakeEnvelope(x_min, y_min, x_max, y_max, srid));

    # SELECT COUNT(*) FROM road_junctions;

    # SELECT *
    # FROM road_junctions
    # ORDER BY ST_Distance(geom, ST_MakePoint(x, y))
    # LIMIT 1;

    # SELECT SUM(ST_Length(geom))
    # FROM road_segments;



    # Execute the SQL query and fetch results
    cursor.execute(sql_query)
    results = cursor.fetchall()

    # Close the database connection
    connection.close()

    # Generate an HTML response
    print("<html>")
    print("<head><title>SQL Query Results</title></head>")
    print("<body>")
    print("<h1>SQL Query Results</h1>")
    print("<p>SQL Query: {}</p>".format(sql_query))
    print("<table>")
    for row in results:
        print("<tr>")
        for value in row:
            print("<td>{}</td>".format(value))
        print("</tr>")
    print("</table>")
    print("</body>")
    print("</html>")
except Exception as e:
    # Log the error to a file or to stdout
    print("Content-type: text/html\n")
    print(f"Error: {str(e)}")