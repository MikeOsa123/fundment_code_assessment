
# Fundment Code Assessment

Coding exercise for Fundment answering Questions 1 and 2.

## Investment Account Returns

This project provides an implementation of calculating time-weighted returns for a client's investment account using Pandas DataFrame.

### Installation
This project requires Python 3.6 or higher. The following steps outline how to set up the project:

#### 1. Clone the repository
```
git clone https://github.com/MikeOsa123/fundment_code_assessment.git
cd fundment_code_assessment
 ```

#### 2. Create a virtual environment
```
python3 -m venv venv
```

#### 3. Activate the virtual environment
```
source venv/bin/activate
```

#### 4. Install the dependencies
```
pip install -r requirements.txt
```

#### 5. Run the tests to verify that everything is working
```
pytest
```

### Technologies Used
This project uses the following technologies:

- Python 3.6 or higher: The programming language used to write the code for this project.
- Pandas: A Python library used for data manipulation and analysis.
- Numpy: A Python library used to generate NaN values.
- pytest: A testing framework used to write and run unit tests for the project.

### Requirements
The project meets the following requirements:

Parses a CSV file into a Pandas DataFrame.
Calculates the time-weighted returns for a client's investment account.
Handles edge cases such as zero or negative initial values and cash flows, and accounts with no data.



## Carbon Filter Planner

This program generates a filter plan for a street where some houses already have carbon filters fitted and others do not. The program uses two types of filters named “a” and “b”. These filters work best if no three adjacent houses have the same type of filter. Houses are represented as a string of characters containing a, b and “?”. Where a or b denote the type of filter that is already fitted, and “?” represents a house with no filter.

### Installation
    1. Clone this repository
    2. Install Python (if not already installed)
    3. Install dependencies by running pip install -r requirements.txt in the command line

### Usage
To generate a filter plan, use the filter_plan function in the carbon_filter_planner.py module. The function takes a string representing the current state of the street and returns a string representing the plan of how to fit the new filters.

```
    from filter_plan import filter_plan

    input_str = "a?bb"
    result = filter_plan(input_str)
    print(result)  # output: "aabb"
```
### Technologies Used
This program was written in Python 3.

### Meeting the Requirements
The program meets the requirements by:

- Generating a filter plan for the street based on the current state of each house
- Using two types of filters named "a" and "b"
- Ensuring that no three adjacent houses have the same type of filter
- Handling edge cases where there are no possible solutions or only one house needs a filter
- Using the input string and outputting a string representing the plan of how to fit the new filters.
