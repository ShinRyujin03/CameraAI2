-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th8 23, 2023 lúc 04:30 AM
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
-- Cơ sở dữ liệu: `face_metadata`
--

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

--
-- Đang đổ dữ liệu cho bảng `face_landmark`
--

INSERT INTO `face_landmark` (`id`, `image_name`, `bottom_lip`, `chin`, `left_eye`, `left_eyebrow`, `nose_bridge`, `nose_tip`, `right_eye`, `right_eyebrow`, `top_lip`, `created_at`) VALUES
(6, '239076911_1317254428690642_1307688377531805723_n.jpg', '[(691, 404), (680, 415), (670, 421), (662, 422), (653, 421), (645, 416), (637, 407), (642, 407), (653, 407), (661, 408), (668, 406), (686, 404)]', '[(581, 317), (584, 340), (589, 364), (597, 386), (606, 407), (619, 424), (634, 440), (651, 452), (670, 456), (692, 451), (712, 436), (730, 418), (745, 397), (753, 373), (759, 347), (763, 321), (764, 294)]', '[(604, 317), (613, 310), (625, 310), (636, 320), (624, 322), (612, 322)]', '[(589, 298), (599, 290), (612, 288), (626, 291), (639, 297)]', '[(656, 315), (656, 332), (656, 349), (656, 366)]', '[(644, 377), (652, 380), (660, 382), (668, 379), (675, 376)]', '[(683, 317), (692, 306), (705, 304), (718, 310), (708, 316), (694, 318)]', '[(669, 295), (684, 287), (701, 282), (718, 282), (734, 289)]', '[(637, 407), (644, 398), (652, 392), (660, 394), (667, 392), (678, 397), (691, 404), (686, 404), (668, 403), (660, 404), (653, 403), (642, 407)]', '2023-08-23 02:26:57'),
(7, 'IU.PNG', '[(481, 322), (473, 330), (463, 332), (455, 332), (446, 330), (432, 325), (416, 317), (424, 315), (448, 314), (456, 315), (463, 316), (475, 320)]', '[(309, 225), (311, 255), (314, 287), (321, 316), (338, 340), (362, 359), (389, 374), (417, 385), (443, 388), (466, 386), (485, 374), (501, 358), (513, 338), (523, 316), (528, 290), (531, 267), (532, 242)]', '[(375, 207), (389, 201), (404, 201), (417, 211), (403, 213), (388, 213)]', '[(352, 179), (370, 167), (392, 163), (415, 166), (435, 174)]', '[(454, 205), (456, 220), (460, 235), (463, 250)]', '[(436, 275), (447, 276), (456, 277), (464, 276), (471, 276)]', '[(475, 216), (489, 209), (503, 211), (513, 220), (503, 222), (489, 221)]', '[(469, 175), (486, 169), (504, 170), (520, 177), (528, 192)]', '[(416, 317), (433, 302), (449, 295), (457, 298), (465, 295), (476, 305), (481, 322), (475, 320), (463, 310), (456, 310), (448, 309), (424, 315)]', '2023-08-23 02:28:20');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `face_location`
--

CREATE TABLE `face_location` (
  `id` int(11) NOT NULL,
  `image_name` varchar(255) NOT NULL,
  `face_location` varchar(255) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `face_location`
--

INSERT INTO `face_location` (`id`, `image_name`, `face_location`, `created_at`) VALUES
(8, '239076911_1317254428690642_1307688377531805723_n.jpg', '[(263, 758, 449, 572)]', '2023-08-23 02:26:54'),
(9, 'IU.PNG', '[(112, 587, 379, 319)]', '2023-08-23 02:28:23');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `human_location`
--

CREATE TABLE `human_location` (
  `id` int(11) NOT NULL,
  `image_name` varchar(255) NOT NULL,
  `human_location_boxes` varchar(255) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `human_location_weights` varchar(255) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `human_location`
--

INSERT INTO `human_location` (`id`, `image_name`, `human_location_boxes`, `human_location_weights`, `created_at`) VALUES
(4, '239076911_1317254428690642_1307688377531805723_n.jpg', '[[309  34  85 170]]', '[0.4615867]', '2023-08-23 02:26:51');

--
-- Chỉ mục cho các bảng đã đổ
--

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
-- Chỉ mục cho bảng `human_location`
--
ALTER TABLE `human_location`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `face_landmark`
--
ALTER TABLE `face_landmark`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT cho bảng `face_location`
--
ALTER TABLE `face_location`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT cho bảng `human_location`
--
ALTER TABLE `human_location`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
