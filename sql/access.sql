create table access(
	access_id INT AUTO_INCREMENT PRIMARY KEY,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    access_granted TIMESTAMP,
    access_denied TIMESTAMP,
    last_user VARCHAR(10)
);