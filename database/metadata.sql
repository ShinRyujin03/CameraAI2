-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 05, 2023 at 08:42 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `metadata`
--

-- --------------------------------------------------------

--
-- Table structure for table `face_landmark`
--

CREATE TABLE `face_landmark` (
  `id` int(11) NOT NULL,
  `image_name` varchar(500) NOT NULL,
  `bottom_lip` varchar(500) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `chin` varchar(500) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `left_eye` varchar(500) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `left_eyebrow` varchar(500) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `nose_bridge` varchar(500) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `nose_tip` varchar(500) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `right_eye` varchar(500) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `right_eyebrow` varchar(500) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `top_lip` varchar(500) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- --------------------------------------------------------

--
-- Table structure for table `face_location`
--

CREATE TABLE `face_location` (
  `id` int(11) NOT NULL,
  `image_name` varchar(500) NOT NULL,
  `face_location` varchar(500) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- --------------------------------------------------------

--
-- Table structure for table `human_location`
--

CREATE TABLE `human_location` (
  `id` int(11) NOT NULL,
  `image_name` varchar(500) NOT NULL,
  `human_location_boxes` varchar(500) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `human_location_weights` varchar(500) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
--
-- Indexes for dumped tables
--

--
-- Indexes for table `face_landmark`
--
ALTER TABLE `face_landmark`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `face_location`
--
ALTER TABLE `face_location`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `human_location`
--
ALTER TABLE `human_location`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `face_landmark`
--
ALTER TABLE `face_landmark`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT for table `face_location`
--
ALTER TABLE `face_location`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT for table `human_location`
--
ALTER TABLE `human_location`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
