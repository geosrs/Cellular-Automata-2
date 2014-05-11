CREATE TABLE row_count (
	amount	INTEGER		NOT NULL	DEFAULT	0
	);

INSERT INTO row_count (amount) VALUES (0);

CREATE TABLE history (
	rule_number	INTEGER		PRIMARY KEY 	AUTOINCREMENT,
	time		TIMESTAMP		NOT NULL 	DEFAULT 	CURRENT_TIMESTAMP,
	wrap		INTEGER		NOT NULL	DEFAULT	1,
	dimension	INTEGER		NOT NULL	DEFAULT	1,
	interest	INTEGER		NOT NULL	DEFAULT	2,
	rule		VARCHAR(255)		NOT NULL 	DEFAULT 	'',
	image		VARCHAR(255)		NOT NULL 	DEFAULT 	''
	);
 
CREATE TRIGGER increment_row_count AFTER INSERT ON history
	BEGIN
		UPDATE row_count SET amount = amount + 1 WHERE 1 = 1;
	END;

CREATE TRIGGER decrement_row_count AFTER DELETE ON history
	BEGIN
		UPDATE row_count SET amount = amount - 1 WHERE 1 = 1;
	END;
