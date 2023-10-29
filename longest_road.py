#!/usr/bin/python3

try:
    import cgi
    import cgitb
    import sqlite3 

    cgitb.enable()  # Enable CGI error reporting

    # Set the content type to HTML
    print("Content-type: text/html\n")

    # Parse the form data
    form = cgi.FieldStorage()
    limit = form.getvalue("limit")

    # Connect to the database (SQLite in this example)
    connection = sqlite3.connect("canvec_231027_433481.gpkg")
    cursor = connection.cursor()

    # SELECT * FROM road_segment_1
    # WHERE ST_Intersects(geom, ST_MakeEnvelope(x_min, y_min, x_max, y_max, srid));

    # SELECT *
    # FROM road_segment_1
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
    # FROM road_segment_1;



    # Execute the SQL query and fetch results
    cursor.execute(f"SELECT * FROM road_segment_1 ORDER BY ST_Length(geom) DESC LIMIT {limit};")
    results = cursor.fetchall()

    # Close the database connection
    connection.close()

    # Generate an HTML response
    print("<html>")
    print("<head><title>SQL Query Results</title></head>")
    print("<body>")
    print("<h1>SQL Query Results</h1>")
    print("<p>SQL Query: {}</p>".format(f"SELECT * FROM road_segment_1 ORDER BY ST_Length(geom) DESC LIMIT {limit};"))
    print("<p>Longest Road Segment: </p>")
    print("<table>")
    for row in results:
        print("<tr>")
        for value in row:
            print("<td>{}</td>".format(value))
        print("</tr>")
    print("</table>")
    print("</body>")
    print("</html>")
    # hydro_obstacle_0
    # road_segment_1
    # waterbody_2
except Exception as e:
    # Log the error to a file or to stdout
    print("Content-type: text/html\n")
    print(f"Error: {str(e)}")