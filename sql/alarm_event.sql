create table alarm_event(
	event_id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(25) NOT NULL,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    state VARCHAR(3)
);