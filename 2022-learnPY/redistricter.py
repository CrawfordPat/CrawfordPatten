"""Fix election district boundaries in the US."""
# Import modules
import csv
import os
# Redistrict the US
def redistrict(csv_path, state_abbr, state_name):
    """Redistrict the US."""
    # Open the CSV file
    with open(csv_path, 'r') as f:
        # Read the CSV file
        reader = csv.reader(f)
        # Skip the header
        next(reader)
        # Create a dictionary to hold the data
        data = {}
        # Loop through the rows
        for row in reader:
            # Get the district number
            district_number = row[0]
            # Get the district name
            district_name = row[1]
            # Get the district population
            district_population = row[2]
            # Get the district area
            district_area = row[3]
            # Get the district state
            district_state = row[4]
            # Get the district state abbreviation
            district_state_abbr = row[5]
            # Get the district state name
            district_state_name = row[6]
            # Get the district congressional district
            district_congressional_district = row[7]
            # Get the district state legislative district
            district_state_legislative_district = row[8]
            # Get the district judicial district
            district_judicial_district = row[9]
            # Get the district school district
            district_school_district = row[10]
            # Get the district city council district
            district_city_council_district = row[11]
            # Get the district township council district
            district_township_council_district = row[12]
            # Get the district county council district
            district_county_council_district = row[13]
            # Get the district school board district
            district_school_board_district = row[14]
            # Get the district charter township
            district_charter_township = row[15]
            # Get the district charter school district
            district_charter_school_district = row[16]
            # Get the district block group
            district_block_group = row[17]
            # Get the district census block group
            district_census_block_group =

    # Who is your daddy?
    # print(data)

    # Write the data to a CSV file
    with open(os.path.join(os.path.dirname(csv_path), state_abbr + "_redistrict.csv"), 'w') as f:
        