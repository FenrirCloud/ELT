
with source as (
    select
        id as order_id,
        order_status,
        order_purchase_timestamp,
        order_aproved_at as order_approved_at,
        order_delivered_customer_date,
        order_estimated_delivery_date
    from olist_classified_public_dataset
)

select * from source