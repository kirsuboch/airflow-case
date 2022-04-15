CREATE TABLE IF NOT EXISTS out_table (
    pair VARCHAR,
    ratedate DATE,
    rate DECIMAL(20, 5),
    primary key(pair, ratedate)
);