create table hardware(
	hardware_id INT AUTO_INCREMENT PRIMARY KEY,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cpu_temp INT,
    cpu_usage INT,
    memory INT
);