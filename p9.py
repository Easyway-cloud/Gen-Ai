# Install before running
# pip install pydantic

from pydantic import BaseModel

# Create structure
class Institution(BaseModel):

    founder: str

    founded_year: str

    branches: str

    employees: str

    summary: str

# Function to get details
def details(name):

    data = {

        "founder":
        "Rajya Vokkaligara Sangha",

        "founded_year":
        "1979",

        "branches":
        "Single campus in Bangalore",

        "employees":
        "Not Available",

        "summary":
        "Bangalore Institute of Technology is a reputed engineering college in Bangalore."
    }

    return Institution(**data)

# Institution name
name = "Bangalore Institute of Technology"

# Get result
result = details(name)

# Print output
print("Institution Name:",
      name)

print("Founder:",
      result.founder)

print("Founded Year:",
      result.founded_year)

print("Branches:",
      result.branches)

print("Employees:",
      result.employees)

print("Summary:",
      result.summary)