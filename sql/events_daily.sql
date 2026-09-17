select
    date(event_time)                                                            as dt,
    count(distinct user_id)                                                     as dau,
    count(distinct user_session)                                                as sessions,
    count(distinct case when event_type = 'view'     then user_id end)          as users_view,
    count(distinct case when event_type = 'cart'     then user_id end)          as users_cart,
    count(distinct case when event_type = 'purchase' then user_id end)          as users_purchase,
    count(distinct case when event_type = 'purchase' then user_session end)     as sessions_purchase,
    sum(case when event_type = 'purchase' then price end)                       as gmv
from sandbox.events_201911
group by 1
order by 1
