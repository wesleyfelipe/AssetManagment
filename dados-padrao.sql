INSERT INTO users (username, email_addr, desc, role, hash, creation_date, nome, telefone) VALUES ('admin','admin@localhost.local','admin test user','admin','cLzRnzbEwehP6ZzTREh3A4MXJyNo+TV8Hs4//EEbPbiDoo+dmNg22f2RJC282aSwgyWv/O6s3h42qrA6iHx8yfw=','2012-10-28 20:50:26.286723', 'ADMIN','(51) 9999-9999');
INSERT INTO roles (role, level) VALUES ('special', 200);
INSERT INTO roles (role, level) VALUES ('admin', 100);
INSERT INTO roles (role, level) VALUES ('editor', 60);
INSERT INTO roles (role, level) VALUES ('user', 50);