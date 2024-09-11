{{ config(materialized='table') }}

with source_data as (

SELECT
  c.client,
  c.service_name,
  c.service_id,
  c.date,
  c.total_used,
  c.resource_type,
  s.cost_per_unit,
  c.total_used * s.cost_per_unit AS total_cost
FROM {{ ref('usage') }} c
JOIN {{ ref('service_costs') }} s ON c.service_name = s.service_name

)

select *
from source_data
