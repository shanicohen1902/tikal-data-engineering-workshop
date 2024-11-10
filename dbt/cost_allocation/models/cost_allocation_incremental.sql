{{ config(
    materialized='incremental',
    unique_key=['service_id', 'date']
) }}

WITH usage_data AS (
    SELECT
        client,
        service_name,
        service_id,
        date,
        total_used,
        resource_type
    FROM {{ ref('service_usage') }}  -- Reference to the usage seed table
),

service_costs AS (
    SELECT
        service_name,
        cost_per_unit,
        measure_unit,
        resource_type,
        currency
    FROM {{ ref('service_costs') }}  -- Reference to the service costs seed table
)

SELECT
    u.client,
    u.service_name,
    u.service_id,
    u.date,
    u.total_used,
    u.resource_type,
    s.cost_per_unit,
    (u.total_used * s.cost_per_unit) AS total_cost,
    s.currency,
    {{ upper_case('u.service_name') }} AS upper_case_namr
FROM usage_data u
JOIN service_costs s ON u.service_name = s.service_name

{% if is_incremental() %}
WHERE u.date > (SELECT MAX(date) FROM {{ this }})  -- Only select new records based on the date
{% endif %}