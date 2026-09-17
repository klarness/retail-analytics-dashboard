select
    date(o.date_paid)                                   as dt,
    sum(od.price * od.quantity)                         as gmv_paid,
    sum(od.price * od.quantity * od.commission)         as margin_paid,
    count(distinct o.order_id)                          as orders_paid,
    count(distinct o.customer_id)                       as customers_paid
from sandbox.orders o
join sandbox.order_details od on o.order_id = od.order_id
where o.date_paid is not null
group by 1
order by 1
