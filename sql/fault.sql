create table fault(
    fault_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);