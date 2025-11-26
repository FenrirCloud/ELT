
with source as (
    select
        id as customer_id, 
        customer_zip_code_prefix,
        customer_city,
        customer_state
    from olist_classified_public_dataset
)

select * from source