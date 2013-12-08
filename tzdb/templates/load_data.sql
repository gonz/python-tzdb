BEGIN;

TRUNCATE tz_version;
INSERT INTO tz_version VALUES ('${date_version}');

TRUNCATE tz_zone;
COPY tz_zone("id", "country_code", "name") FROM '${dumps_dir}/zone.csv' WITH DELIMITER ',' CSV;

TRUNCATE tz_timezone;
COPY tz_timezone("zone_id", "abbreviation", "time_start", "gmt_offset", "dst") FROM '${dumps_dir}/timezone.csv' WITH DELIMITER ',' CSV;

TRUNCATE tz_country;
COPY tz_country("code", "name") FROM '${dumps_dir}/country.csv' WITH DELIMITER ',' CSV;

COMMIT;
