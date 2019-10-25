--
-- Database: `crud`
--
create database if not exists `crud`;
use `crud`;

--
-- Table structure for table `article`
--
CREATE TABLE `article` (
  `id` int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  `imgname` varchar(255) NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  `title` varchar(255) NOT NULL,
  `content` varchar(255) NOT NUll
);


--
-- Dumping data for table `article`
--
INSERT INTO `article` (`type`, `imgname`, `title`, `content`) VALUES
('event', 'event.jpg', 'Chương trình Chào mừng năm học mới - Nhận chứng nhận kiểm định chất lượng chương trình đào tạo Ngành Quản trị khách sạn', 'Hội trường lầu 9, cơ sở An Phú Đông, 331 Quốc lộ 1A, Phường An Phú Đông, Quận 12'),
('event', 'event.jpg', 'Ngày Doanh nhân Việt Nam và Đại hội CLB Doanh nghiệp Trường Đại học Nguyễn Tất Thành', 'Hội trường A.801, 300A Nguyễn Tất Thành, phường 13, quận 4, TP. HCM'),
('event', 'event.jpg', 'Lễ tốt nghiệp cho Sinh viên bậc Đại học liên thông từ Trung cấp khóa 2016; bậc Cao đẳng liên thông từ Trung cấp khóa 2017', 'Hội trường A.801, 300A Nguyễn Tất Thành, phường 13, quận 4, TP. HCM'),
('news', 'tintuc3.jpg', 'ĐH Nguyễn Tất Thành tuyển sinh Thạc sỹ đợt 2 năm 2019', 'NTTU – Viện Nghiên cứu và Đào tạo sau đại học Trường ĐH Nguyễn Tất Thành thông báo tuyển sinh bậc sau đại học đợt 2 năm 2019. Hồ sơ nhận đến ngày 30/10/2019'),
('news', 'tintuc2.jpg', 'Cầu nối việc làm vững chắc cho sinh viên', 'NTTU – Chiều ngày 10/10/2019 đã diễn ra Đại hội Câu lạc bộ Doanh nghiệp Trường ĐH Nguyễn Tất Thành tại Hội trường cơ sở chính. Đồng thời, đây cũng là dịp ...'),
('news', 'tintuc1.jpg', 'Lễ khai giảng cho sinh viên quốc tế năm học 2019 - 2020', 'NTTU – Hòa chung vào không khí hân hoan toàn Trường ĐH Nguyễn Tất Thành chào đón năm mới, sáng ngày 11/03/2019, được sự cho phép của ban lãnh đạo Nhà trường, ...');


--
-- Table structure for table `account`
--
CREATE TABLE IF NOT EXISTS `accounts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;


--
-- Dumping data for table `accounts`
--
INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES (1, 'test', 'test', 'test@test.com');
