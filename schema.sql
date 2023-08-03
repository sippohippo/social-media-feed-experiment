CREATE TABLE users (
id SERIAL PRIMARY KEY, 
email TEXT UNIQUE, 
password TEXT, 
admin BOOLEAN,
acceptTerms BOOLEAN
);

CREATE TABLE images (
id SERIAL PRIMARY KEY,
name TEXT,
generated BOOLEAN,
data BYTEA
);

CREATE TABLE real_posts (
id SERIAL PRIMARY KEY,
name TEXT,
handle TEXT,
content TEXT,
profilePicId INT REFERENCES images(id),
type TEXT
);

CREATE TABLE fake_posts (
id SERIAL PRIMARY KEY,
content TEXT
);

CREATE TABLE fake_profiles (
id SERIAL PRIMARY KEY,
name TEXT UNIQUE,
handle TEXT,
profilePicId INT REFERENCES images(id),
type TEXT
);