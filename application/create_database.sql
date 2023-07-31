CREATE TABLE users (
	id SERIAL PRIMARY KEY, 
	email TEXT, 
	password TEXT, 
	admin BOOLEAN,
	acceptTerms BOOLEAN
);
