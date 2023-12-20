import pandas as pd

"""
--PROBLEM DETAILS--

185. Department Top Three Salaries

A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

Write a solution to find the employees who are high earners in each of the departments.

Return the result table in any order.

Example:


Input: 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output: 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Joe      | 85000  |
| IT         | Randy    | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+
Explanation: 
In the IT department:
- Max earns the highest unique salary
- Both Randy and Joe earn the second-highest unique salary
- Will earns the third-highest unique salary

In the Sales department:
- Henry earns the highest salary
- Sam earns the second-highest salary
- There is no third-highest salary as there are only two employees


Acceptance rate: 51.4%
Difficulty: Hard

--SUBMISSION DETAILS--

Status: Accepted
Language: Python
Runtime: 992ms (Beats 5.5%)
Memory: 61.6MB (Beats 88.33%)

Values correct as of: 06/12/2023

"""


def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    """ Using pandas gets the top 3 unique salaries for each department 

    Args:
        employee (pd.DataFrame): A table of employee data
        department (pd.DataFrame): A table of department data

    Returns:
        pd.DataFrame: _description_
    """
    # splits up the employee table into a table for each department and sorts each table based on the salary of the employees
    department_split = [employee.loc[employee["departmentId"] == i].sort_values("salary", ascending=False) for i in department["id"].tolist()]
    
    # gets the salary of the 3rd unique highest earner for each of the departments
    threshold_salary = [i.drop_duplicates(keep="first", subset=["salary"]).head(3).iloc[-1]["salary"].item() if len(i.index) != 0 else 0 for i in department_split]

    # gets the employees that are within the top three unique salaries for each department
    department_split = [i.loc[i["salary"] >= threshold_salary[counter]] for counter, i in enumerate(department_split)]

    # if no data given then return empty table
    if department_split == []:
        return pd.DataFrame({
            "Department": [],
            "Employee": [],
            "Salary": []
        })
        
    # combine the seporate department tables together
    result = pd.concat(department_split)

    # select the required information 
    result = result[["departmentId", "name", "salary"]]

    # convert the department id to the name of the department from the department table
    result["departmentId"] = result["departmentId"].apply(lambda x: department.loc[department["id"] == x]["name"].item())
    
    # rename the colun names according to problem definition 
    result = result.rename(columns={
        "departmentId": "Department",
        "name": "Employee",
        "salary": "Salary"
    })

    return result
