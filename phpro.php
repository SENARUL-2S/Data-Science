<?php
// config.php - Database connection
$host = 'localhost';
$user = 'root';
$pass = '';
$dbname = 'service_directory';
$conn = new mysqli($host, $user, $pass, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>

<!-- index.php -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Directory</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Welcome to Service Directory</h1>
    <ul>
        <li><a href="services.php?category=doctor">Doctors</a></li>
        <li><a href="services.php?category=hospital">Hospitals</a></li>
        <li><a href="services.php?category=transport">Bus & Train Schedule</a></li>
        <li><a href="services.php?category=emergency">Emergency Services</a></li>
    </ul>
</body>
</html>

<?php
// services.php - Display services by category with pagination
include 'config.php';
$category = $_GET['category'] ?? '';
$page = isset($_GET['page']) ? (int)$_GET['page'] : 1;
$limit = 20;
$offset = ($page - 1) * $limit;

$sql = "SELECT * FROM services WHERE category='$category' LIMIT $limit OFFSET $offset";
$result = $conn->query($sql);
?>
<!DOCTYPE html>
<html>
<head>
    <title>Services - <?php echo ucfirst($category); ?></title>
</head>
<body>
    <h2><?php echo ucfirst($category); ?> List</h2>
    <ul>
        <?php while ($row = $result->fetch_assoc()) { ?>
            <li><?php echo $row['name'] . ' - ' . $row['contact']; ?></li>
        <?php } ?>
    </ul>
    <div>
        <?php
        $result_total = $conn->query("SELECT COUNT(*) as total FROM services WHERE category='$category'");
        $row_total = $result_total->fetch_assoc();
        $total_pages = ceil($row_total['total'] / $limit);
        for ($i = 1; $i <= $total_pages; $i++) {
            echo "<a href='services.php?category=$category&page=$i'>$i</a> ";
        }
        ?>
    </div>
</body>
</html>

<?php
// database.sql - Create database and table
/*
CREATE DATABASE service_directory;
USE service_directory;
CREATE TABLE services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(50),
    contact VARCHAR(100)
);
INSERT INTO services (name, category, contact) VALUES
('Dr. Rahim', 'doctor', '1234567890'),
('City Hospital', 'hospital', '0987654321'),
('Dhaka Bus Service', 'transport', '5678901234');
*/
?>
