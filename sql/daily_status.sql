create table daily_status(
	daily_status_id INT AUTO_INCREMENT PRIMARY KEY,
    created_date DATE NOT NULL,
    allowed_devices INT,
    blocked_devices INT,
    unknown_devices INT,
    total_events INT,
    common_event VARCHAR(10),
    total_faults INT,
    common_fault INT
);