CREATE TABLE IF NOT EXISTS db1.weather_hourly
(
	city varchar,
    temp_c decimal32(3),
    wind_speed_kph decimal32(3),
    wind_direction varchar,
    chance_of_rain Int32,
    chance_of_snow Int32,
    precipitation_mm decimal32(3),
    time datetime
)
ENGINE = ReplacingMergeTree
ORDER BY (city, time);

CREATE TABLE IF NOT EXISTS db1.weather_daily
(
	city varchar,
    min_temp_c decimal32(3),
    max_temp_c decimal32(3),
    avg_temp_c decimal32(3),
    precipitation_mm decimal32(3),
    date date
)
ENGINE = ReplacingMergeTree
ORDER BY (city, date);

CREATE TABLE IF NOT EXISTS db1.alerts
(
	city varchar,
    headline varchar,
    message varchar,
    category varchar,
    instruction varchar,
    date date
)
ENGINE = ReplacingMergeTree
ORDER BY (city, date);