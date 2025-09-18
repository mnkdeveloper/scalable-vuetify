CREATE TABLE user (    id int NOT NULL,    usernam varchar(255) NOT NULL,    email varchar(255) NOT NULL,    PRIMARY KEY (ID),    UNIQUE (username),    UNIQUE (email));

INSERT INTO user (id, username, email) values (1, 'naresh', 'naresh@gmail.com');



INSERT INTO user (id, username, email) values (2, 'kumar', 'kumar@gmail.com');
