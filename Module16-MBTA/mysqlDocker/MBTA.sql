CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    id varchar(255) not null,
    latitude decimal(11,8) not null,
    longitude decimal(11,8) not null,
    direction int not null,
    current_status varchar(255) null,
    label varchar(255) not null,
    occupancy_status varchar(255) null,
    speed int null,
    updated_at varchar(255) not null,
    current_stop_sequence int not null
);

