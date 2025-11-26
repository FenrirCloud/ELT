
with source as (
    select
        id as order_id, 
        order_items_qty,
        order_products_value as price,
        order_freight_value as freight_value
    from olist_classified_public_dataset
)

select * from source