CREATE DATABASE tasks;

-- switch connection to a new database
\c tasks;

CREATE TABLE users(
    id bigserial NOT NULL,
    name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    username varchar(100) NOT NULL UNIQUE,
    email varchar(150) NOT NULL UNIQUE,
    password varchar(50) NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE taks (
    id bigserial NOT NULL,
    user_id bigint NOT NULL,
    title VARCHAR(150) NOT NULL,
    description VARCHAR(250) NOT NULL,
    due_date Date  NOT NULL,
    status varchar(100) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(user_id) REFERENCES users(id)
);


INSERT INTO users (id, name, last_name, username, email, password) VALUES (1, 'Javier', 'Amaya','javieramayapat', 'javieramayapat@gmail.com', 'easypassword');


INSERT INTO taks (user_id, title, description, due_date, status)
VALUES (1, 'Finish report', 'Complete the report on project progress', '2023-04-05', 'in progress');

INSERT INTO taks (user_id, title, description, due_date, status)
VALUES (1, 'Buy groceries', 'Pick up milk, eggs, bread, and vegetables', '2023-04-01', 'completed');

INSERT INTO taks (user_id, title, description, due_date, status)
VALUES (1, 'Call client', 'Schedule a meeting with the new client', '2023-04-08', 'pending');

INSERT INTO taks (user_id, title, description, due_date, status)
VALUES (1, 'Prepare presentation', 'Create slides for upcoming presentation', '2023-04-12', 'required');

INSERT INTO taks (user_id, title, description, due_date, status)
VALUES (1, 'Submit timesheet', 'Complete and submit weekly timesheet', '2023-04-02', 'completed');
