CREATE TABLE operating_systems (
    id VARCHAR(100) PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    release VARCHAR(255) NOT NULL,
    architecture VARCHAR(255) NOT NULL,
    version VARCHAR(255) NOT NULL,
    processor VARCHAR(255) NOT NULL,
    physical_cores INT NOT NULL,
    logical_cores INT NOT NULL,
    total_ram BIGINT NOT NULL,
    total_swapspace BIGINT NOT NULL
);

CREATE TABLE cpu_metrics (
    id SERIAL PRIMARY KEY NOT NULL,
    producer_id VARCHAR(100) NOT NULL,
    date_time TIMESTAMP NOT NULL,
    operating_system VARCHAR(100) REFERENCES operating_systems(id),
    core INT NOT NULL,
    load_percentage FLOAT NOT NULL
);

CREATE TABLE memory_metrics (
    id SERIAL PRIMARY KEY NOT NULL,
    producer_id VARCHAR(100) NOT NULL,
    date_time TIMESTAMP NOT NULL,
    operating_system VARCHAR(100) REFERENCES operating_systems(id),
    ram_load_percentage FLOAT NOT NULL,
    swap_load_percentage FLOAT NOT NULL
);
