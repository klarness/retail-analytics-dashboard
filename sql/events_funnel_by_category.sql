select
    split_part(category_code, '.', 1)                                   as category_l1,
    count(distinct case when event_type = 'view'     then user_id end)  as users_view,
    count(distinct case when event_type = 'cart'     then user_id end)  as users_cart,
    count(distinct case when event_type = 'purchase' then user_id end)  as users_purchase
from sandbox.events_201911
where category_code is not null and category_code <> ''
group by 1
order by users_view desc
