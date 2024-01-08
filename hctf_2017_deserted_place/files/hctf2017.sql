
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

DROP DATABASE IF EXISTS `hctf2017`;
CREATE DATABASE `hctf2017` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hctf2017;

DROP TABLE IF EXISTS `records`;
CREATE TABLE `records` (
  `id` int(20) NOT NULL,
  `link` text NOT NULL,
  `is_read` int(20) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `email` varchar(40) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `users` (`id`, `username`, `password`, `email`, `message`) VALUES
(1, 'hctf_admin_LoRexxar2e23', 'e10adc3949ba59abbe56e057f20f883e', 'None', 'None'),
(2, 'admin', '21232f297a57a5a743894a0e4a801fc3', '<img src=\"1\" onerror=\"alert(1)\">', 'None'),
(3, 'admin1', 'e00cf25ad42683b3df678c61f42c6bda', NULL, NULL);

ALTER TABLE `records`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `records`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;COMMIT;
