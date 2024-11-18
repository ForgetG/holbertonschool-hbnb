from sqlalchemy import create_engine, text

# Create an engine
engine = create_engine('sqlite:///development.db')  # Use your actual database URI

# Function to execute SQL scripts from files
def execute_sql_from_file(file_name):
    with open(file_name, 'r') as file:
        sql_script = file.read()

    # Split the script into individual statements (assuming each statement ends with a semicolon)
    statements = sql_script.split(';')

    # Execute each statement separately
    with engine.begin() as connection:
        for statement in statements:
            if statement.strip():  # Avoid empty statements
                connection.execute(text(statement.strip()))

# Execute SQL files
execute_sql_from_file('user_table.sql')
execute_sql_from_file('place_table.sql')
execute_sql_from_file('amenity_table.sql')
execute_sql_from_file('review_table.sql')
execute_sql_from_file('place_amenity_table.sql')
