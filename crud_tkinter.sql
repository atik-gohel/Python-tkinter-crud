-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 17, 2021 at 10:20 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crud tkinter`
--

-- --------------------------------------------------------

--
-- Table structure for table `designation`
--

CREATE TABLE `designation` (
  `id` int(11) NOT NULL,
  `edesignation` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `designation`
--

INSERT INTO `designation` (`id`, `edesignation`) VALUES
(1, 'select skill'),
(2, 'Application Developer'),
(3, 'UI/UX Designer'),
(4, 'Laravel Developer'),
(5, 'WORDPRESS Developer'),
(6, 'Game Developer'),
(7, 'ASP.NET Developer');

-- --------------------------------------------------------

--
-- Table structure for table `employee_master`
--

CREATE TABLE `employee_master` (
  `id` int(11) NOT NULL,
  `ename` varchar(255) NOT NULL,
  `eaddress` varchar(255) NOT NULL,
  `ecity` varchar(255) NOT NULL,
  `ebdate` varchar(255) NOT NULL,
  `emonthlysalary` varchar(255) NOT NULL,
  `eclass` varchar(255) NOT NULL,
  `egender` varchar(255) NOT NULL,
  `edesignation` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee_master`
--

INSERT INTO `employee_master` (`id`, `ename`, `eaddress`, `ecity`, `ebdate`, `emonthlysalary`, `eclass`, `egender`, `edesignation`) VALUES
(98, 'atik ', 'hl  ', 'kjhl  ', 'kjh  ', 'ljkh  ', 'Class_IV', 'Female', 'Application Developer  '),
(100, 'l', 'jhl', 'kjh', 'lkj', 'hlkj', 'Class_II', 'Female', 'Application Developer'),
(102, 'lkjh', 'ljk', 'hlkj', 'h', 'lkjhl', 'Class_IV', 'Female', 'WORDPRESS Developer'),
(103, 'lkjh', 'lkj', 'hlkj', 'h', 'lkjhl', 'Class_III', 'Female', 'UI/UX Designer'),
(104, 'lh', 'lkj', 'hlkj', 'hl', 'kjh', 'Class_I', 'Male', 'UI/UX Designer'),
(105, 'lkj', 'hlk', 'jhl', 'kj', 'hlkj', 'Class_I', 'Female', 'WORDPRESS Developer'),
(106, 'kln', 'k;lkj', ';lkj;', 'lkj', ';lk', 'Class_I', 'Male', 'ASP.NET Developer'),
(107, ';hlkjh', 'lkj', 'hlkj', 'hl', 'kj', 'Class_I', 'Male', 'UI/UX Designer'),
(108, 'nb', 'jk', 'nkj', 'njk', 'n', 'Class_II', 'Female', 'Laravel Developer'),
(109, 'j', 'j', 'jjj', 'j', 'jj', 'Class_I', 'Male', 'Application Developer'),
(110, 'jk', 'jk', 'jkkj', 'k', 'kjj', 'Class_II', 'Male', 'UI/UX Designer'),
(113, 'jj', 'kj', 'jkjk', 'jk', 'jkjk', 'Class_II', 'Other', 'WORDPRESS Developer'),
(114, 'jn', 'jk', 'jk', 'jk', 'jk', 'Class_II', 'Male', 'Application Developer'),
(115, 'danish', 'fh-8', 'Rajkot', '22-4-1998', '100020', 'Class_II', 'Male', 'WORDPRESS Developer'),
(116, 'danis ', 'j  ', 'lkj  ', 'gljk  ', 'h  ', 'Class_IV', 'Other', 'Game Developer  '),
(117, ',kjhlkjh ', 'lkj ', 'hlk ', 'jh ', 'lkj ', '(\'Class_I\',)', '(\'Male\',)', 'Laravel Developer '),
(118, 'ASDLKJFAHLKSJH', 'LKJ', 'HLK', 'JHLKJ', 'HLJK', 'Class_I', 'Male', 'Game Developer'),
(119, 'LHJ', 'GJ', 'HGK', 'JH', 'GH', 'Class_I', 'Male', 'Application Developer'),
(120, 'KHG', 'KJH', 'GKJ', 'HG', 'KJH', 'Class_I', 'Male', 'Application Developer'),
(121, 'KK', 'J', 'KJ', 'KJ', 'KJKJK', 'JKJ', 'KJK', 'KJK'),
(122, 'MOHIT ', 'LKJ  ', 'HLK  ', 'JH  ', 'LKJ  ', '(\"(\'Class_I\',)\",)', '(\"(\'Male\',)\",)', 'UI/UX Designer  '),
(124, 'f;alsdkf;k', 'hlj', 'l', 'jkg', 'kjh', 'Class_I', 'Male', 'Laravel Developer'),
(125, 'l', 'kjh', 'ljk', 'hl', 'kjh', 'Class_I', 'Female', 'Laravel Developer'),
(126, 'ksdfkjhLKJ', 'HLKjHLKJhlkjh', 'lk', 'jh', 'lkj', 'Class_II', 'Male', 'Laravel Developer'),
(127, 'atik', 'sfa', ';lj;lkj', 'lkj', 'lkjk', 'Class_I', 'Male', 'WORDPRESS Developer'),
(128, 'k', '.lkj', '.m,', 'lk', 'jlk', 'Class_II', 'Male', 'UI/UX Designer'),
(130, 'sadjkfhlkj', 'l', 'kjhl', 'kjh', 'lkj', 'Class_IV', 'Female', 'Game Developer'),
(134, 'ljhg ljkhlkj', 'kjh ', 'gkj ', 'gh ', 'kjh ', '(\'Class_IV\',)', '(\'Male\',)', 'Application Developer '),
(135, 'dlakjhl', 'jh', 'gkjh', 'gkj', 'h', 'Class_I', 'Male', 'Application Developer');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `designation`
--
ALTER TABLE `designation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employee_master`
--
ALTER TABLE `employee_master`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `designation`
--
ALTER TABLE `designation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `employee_master`
--
ALTER TABLE `employee_master`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=136;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
