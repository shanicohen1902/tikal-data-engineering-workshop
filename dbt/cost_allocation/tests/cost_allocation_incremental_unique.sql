select
    service_id,
    date,
    count(*)
from {{ ref('cost_allocation_incremental') }}
group by service_id, date
having count(*) > 1