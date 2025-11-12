{{ config(materialized='view') }}

WITH source AS (
    SELECT
        *
    FROM {{ref("orders_items")}}
),

renamed AS (
    SELECT
        order_id,
        product_id,
        CAST(quantity AS NUMERIC) AS quantity
    FROM
        source
)

SELECT
    *
FROM
    renamed