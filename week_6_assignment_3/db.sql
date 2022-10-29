SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;

DROP TABLE IF EXISTS nft CASCADE;

CREATE TABLE nft(
    nft_address text,
    nft_info text
);

DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users(
	user_name text,
	user_password text
);

SELECT * FROM nft;

/*
INSERT INTO nft VALUES ('', '');
*/