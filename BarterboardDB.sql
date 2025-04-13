-- Valencia, Jhon Lloyd M.
-- BARTERBOARD – Reviving Barter, Reinventing Exchange

-- Create a new database
CREATE DATABASE IF NOT EXISTS BarterBoard;
USE BarterBoard;

-- Create 'users' table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Create 'listings' table
CREATE TABLE IF NOT EXISTS listings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    item TEXT NOT NULL,
    description TEXT NOT NULL,
    quantity INT NOT NULL,
    location TEXT NOT NULL,
    desired_barter TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS proposals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    listing_id INTEGER NOT NULL,
    username TEXT,
    item TEXT,
    description TEXT,
    quantity INT,
    from_user TEXT,
    status VARCHAR(255) DEFAULT 'Pending'
);

CREATE TABLE IF NOT EXISTS transactions (
	id INT AUTO_INCREMENT PRIMARY KEY,
	from_user TEXT,
	to_user TEXT,
	item TEXT,
	description TEXT,
	quantity INT,
	status TEXT
);
SET SQL_SAFE_UPDATES = 0;

-- Insert data into 'users'
INSERT INTO users (username, password) VALUES
('alice01', 'password()'),
('lloyd', 'Kahitano1'),
('joshua', 'firstmovekanapls'),
('ednaa', 'blackpink08'),
('elena23', 'skyfall321'),
('frankD', 'go4it987'),
('gwen_stacy', 'pw123!@#'),
('lucyy', 'Kahitano1'),
('ivy_lee', 'greenivy44'),
('jake_s', 'jake2025'),
('abbyy', 'lucy0919629141'),
('lorenz', 'mace123'),
('jhonlloyd', '011405'),
('valencia', 'Kahitano1');

-- Insert data into 'listings'
INSERT INTO listings (user_id, item, description, quantity, location, desired_barter) VALUES
(1, 'Camping Tent', '4-person waterproof tent', 1, 'New York', 'Sleeping Bags'),
(2, 'Mountain Bike', 'Used but in pristine condition', 1, 'Lucena City', 'Skateboard'),
(3, 'Guitar', 'Acoustic guitar, barely used', 1, 'Austin', 'Keyboard'),
(4, 'Books', 'Set of mystery novels', 10, 'San Juan Batangas', 'Cookbooks'),
(5, 'Lawn Mower', 'Electric, fully working', 1, 'Los Banos', 'Power Tools'),
(6, 'Camera', 'Sony a6400 with lens', 1, 'Seattle', 'GoPro'),
(7, 'iPhone 16', 'Brand New', 1, 'Lucena City', 'iPad Pro 11'),
(8, 'Art Supplies', 'Acrylic paint set with brushes', 5, 'Denver', 'Sketchbooks'),
(9, 'LED Monitor', '27-inch 1080p', 1, 'Boston', 'Laptop Parts'),
(10, 'Coffee Maker', 'Espresso machine', 1, 'San Francisco', 'Coffee Beans'),
(11, 'Hirono', 'The Insight', 2, 'Los Banos', 'Hirono The Switchman'),
(12, 'Macbook Air M1', '3rd Hand', 1, 'Lucena City', 'Sony a6400'),
(13, 'Ben10 Brief', '2nd hand, pristine cond.', 1, 'Sariaya Quezon', 'Calvin Klein Brief'),
(3, 'Earphones', 'Sirang right piece', 2, 'Lucban', 'Earbuds'),
(3, 'Mouse Pad', 'Black with blue shade', 1, 'Lucban', 'Earbuds'),
(3, 'Mech Keyboard', 'Aula F75', 1, 'Lucban', '68 key piano');

-- Update a listing description
UPDATE listings
SET description = '4-person waterproof camping tent with extra stakes update'
WHERE item = 'Camping Tent';

-- Delete one record from 'listings'
DELETE FROM listings
WHERE item = 'Lawn Mower';

-- SELECT Statements

-- 1. All listings in New York
SELECT * FROM listings
WHERE location = 'New York';

-- 2. Listings with quantity >= 5
SELECT * FROM listings
WHERE quantity >= 5;

-- 3. Listings sorted by location
SELECT * FROM listings
ORDER BY location ASC;

-- 4. Users whose usernames start with 'a' or 'b'
SELECT * FROM users
WHERE username LIKE 'a%' OR username LIKE 'b%';

-- 5. Join: Show listings with the owner's username
SELECT l.item, l.description, u.username, l.location
FROM listings l
JOIN users u ON l.user_id = u.id;

-- 6. Get all listings that want to barter for 'Coffee Beans'
SELECT * FROM listings
WHERE desired_barter = 'Coffee Beans';

-- 7. Count how many listings each user has posted
SELECT u.username, COUNT(l.id) AS total_listings
FROM users u
LEFT JOIN listings l ON u.id = l.user_id
GROUP BY u.username;

-- 8. Find the listings with the highest quantityyu
SELECT * FROM listings
ORDER BY quantity DESC
LIMIT 1;

