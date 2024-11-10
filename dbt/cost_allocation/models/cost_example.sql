{{ config(materialized='table') }}

with source_data as (

SELECT
  c.client,
  c.service_name,
  c.service_id,
  c.date,
  c.total_used,
  c.resource_type,
FROM {{ ref('service_usage') }} c
)

select *
from source_data
