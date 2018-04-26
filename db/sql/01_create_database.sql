CREATE DATABASE "industry_price_quote"
    WITH
    OWNER = industry_user
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

grant all privileges on database "industry_price_quote" to industry_user;