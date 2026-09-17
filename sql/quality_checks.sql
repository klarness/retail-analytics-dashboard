select
    count(*)                                                        as rows_total,
    count(distinct o.order_id)                                      as orders_unique,
    min(o.date_created)                                             as first_created,
    max(o.date_created)                                             as last_created,
    min(o.date_paid)                                                as first_paid,
    max(o.date_paid)                                                as last_paid,
    sum(case when o.date_paid is null then 1 else 0 end)            as rows_not_paid,
    sum(case when o.date_paid < o.date_created then 1 else 0 end)   as rows_paid_before_created,
    sum(case when od.price <= 0 then 1 else 0 end)                  as rows_bad_price,
    sum(case when od.quantity <= 0 then 1 else 0 end)               as rows_bad_quantity,
    sum(case when od.commission < 0 or od.commission > 1 then 1 else 0 end) as rows_bad_commission
from sandbox.orders o
join sandbox.order_details od on o.order_id = od.order_id
