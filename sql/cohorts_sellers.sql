with first_activity as (
    select
        od.seller_id,
        date(date_trunc('month', min(o.{date_col}))) as cohort_month
    from sandbox.orders o
    join sandbox.order_details od on o.order_id = od.order_id
    where o.{date_col} is not null
    group by od.seller_id
)
select
    f.cohort_month,
    date(date_trunc('month', o.{date_col}))             as activity_month,
    count(distinct od.seller_id)                        as sellers,
    sum(od.price * od.quantity)                         as gmv,
    sum(od.price * od.quantity * od.commission)         as margin
from sandbox.orders o
join sandbox.order_details od on o.order_id = od.order_id
join first_activity f on od.seller_id = f.seller_id
where o.{date_col} is not null
group by 1, 2
order by 1, 2
