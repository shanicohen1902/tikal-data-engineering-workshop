# Data Engineering Course Exercises with dbt

## Installation

### setup
```sh
cd cost_allocation
dbt debug
```

## Exercise 1: dbt Seeds
**Objective**: Understand how to use dbt seeds to load CSV data into the dbt project.

### Instructions:
1. Run the command `dbt seed` to load the data into your dbt project.
1. Verify the data is loaded correctly by querying the tables in your database.

Answer the following questions using DuckDB cli:
Which tables created in the db?
How many lines in each table?

### Hint:
- Use the `dbt seed --help` command to understand the options available for seeding data.

---

## Exercise 2: dbt Docs
**Objective**: Generate documentation for your dbt models and seeds.

### Instructions:
1. Create a new model `cost_allocation` in your dbt project that calculates total costs based on the usage and service cost data 
2. Use the `description` property in your model file to document the purpose of the model.
3. Add descriptions for each column in the `usage` and `cost_allocation` tables using the `description` property in the schema file.
4. Run `dbt docs generate` to create the documentation.
5. Open the documentation in your browser using `dbt docs serve` and explore the generated documentation.

### Hint:
- Make sure to include clear and concise descriptions to enhance understanding for future users.

---

## Exercise 3: dbt Materialization Strategies
**Objective**: Learn about different materialization strategies in dbt.

### Instructions:
1. Create a new model ‘cost_allocation_incremental. 
1. join service_costs and service_usage tables by service_name aggregate the data monthly
1. calculate total_cost -  total usage costs  (cost_per_unit * total_used)
1. Make this model to be updated incrementally 
1. Think - how would you test that kind of model?

---

## Exercise 4: Testing
**Objective**: Implement testing in your dbt models to ensure data quality.

### Instructions:
1. Create tests for your models to check for:
   - Non-null values in critical columns (e.g., `client`, `service_name`, `total_used`).
   - Valid values for `resource_type` (e.g., check that it only contains specified types).
   - Logical checks, such as ensuring that `total_used` is greater than zero.
2. Define these tests in the schema file for your models.
3. Run the tests using the command `dbt test` and analyze the results.
4. Fix any issues identified by the tests and re-run them to ensure data quality.

### Hint:
- Use the `dbt test --help` command to explore different testing options available in dbt.

---


## Exercise 5: Jinja and Macros
**Objective**: Utilize Jinja templating and macros to enhance dbt models.

### Instructions:
Create a macro that add ‘upper_case_name’ column with service name in upper case mode
Use this macro in your model to compute total this string
Document your macro and provide examples of how to use it in your models.

### Hint:
- Refer to the [dbt documentation on Jinja](https://docs.getdbt.com/docs/building-a-dbt-project/jinja-macros) for examples of how to create and use macros effectively.

---