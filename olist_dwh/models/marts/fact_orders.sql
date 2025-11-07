with orders as (
    select * from {{ ref('stg_orders') }}
),
order_items as (
    select * from {{ ref('stg_order_items') }}
)

select
    -- Khóa chính & Khóa ngoại để nối với các bảng Dim
    o.order_id,
    oi.order_item_id,
    o.customer_id,
    oi.product_id,
    oi.seller_id,

    -- Timestamps (Thời gian)
    o.purchase_at,
    o.approved_at,
    o.delivered_to_customer_at,
    o.estimated_delivery_at,

    -- Metrics (Số liệu để tính toán)
    oi.price,
    oi.freight_value,
    (oi.price + oi.freight_value) as total_order_value,

    -- Status
    o.order_status

from orders o
join order_items oi on o.order_id = oi.order_id