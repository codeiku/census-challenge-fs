import sqlite3
from tqdm import tqdm
from faker import Faker
import random

"""
Census Database Generator
------------------------

This script generates a synthetic US census database with a configurable number of rows inspired by https://data2.nhgis.org/main.
It creates realistic-looking demographic data including age, employment, education, marital status, and other census-typical fields. 
It does not aim for anything else but to recreate a similar dataset, nor does it account for valid distributions in the data. 

Usage:
   python create_db.py  # Creates us-census.db with 1000001 rows by default
   
   # Or from another script:
   from create_db import create_census_database
   create_census_database(5000)  # Creates db with 5000 rows

Dependencies:
   - sqlite3
   - faker
   - random

Many thanks to Claude for your help.
"""


def create_census_database(num_rows, output_file="us-census.db"):
    # Initialize Faker
    fake = Faker()

    # Connect to SQLite database
    conn = sqlite3.connect(output_file)
    cursor = conn.cursor()

    # Create table with correct schema
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS census_learn_sql (
        age INTEGER,
        "class of worker" TEXT,
        industry TEXT,
        occupation TEXT,
        education TEXT,
        "wage per hour" INTEGER,
        "marital status" TEXT,
        "major industry code" TEXT,
        "major occupation code" TEXT,
        race TEXT,
        "hispanic origin" TEXT,
        sex TEXT,
        "member of a labor union" TEXT,
        "reason for unemployment" TEXT,
        "full or part time employment stat" TEXT,
        "capital gains" INTEGER,
        "capital losses" INTEGER,
        "dividends from stocks" INTEGER,
        "tax filer status" TEXT,
        "region of previous residence" TEXT,
        "state of previous residence" TEXT,
        "detailed household summary in household" TEXT,
        "migration code-change in msa" TEXT,
        "migration code-change in reg" TEXT,
        "migration code-move within reg" TEXT,
        "live in this house 1 year ago" TEXT,
        "migration prev res in sunbelt" TEXT,
        "family members under 18" TEXT,
        "country of birth father" TEXT,
        "country of birth mother" TEXT,
        "country of birth self" TEXT,
        citizenship TEXT,
        "own business or self employed" TEXT,
        "veterans benefits" INTEGER,
        "weeks worked in year" INTEGER
    )
    """)

    # Define possible values for categorical fields
    class_workers = [
        "Private",
        "Self-employed-not incorporated",
        "Local government",
        "State government",
        "Federal government",
        "Never worked",
    ]
    industries = [
        "Construction",
        "Education",
        "Finance",
        "Healthcare",
        "Manufacturing",
        "Retail",
        "Technology",
        "Transportation",
    ]
    occupations = [
        "Manager",
        "Professional",
        "Service",
        "Sales",
        "Administrative",
        "Production",
        "Transportation",
    ]
    education_levels = [
        "Less than high school",
        "High school",
        "Some college",
        "Bachelor's degree",
        "Master's degree",
        "Doctorate",
    ]
    marital_statuses = ["Never married", "Married", "Divorced", "Widowed", "Separated"]
    races = ["White", "Black", "Asian or Pacific Islander", "American Indian", "Other"]
    hispanic_origins = [
        "All other",
        "Mexican-American",
        "Mexican",
        "Puerto Rican",
        "Cuban",
        "Central or South American",
        "Other Spanish",
    ]

    # Generate data
    data = []
    for _ in tqdm(range(num_rows)):
        row = (
            random.randint(16, 90),  # age
            random.choice(class_workers),
            random.choice(industries),
            random.choice(occupations),
            random.choice(education_levels),
            random.randint(0, 100),  # wage per hour
            random.choice(marital_statuses),
            str(random.randint(1, 9)),  # major industry code
            str(random.randint(1, 9)),  # major occupation code
            random.choice(races),
            random.choice(hispanic_origins),
            random.choice(["Male", "Female"]),
            random.choice(["Yes", "No"]),  # union member
            random.choice(["Job leaver", "Job loser", "New entry", "Re-entry", ""]),
            random.choice(["Full-time schedules", "Part-time schedules", ""]),
            random.randint(0, 100000),  # capital gains
            random.randint(0, 10000),  # capital losses
            random.randint(0, 50000),  # dividends
            random.choice(["Single", "Joint", "Head of household"]),
            random.choice(["Northeast", "Midwest", "South", "West", ""]),
            fake.state_abbr(),
            random.choice(
                ["Householder", "Spouse", "Child", "Other relative", "Non-relative"]
            ),
            random.choice(["Yes", "No", ""]),  # migration msa
            random.choice(["Yes", "No", ""]),  # migration reg
            random.choice(["Yes", "No", ""]),  # move within reg
            random.choice(["Yes", "No"]),
            random.choice(["Yes", "No", ""]),
            str(random.randint(0, 5)),
            fake.country(),
            fake.country(),
            fake.country(),
            random.choice(["Native", "Naturalized", "Not citizen"]),
            random.choice(["Yes", "No"]),
            random.randint(0, 10000),  # veterans benefits
            random.randint(0, 52),  # weeks worked
        )
        data.append(row)

    # Insert data
    cursor.executemany(
        """
    INSERT INTO census_learn_sql VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    )
    """,
        data,
    )

    # Commit and close
    conn.commit()
    conn.close()

    print(f"Created database '{output_file}' with {num_rows} rows")


if __name__ == "__main__":
    # Create database with 1000001 rows
    create_census_database(1000001)
