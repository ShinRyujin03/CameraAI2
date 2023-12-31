-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th9 28, 2023 lúc 10:26 AM
-- Phiên bản máy phục vụ: 10.4.28-MariaDB
-- Phiên bản PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `metadata`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `detected_objects`
--

CREATE TABLE `detected_objects` (
  `id` int(11) NOT NULL,
  `image_name` varchar(255) NOT NULL,
  `objects_name` varchar(50) NOT NULL,
  `objects_location_boxes` varchar(255) NOT NULL,
  `objects_location_weights` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `face_emotions`
--

-- Cấu trúc bảng cho bảng `face_facial_attribute`
CREATE TABLE `face_facial_attribute` (
    `id` int(11) NOT NULL,
    `image_name` varchar(255) NOT NULL,
    `emotions` varchar(255) NOT NULL,
    `ages` VARCHAR(255) NOT NULL,
    `gender` VARCHAR(255) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `face_landmark`
--

CREATE TABLE `face_landmark` (
  `id` int(11) NOT NULL,
  `image_name` varchar(255) NOT NULL,
  `bottom_lip` varchar(255) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `chin` varchar(255) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `left_eye` varchar(255) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `left_eyebrow` varchar(255) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `nose_bridge` varchar(255) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `nose_tip` varchar(255) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `right_eye` varchar(255) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `right_eyebrow` varchar(255) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `top_lip` varchar(255) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `face_location`
--

CREATE TABLE `face_location` (
  `id` int(11) NOT NULL,
  `image_name` varchar(255) NOT NULL,
  `face_location` varchar(500) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `face_location`
--


-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `face_metadata`
--

CREATE TABLE `face_metadata` (
  `id` int(11) NOT NULL,
  `image_name` varchar(255) NOT NULL,
  `image_file` longblob DEFAULT NULL,
  `face_name` varchar(255) DEFAULT NULL,
  `face_location` varchar(255) DEFAULT NULL,
  `emotions` varchar(50) DEFAULT NULL,
  `ages` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `verify_status` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `face_verified`
--

CREATE TABLE `face_verified` (
  `id` int(11) NOT NULL,
  `image_name` varchar(255) NOT NULL,
  `face_name` varchar(255) NOT NULL,
  `verify_status` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `human_location`
--

CREATE TABLE `human_location` (
  `id` int(11) NOT NULL,
  `image_name` varchar(255) NOT NULL,
  `human_location_boxes` varchar(500) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `human_location_weights` varchar(255) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `image`
--

CREATE TABLE `image` (
  `id` int(11) NOT NULL,
  `image_name` varchar(500) NOT NULL,
  `image_file` longblob NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


--
-- Chỉ mục cho bảng `detected_objects`
--
ALTER TABLE `detected_objects`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `face_emotions`
--
ALTER TABLE `face_facial_attribute`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `face_landmark`
--
ALTER TABLE `face_landmark`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `face_location`
--
ALTER TABLE `face_location`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `face_metadata`
--
ALTER TABLE `face_metadata`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `image_name` (`image_name`);

--
-- Chỉ mục cho bảng `face_verified`
--
ALTER TABLE `face_verified`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `human_location`
--
ALTER TABLE `human_location`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `image`
--
ALTER TABLE `image`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `detected_objects`
--
ALTER TABLE `detected_objects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT cho bảng `face_emotions`
--
ALTER TABLE `face_facial_attribute`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT cho bảng `face_landmark`
--
ALTER TABLE `face_landmark`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT cho bảng `face_location`
--
ALTER TABLE `face_location`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT cho bảng `face_metadata`
--
ALTER TABLE `face_metadata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT cho bảng `face_verified`
--
ALTER TABLE `face_verified`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT cho bảng `human_location`
--
ALTER TABLE `human_location`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT cho bảng `image`
--
ALTER TABLE `image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
COMMIT;

-- Trigger for face_facial_attribute
DELIMITER //

CREATE TRIGGER after_insert_face_emotions
AFTER INSERT ON face_facial_attribute
FOR EACH ROW
BEGIN
    INSERT INTO face_metadata (image_name, emotions)
    VALUES (NEW.image_name, NEW.emotions)
    ON DUPLICATE KEY UPDATE emotions = NEW.emotions;
END //

CREATE TRIGGER after_insert_face_location
AFTER INSERT ON face_location
FOR EACH ROW
BEGIN
    INSERT INTO face_metadata (image_name, face_location)
    VALUES (NEW.image_name, NEW.face_location)
    ON DUPLICATE KEY UPDATE face_location = NEW.face_location;
END //

CREATE TRIGGER after_insert_face_verified
AFTER INSERT ON face_verified
FOR EACH ROW
BEGIN
    INSERT INTO face_metadata (image_name, verify_status)
    VALUES (NEW.image_name, NEW.verify_status)
    ON DUPLICATE KEY UPDATE verify_status = NEW.verify_status;
END //

CREATE TRIGGER after_insert_image
AFTER INSERT ON image
FOR EACH ROW
BEGIN
    INSERT INTO face_metadata (image_name, image_file)
    VALUES (NEW.image_name, NEW.image_file)
    ON DUPLICATE KEY UPDATE image_file = NEW.image_file;
END //

-- Trigger for face_facial_attribute
CREATE TRIGGER insert_gender_age
AFTER INSERT ON face_facial_attribute
FOR EACH ROW
BEGIN
    INSERT INTO face_metadata (image_name, gender, ages)
    VALUES (NEW.image_name, NEW.gender, NEW.ages)
    ON DUPLICATE KEY UPDATE gender = NEW.gender, ages = NEW.ages;
END //

CREATE TRIGGER update_face_emotions
AFTER INSERT ON face_facial_attribute
FOR EACH ROW
BEGIN
    INSERT INTO face_metadata (image_name, emotions)
    VALUES (NEW.image_name, NEW.emotions)
    ON DUPLICATE KEY UPDATE emotions = NEW.emotions;
END //

CREATE TRIGGER update_face_location
AFTER INSERT ON face_location
FOR EACH ROW
BEGIN
    INSERT INTO face_metadata (image_name, face_location)
    VALUES (NEW.image_name, NEW.face_location)
    ON DUPLICATE KEY UPDATE face_location = NEW.face_location;
END //

CREATE TRIGGER update_face_verified
AFTER INSERT ON face_verified
FOR EACH ROW
BEGIN
    INSERT INTO face_metadata (image_name, face_name, verify_status)
    VALUES (NEW.image_name, NEW.face_name, NEW.verify_status)
    ON DUPLICATE KEY UPDATE face_name = NEW.face_name, verify_status = NEW.verify_status;
END //

CREATE TRIGGER update_gender_age
AFTER UPDATE ON face_facial_attribute
FOR EACH ROW
BEGIN
    UPDATE face_metadata
    SET gender = NEW.gender, ages = NEW.ages
    WHERE image_name = NEW.image_name;
END //

DELIMITER ;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
