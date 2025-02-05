
> This is an adapted version of our dedicated FE test @ https://github.com/dataiku/census-challenge

 # Legendary legacy

The best code runs forever, right? So did our great little Census app. It was written in NodeJS as an internal API but now we want to ship it to users that aren't developers.

## The app
You will find a NodeJS server app in `/resources/census-server-dataiku`

The server runs against a SQLite database containing demographical record data that does not exist, yet. Install the dependencies and `create_db.py` to generate your data (make sure to put in the right path after you create it). 

The Node app provides an example REST API with 2 endpoints. 

- `GET /api/columns` returns the list of all columns
- `GET /api/data/<columnName>` returns the list of all unique values found in the database for the column named <columnName>, and for each value its count and the average of the age.

Example: `GET /api/data/marital%20status` returns (with our own randomly generate data):

```sh
{
  "values": [
    {
      "id": "Widowed",
      "count": 200692,
      "average": 53
    },
    {
      "id": "Separated",
      "count": 199952,
      "average": 53
    },
    {
      "id": "Never married",
      "count": 199940,
      "average": 53
    },
    {
      "id": "Divorced",
      "count": 199873,
      "average": 53
    },
    {
      "id": "Married",
      "count": 199544,
      "average": 53
    }
  ],
  "count": 5
}

```

This means that the database contains 5 different unique values in the `marital status` column, with for instance 199952 people that have the marital status `Separated` and are `53` years old on average. 

# Your challenge
Your goal is to create a small web application front-end to intuitively interact with the data in the underlying database. It is also time to harmonize the Census app with our current stack. You can re-create the existing data model but we want to swap the back-end for a modern Python API (you can use a framework). If you need or want additional endpoints, you can add them.

## Desired behavior and constraints
The application should allow the user to select a column from the database. It should then display -as a datatable- for each value of the variable, the count of rows with this value and the average or uniques of that value if it is a categorical. There are some constraints and stakeholder demands:

- Your database should contain a few million rows
- The values should be sorted by decreasing count as default.
- It should also display next to the table, one (or 2) charts displaying the same data that changes if the selection in the table changes. 
- Make sure to add some summary statistics about the underlying data next to graphs, like # points and averages.
- Your application should be a SPA, and try to make the behavior as intuitive as you can.

Also consider this:
- We encourage you to think of ways to properly manage the returned data size and optimize the user experience. 
- It's OK to take shortcuts or make assumptions, but provide clarity on where you did this to help us understand your thinking (eg document what you would consider/add if this were a real production app). 

# Final note
Apart from swapping the API for a Python back-end, there are no constraints on the tech choices you can make. For instance, it is fine to allow yourself a little tailwind by utilising a CSS framework. Choose the tech you feel comfortable in and consider fit for the task, as long as it helps us to understand your level and approach to crafting great user experiences! Deliver this test as an application our average Dataiker can install, test and run locally with your provided documentation. 

And, perhaps most importantly, make sure to have fun!