-- Create the database
CREATE DATABASE IF NOT EXISTS user_auth_db;

-- Use the database
USE user_auth_db;

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL
);

-- Create a table to store user login history (optional)
CREATE TABLE IF NOT EXISTS login_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    status VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Optional: Create a stored procedure to log login attempts
DELIMITER //
CREATE PROCEDURE LogLoginAttempt(
    IN p_username VARCHAR(50),
    IN p_status VARCHAR(20),
    IN p_ip_address VARCHAR(45)
)
BEGIN
    DECLARE user_id_var INT;
    
    -- Get the user ID
    SELECT id INTO user_id_var FROM users WHERE username = p_username;
    
    -- If user exists, log the attempt
    IF user_id_var IS NOT NULL THEN
        INSERT INTO login_history (user_id, status, ip_address)
        VALUES (user_id_var, p_status, p_ip_address);
        
        -- If login was successful, update last_login time
        IF p_status = 'success' THEN
            UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = user_id_var;
        END IF;
    END IF;
END //
DELIMITER ;

-- Optional: Create an index on the username column for faster lookups
CREATE INDEX idx_username ON users(username);