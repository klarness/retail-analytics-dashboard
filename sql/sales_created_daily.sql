select
    date(o.date_created)                as dt,
    sum(od.price * od.quantity)         as gmv_created,
    count(distinct o.order_id)          as orders_created,
    count(distinct o.customer_id)       as customers_created,
    count(distinct od.seller_id)        as sellers_created
from sandbox.orders o
join sandbox.order_details od on o.order_id = od.order_id
where o.date_created is not null
group by 1
order by 1
