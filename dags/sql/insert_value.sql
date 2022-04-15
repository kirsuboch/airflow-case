INSERT INTO out_table (pair, ratedate, rate)
VALUES (
    '{{ ti.xcom_pull(task_ids="retrieve_rate", key="pair") }}',
    '{{ ti.xcom_pull(task_ids="retrieve_rate", key="curdate") }}',
    '{{ ti.xcom_pull(task_ids="retrieve_rate", key="rate") }}')
ON CONFLICT (pair, ratedate)
DO UPDATE SET rate = '{{ ti.xcom_pull(task_ids="retrieve_rate", key="rate") }}';