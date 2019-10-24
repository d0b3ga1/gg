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
('news', 'img1.jpg', 'Lễ trao chứng nhận kiểm định chất lượng giáo dục cho ngành Quản trị Khách sạn bậc đại học', 'NTTU - Vừa qua, Trung tâm Kiểm định chất lượng Giáo dục ĐHQG TP.HCM đã ký quyết định công nhận 2 chương trình đào tạo của Trường ĐH Nguyễn Tất Thành là Quản trị Khách sạn và Công nghệ Kỹ thuật Điện – Điện'),
('news', 'img2.jpg', 'Trường ĐH Nguyễn Tất Thành đạt chuẩn 4 sao của tổ chức QS Stars Anh Quốc', 'NTTU - Trải qua quá trình nghiêm túc và độc lập trong việc thu thập số liệu và đánh giá hoạt động của Trường theo bộ tiêu chuẩn QS Stars, vừa qua Tổ chức QS chính thức công nhận Trường Đại học Nguyễn Tất Thành đạt'),
('news', 'img3.jpg', 'ĐH Nguyễn Tất Thành tuyển sinh Thạc sỹ đợt 2 năm 2019', 'NTTU – Viện Nghiên cứu và Đào tạo sau đại học Trường ĐH Nguyễn Tất Thành thông báo tuyển sinh bậc sau đại học đợt 2 năm 2019. Hồ sơ nhận đến ngày 30/10/2019');


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
