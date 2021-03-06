-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 15, 2013 at 11:30 AM
-- Server version: 5.5.29
-- PHP Version: 5.4.6-1ubuntu1.1

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `crawler`
--

-- --------------------------------------------------------

--
-- Table structure for table `table1`
--

/*CREATE DATABASE crawler
USE crawler*/

CREATE TABLE IF NOT EXISTS `table1` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- Table structure for table `table2`
--

CREATE TABLE IF NOT EXISTS `table2` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table3`
--

CREATE TABLE IF NOT EXISTS `table3` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=24 ;

--
-- Dumping data for table `table3`
--

INSERT INTO `table3` (`Sr_no`, `Acronym`, `Type`, `Dates`, `Links`, `Time`) VALUES
(23, 'CIKM', '', 'june 3, 2013', 'http://www.cikm2013.org/', '2013-04-15 04:54:11');

-- --------------------------------------------------------

--
-- Table structure for table `table4`
--

CREATE TABLE IF NOT EXISTS `table4` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table5`
--

CREATE TABLE IF NOT EXISTS `table5` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table6`
--

CREATE TABLE IF NOT EXISTS `table6` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table7`
--

CREATE TABLE IF NOT EXISTS `table7` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table8`
--

CREATE TABLE IF NOT EXISTS `table8` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table9`
--

CREATE TABLE IF NOT EXISTS `table9` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Dumping data for table `table9`
--

INSERT INTO `table9` (`Sr_no`, `Acronym`, `Type`, `Dates`, `Links`, `Time`) VALUES
(14, 'ICDM', '', 'june 21', 'http://icdm2013.rutgers.edu/dates', '2013-04-15 05:12:27');

-- --------------------------------------------------------

--
-- Table structure for table `table10`
--

CREATE TABLE IF NOT EXISTS `table10` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table11`
--

CREATE TABLE IF NOT EXISTS `table11` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table12`
--

CREATE TABLE IF NOT EXISTS `table12` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table13`
--

CREATE TABLE IF NOT EXISTS `table13` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `table13`
--

INSERT INTO `table13` (`Sr_no`, `Acronym`, `Type`, `Dates`, `Links`, `Time`) VALUES
(1, 'MFCS', '', '', '', '2013-04-14 23:06:25');

-- --------------------------------------------------------

--
-- Table structure for table `table14`
--

CREATE TABLE IF NOT EXISTS `table14` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table15`
--

CREATE TABLE IF NOT EXISTS `table15` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table16`
--

CREATE TABLE IF NOT EXISTS `table16` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table17`
--

CREATE TABLE IF NOT EXISTS `table17` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table18`
--

CREATE TABLE IF NOT EXISTS `table18` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table19`
--

CREATE TABLE IF NOT EXISTS `table19` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `table19`
--

INSERT INTO `table19` (`Sr_no`, `Acronym`, `Type`, `Dates`, `Links`, `Time`) VALUES
(1, 'STACS', '', 'Traceback (most recent call last):', 'http://www.stacs2013.uni-kiel.de/', '2013-04-14 22:36:40');

-- --------------------------------------------------------

--
-- Table structure for table `table20`
--

CREATE TABLE IF NOT EXISTS `table20` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table21`
--

CREATE TABLE IF NOT EXISTS `table21` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table22`
--

CREATE TABLE IF NOT EXISTS `table22` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `table22`
--

INSERT INTO `table22` (`Sr_no`, `Acronym`, `Type`, `Dates`, `Links`, `Time`) VALUES
(1, 'VLDB', 'oijk', '', '', '2013-04-14 22:04:56'),
(2, 'VLDB', 'oijk', 'march 1st, 2013', 'http://www.vldb.org/2013/important_dates.html', '2013-04-14 22:13:14'),
(3, 'VLDB', 'oijk', 'march 1st, 2013', 'http://www.vldb.org/2013/important_dates.html', '2013-04-14 22:15:44');

-- --------------------------------------------------------

--
-- Table structure for table `table23`
--

CREATE TABLE IF NOT EXISTS `table23` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table24`
--

CREATE TABLE IF NOT EXISTS `table24` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table25`
--

CREATE TABLE IF NOT EXISTS `table25` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `table26`
--

CREATE TABLE IF NOT EXISTS `table26` (
  `Sr_no` int(11) NOT NULL AUTO_INCREMENT,
  `Acronym` varchar(30) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Dates` varchar(100) NOT NULL,
  `Links` varchar(500) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sr_no`),
  KEY `Acronym` (`Acronym`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
