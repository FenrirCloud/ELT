
with orders as (
    select * from {{ ref('stg_orders') }}
),

customers as (
    select * from {{ ref('stg_customers') }}
),

order_items as (
    select * from {{ ref('stg_order_items') }}
),

-- Final fact table joining the staging tables
final as (
    select
        o.order_id,
    
        c.customer_city,
        c.customer_state,
        
        o.order_status,
        o.order_purchase_timestamp,
        o.order_approved_at,
        o.order_delivered_customer_date,
        o.order_estimated_delivery_date,
        
        oi.order_items_qty,
        oi.price,
        oi.freight_value,
        
        (oi.price + oi.freight_value) as total_value
        
    from orders o
    left join customers c on o.order_id = c.customer_id 
    left join order_items oi on o.order_id = oi.order_id
)

select * from final