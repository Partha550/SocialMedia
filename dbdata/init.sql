
-- init.sql
DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database
      WHERE datname = 'social'
   ) THEN
      CREATE DATABASE social;
   END IF;
END
$$;

DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_user
      WHERE usename = 'parthasamanta'
   ) THEN
      CREATE USER myuser WITH ENCRYPTED PASSWORD '12908';
   END IF;
END
$$;

GRANT ALL PRIVILEGES ON DATABASE social TO parthasamanta;
