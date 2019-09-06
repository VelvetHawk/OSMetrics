CREATE TABLE OPERATING_SYSTEMS (
    ID INT PRIMARY KEY NOT NULL,
    NAME VARCHAR(255) NOT NULL,
    RELEASE VARCHAR(255) NOT NULL,
    ARCHITECTURE VARCHAR(255) NOT NULL,
    VERSION VARCHAR(255) NOT NULL,
    PROCESSOR VARCHAR(255) NOT NULL,
    PHYYSICAL_CORES INT NOT NULL,
    LOGICAL_CORES INT NOT NULL,
    TOTAL_RAM INT NOT NULL,
    TOTAL_SWAPSPACE INT NOT NULL
);

CREATE TABLE METRICS (
    ID INT PRIMARY KEY NOT NULL,
    OPERATING_SYSTEM INT REFERENCES OPERATING_SYSTEMS(ID),
);