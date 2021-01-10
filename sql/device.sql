create table device(
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    allowed_devices INT,
    blocked_devices INT,
    unknown_devices INT
);