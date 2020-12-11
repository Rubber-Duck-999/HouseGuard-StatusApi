create table status(
	status_id INT AUTO_INCREMENT PRIMARY KEY,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    motion_detected TIMESTAMP,
    access_granted TIMESTAMP,
    access_denied TIMESTAMP,
    last_fault VARCHAR(50),
    last_user VARCHAR(10),
    cpu_temp INT,
    cpu_usage INT,
    memory INT
);