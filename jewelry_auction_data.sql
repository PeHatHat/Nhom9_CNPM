-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: jewelry_auction
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auction`
--

DROP TABLE IF EXISTS `auction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auction` (
  `auction_id` int NOT NULL AUTO_INCREMENT,
  `manager_id` int NOT NULL,
  `staff_id` int DEFAULT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `status` varchar(255) NOT NULL,
  PRIMARY KEY (`auction_id`),
  KEY `manager_id` (`manager_id`),
  KEY `staff_id` (`staff_id`),
  CONSTRAINT `auction_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `auction_ibfk_2` FOREIGN KEY (`staff_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auction`
--
-- ORDER BY:  `auction_id`

LOCK TABLES `auction` WRITE;
/*!40000 ALTER TABLE `auction` DISABLE KEYS */;
INSERT INTO `auction` (`auction_id`, `manager_id`, `staff_id`, `start_time`, `end_time`, `status`) VALUES (1,2,3,'2024-12-18 10:00:00','2024-12-18 12:00:00','scheduled'),(2,2,3,'2024-12-20 14:00:00','2024-12-20 16:00:00','scheduled');
/*!40000 ALTER TABLE `auction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--
-- ORDER BY:  `id`

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--
-- ORDER BY:  `id`

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--
-- ORDER BY:  `id`

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add auction',7,'add_auction'),(26,'Can change auction',7,'change_auction'),(27,'Can delete auction',7,'delete_auction'),(28,'Can view auction',7,'view_auction'),(29,'Can add jewelry',8,'add_jewelry'),(30,'Can change jewelry',8,'change_jewelry'),(31,'Can delete jewelry',8,'delete_jewelry'),(32,'Can view jewelry',8,'view_jewelry'),(33,'Can add user',9,'add_user'),(34,'Can change user',9,'change_user'),(35,'Can delete user',9,'delete_user'),(36,'Can view user',9,'view_user'),(37,'Can add transaction',10,'add_transaction'),(38,'Can change transaction',10,'change_transaction'),(39,'Can delete transaction',10,'delete_transaction'),(40,'Can view transaction',10,'view_transaction'),(41,'Can add request',11,'add_request'),(42,'Can change request',11,'change_request'),(43,'Can delete request',11,'delete_request'),(44,'Can view request',11,'view_request'),(45,'Can add blog',12,'add_blog'),(46,'Can change blog',12,'change_blog'),(47,'Can delete blog',12,'delete_blog'),(48,'Can view blog',12,'view_blog'),(49,'Can add bid',13,'add_bid'),(50,'Can change bid',13,'change_bid'),(51,'Can delete bid',13,'delete_bid'),(52,'Can view bid',13,'view_bid');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--
-- ORDER BY:  `id`

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES (1,'pbkdf2_sha256$600000$64RyE2XYTFjLRQuHuOV4TP$myxoHCeCGbyhuYGYcYrDfnsuRYBSBuZJP98YvNHoB24=','2024-12-18 11:18:27.877271',1,'nhom9','','','nhom9@gmail.com',1,1,'2024-12-18 10:49:32.302901');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--
-- ORDER BY:  `id`

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--
-- ORDER BY:  `id`

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bid`
--

DROP TABLE IF EXISTS `bid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bid` (
  `bid_id` int NOT NULL AUTO_INCREMENT,
  `auction_id` int NOT NULL,
  `jewelry_id` int NOT NULL,
  `buyer_id` int NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`bid_id`),
  KEY `auction_id` (`auction_id`),
  KEY `jewelry_id` (`jewelry_id`),
  KEY `buyer_id` (`buyer_id`),
  CONSTRAINT `bid_ibfk_1` FOREIGN KEY (`auction_id`) REFERENCES `auction` (`auction_id`),
  CONSTRAINT `bid_ibfk_2` FOREIGN KEY (`jewelry_id`) REFERENCES `jewelry` (`jewelry_id`),
  CONSTRAINT `bid_ibfk_3` FOREIGN KEY (`buyer_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bid`
--
-- ORDER BY:  `bid_id`

LOCK TABLES `bid` WRITE;
/*!40000 ALTER TABLE `bid` DISABLE KEYS */;
/*!40000 ALTER TABLE `bid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog`
--

DROP TABLE IF EXISTS `blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog` (
  `blog_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `author_id` int NOT NULL,
  `publication_date` datetime NOT NULL,
  PRIMARY KEY (`blog_id`),
  KEY `author_id` (`author_id`),
  CONSTRAINT `blog_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--
-- ORDER BY:  `blog_id`

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` (`blog_id`, `title`, `content`, `author_id`, `publication_date`) VALUES (1,'Welcome to our Jewelry Auction','This is the first blog post.',1,'2024-12-20 10:00:00'),(2,'Tips for Buying Jewelry','Here are some tips for buying jewelry.',1,'2024-12-21 12:00:00');
/*!40000 ALTER TABLE `blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_auction`
--

DROP TABLE IF EXISTS `core_auction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_auction` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `manager_id` bigint DEFAULT NULL,
  `staff_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_auction_manager_id_7c0a9bd0_fk_core_user_id` (`manager_id`),
  KEY `core_auction_staff_id_aace6e43_fk_core_user_id` (`staff_id`),
  CONSTRAINT `core_auction_manager_id_7c0a9bd0_fk_core_user_id` FOREIGN KEY (`manager_id`) REFERENCES `core_user` (`id`),
  CONSTRAINT `core_auction_staff_id_aace6e43_fk_core_user_id` FOREIGN KEY (`staff_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_auction`
--
-- ORDER BY:  `id`

LOCK TABLES `core_auction` WRITE;
/*!40000 ALTER TABLE `core_auction` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_auction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_auction_jewelry`
--

DROP TABLE IF EXISTS `core_auction_jewelry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_auction_jewelry` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `auction_id` bigint NOT NULL,
  `jewelry_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_auction_jewelry_auction_id_jewelry_id_780da34d_uniq` (`auction_id`,`jewelry_id`),
  KEY `core_auction_jewelry_jewelry_id_5c1966b9_fk_core_jewelry_id` (`jewelry_id`),
  CONSTRAINT `core_auction_jewelry_auction_id_fdaf219b_fk_core_auction_id` FOREIGN KEY (`auction_id`) REFERENCES `core_auction` (`id`),
  CONSTRAINT `core_auction_jewelry_jewelry_id_5c1966b9_fk_core_jewelry_id` FOREIGN KEY (`jewelry_id`) REFERENCES `core_jewelry` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_auction_jewelry`
--
-- ORDER BY:  `id`

LOCK TABLES `core_auction_jewelry` WRITE;
/*!40000 ALTER TABLE `core_auction_jewelry` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_auction_jewelry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_bid`
--

DROP TABLE IF EXISTS `core_bid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_bid` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `auction_id` bigint NOT NULL,
  `bidder_id` bigint NOT NULL,
  `jewelry_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_bid_auction_id_7ec39da5_fk_core_auction_id` (`auction_id`),
  KEY `core_bid_bidder_id_e4ca1418_fk_core_user_id` (`bidder_id`),
  KEY `core_bid_jewelry_id_9e2df97a_fk_core_jewelry_id` (`jewelry_id`),
  CONSTRAINT `core_bid_auction_id_7ec39da5_fk_core_auction_id` FOREIGN KEY (`auction_id`) REFERENCES `core_auction` (`id`),
  CONSTRAINT `core_bid_bidder_id_e4ca1418_fk_core_user_id` FOREIGN KEY (`bidder_id`) REFERENCES `core_user` (`id`),
  CONSTRAINT `core_bid_jewelry_id_9e2df97a_fk_core_jewelry_id` FOREIGN KEY (`jewelry_id`) REFERENCES `core_jewelry` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_bid`
--
-- ORDER BY:  `id`

LOCK TABLES `core_bid` WRITE;
/*!40000 ALTER TABLE `core_bid` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_bid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_blog`
--

DROP TABLE IF EXISTS `core_blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_blog` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` longtext NOT NULL,
  `publication_date` datetime(6) NOT NULL,
  `author_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_blog_author_id_1575e3e5_fk_core_user_id` (`author_id`),
  CONSTRAINT `core_blog_author_id_1575e3e5_fk_core_user_id` FOREIGN KEY (`author_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_blog`
--
-- ORDER BY:  `id`

LOCK TABLES `core_blog` WRITE;
/*!40000 ALTER TABLE `core_blog` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_jewelry`
--

DROP TABLE IF EXISTS `core_jewelry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_jewelry` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `initial_price` decimal(10,2) DEFAULT NULL,
  `preliminary_price` decimal(10,2) DEFAULT NULL,
  `final_price` decimal(10,2) DEFAULT NULL,
  `image_1` varchar(100) DEFAULT NULL,
  `image_2` varchar(100) DEFAULT NULL,
  `image_3` varchar(100) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `seller_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_jewelry_seller_id_c1c7d54b_fk_core_user_id` (`seller_id`),
  CONSTRAINT `core_jewelry_seller_id_c1c7d54b_fk_core_user_id` FOREIGN KEY (`seller_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_jewelry`
--
-- ORDER BY:  `id`

LOCK TABLES `core_jewelry` WRITE;
/*!40000 ALTER TABLE `core_jewelry` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_jewelry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_request`
--

DROP TABLE IF EXISTS `core_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_request` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(30) NOT NULL,
  `preliminary_price` decimal(10,2) DEFAULT NULL,
  `final_price` decimal(10,2) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `jewelry_id` bigint NOT NULL,
  `seller_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_request_jewelry_id_8d39601a_fk_core_jewelry_id` (`jewelry_id`),
  KEY `core_request_seller_id_f349cde9_fk_core_user_id` (`seller_id`),
  CONSTRAINT `core_request_jewelry_id_8d39601a_fk_core_jewelry_id` FOREIGN KEY (`jewelry_id`) REFERENCES `core_jewelry` (`id`),
  CONSTRAINT `core_request_seller_id_f349cde9_fk_core_user_id` FOREIGN KEY (`seller_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_request`
--
-- ORDER BY:  `id`

LOCK TABLES `core_request` WRITE;
/*!40000 ALTER TABLE `core_request` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_transaction`
--

DROP TABLE IF EXISTS `core_transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_transaction` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `fee` decimal(10,2) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `auction_id` bigint DEFAULT NULL,
  `buyer_id` bigint DEFAULT NULL,
  `seller_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auction_id` (`auction_id`),
  KEY `core_transaction_buyer_id_3b9aa6d7_fk_core_user_id` (`buyer_id`),
  KEY `core_transaction_seller_id_a82e96a9_fk_core_user_id` (`seller_id`),
  CONSTRAINT `core_transaction_auction_id_ef0247b2_fk_core_auction_id` FOREIGN KEY (`auction_id`) REFERENCES `core_auction` (`id`),
  CONSTRAINT `core_transaction_buyer_id_3b9aa6d7_fk_core_user_id` FOREIGN KEY (`buyer_id`) REFERENCES `core_user` (`id`),
  CONSTRAINT `core_transaction_seller_id_a82e96a9_fk_core_user_id` FOREIGN KEY (`seller_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_transaction`
--
-- ORDER BY:  `id`

LOCK TABLES `core_transaction` WRITE;
/*!40000 ALTER TABLE `core_transaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user`
--

DROP TABLE IF EXISTS `core_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `role` varchar(10) NOT NULL,
  `email` varchar(254) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `registration_date` datetime(6) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  `jcoin_balance` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user`
--
-- ORDER BY:  `id`

LOCK TABLES `core_user` WRITE;
/*!40000 ALTER TABLE `core_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user_groups`
--

DROP TABLE IF EXISTS `core_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_user_groups_user_id_group_id_c82fcad1_uniq` (`user_id`,`group_id`),
  KEY `core_user_groups_group_id_fe8c697f_fk_auth_group_id` (`group_id`),
  CONSTRAINT `core_user_groups_group_id_fe8c697f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `core_user_groups_user_id_70b4d9b8_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_groups`
--
-- ORDER BY:  `id`

LOCK TABLES `core_user_groups` WRITE;
/*!40000 ALTER TABLE `core_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user_user_permissions`
--

DROP TABLE IF EXISTS `core_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_user_user_permissions_user_id_permission_id_73ea0daa_uniq` (`user_id`,`permission_id`),
  KEY `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` (`permission_id`),
  CONSTRAINT `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `core_user_user_permissions_user_id_085123d3_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_user_permissions`
--
-- ORDER BY:  `id`

LOCK TABLES `core_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `core_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--
-- ORDER BY:  `id`

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--
-- ORDER BY:  `id`

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (1,'admin','logentry'),(2,'auth','permission'),(3,'auth','group'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'core','auction'),(8,'core','jewelry'),(9,'core','user'),(10,'core','transaction'),(11,'core','request'),(12,'core','blog'),(13,'core','bid');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--
-- ORDER BY:  `id`

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (1,'contenttypes','0001_initial','2024-12-18 10:45:20.840132'),(2,'auth','0001_initial','2024-12-18 10:45:21.371674'),(3,'admin','0001_initial','2024-12-18 10:45:21.511282'),(4,'admin','0002_logentry_remove_auto_add','2024-12-18 10:45:21.518478'),(5,'admin','0003_logentry_add_action_flag_choices','2024-12-18 10:45:21.525195'),(6,'contenttypes','0002_remove_content_type_name','2024-12-18 10:45:21.600218'),(7,'auth','0002_alter_permission_name_max_length','2024-12-18 10:45:21.693922'),(8,'auth','0003_alter_user_email_max_length','2024-12-18 10:45:21.712314'),(9,'auth','0004_alter_user_username_opts','2024-12-18 10:45:21.719297'),(10,'auth','0005_alter_user_last_login_null','2024-12-18 10:45:21.772852'),(11,'auth','0006_require_contenttypes_0002','2024-12-18 10:45:21.776974'),(12,'auth','0007_alter_validators_add_error_messages','2024-12-18 10:45:21.784059'),(13,'auth','0008_alter_user_username_max_length','2024-12-18 10:45:21.842207'),(14,'auth','0009_alter_user_last_name_max_length','2024-12-18 10:45:21.900836'),(15,'auth','0010_alter_group_name_max_length','2024-12-18 10:45:21.916462'),(16,'auth','0011_update_proxy_permissions','2024-12-18 10:45:21.924437'),(17,'auth','0012_alter_user_first_name_max_length','2024-12-18 10:45:21.984500'),(18,'core','0001_initial','2024-12-18 10:45:23.151050'),(19,'sessions','0001_initial','2024-12-18 10:45:23.178469');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--
-- ORDER BY:  `session_key`

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jewelry`
--

DROP TABLE IF EXISTS `jewelry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jewelry` (
  `jewelry_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `seller_id` int NOT NULL,
  `initial_price` decimal(10,2) DEFAULT NULL,
  `preliminary_price` decimal(10,2) DEFAULT NULL,
  `final_price` decimal(10,2) DEFAULT NULL,
  `image_1` varchar(255) DEFAULT NULL,
  `image_2` varchar(255) DEFAULT NULL,
  `image_3` varchar(255) DEFAULT NULL,
  `status` varchar(255) NOT NULL,
  PRIMARY KEY (`jewelry_id`),
  KEY `seller_id` (`seller_id`),
  CONSTRAINT `jewelry_ibfk_1` FOREIGN KEY (`seller_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jewelry`
--
-- ORDER BY:  `jewelry_id`

LOCK TABLES `jewelry` WRITE;
/*!40000 ALTER TABLE `jewelry` DISABLE KEYS */;
INSERT INTO `jewelry` (`jewelry_id`, `name`, `description`, `seller_id`, `initial_price`, `preliminary_price`, `final_price`, `image_1`, `image_2`, `image_3`, `status`) VALUES (1,'Diamond Ring','A beautiful diamond ring',4,500.00,550.00,600.00,'ring1.jpg','ring2.jpg','ring3.jpg','approved'),(2,'Gold Necklace','A luxurious gold necklace',4,1000.00,1100.00,1200.00,'necklace1.jpg','necklace2.jpg','necklace3.jpg','approved'),(3,'Silver Bracelet','An elegant silver bracelet',4,200.00,220.00,250.00,'bracelet1.jpg','bracelet2.jpg','bracelet3.jpg','pending');
/*!40000 ALTER TABLE `jewelry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request`
--

DROP TABLE IF EXISTS `request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `request` (
  `request_id` int NOT NULL AUTO_INCREMENT,
  `seller_id` int NOT NULL,
  `jewelry_id` int NOT NULL,
  `status` varchar(255) NOT NULL,
  `preliminary_price` decimal(10,2) DEFAULT NULL,
  `final_price` decimal(10,2) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`request_id`),
  KEY `seller_id` (`seller_id`),
  KEY `jewelry_id` (`jewelry_id`),
  CONSTRAINT `request_ibfk_1` FOREIGN KEY (`seller_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `request_ibfk_2` FOREIGN KEY (`jewelry_id`) REFERENCES `jewelry` (`jewelry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request`
--
-- ORDER BY:  `request_id`

LOCK TABLES `request` WRITE;
/*!40000 ALTER TABLE `request` DISABLE KEYS */;
INSERT INTO `request` (`request_id`, `seller_id`, `jewelry_id`, `status`, `preliminary_price`, `final_price`, `created_at`, `updated_at`) VALUES (1,4,1,'approved',550.00,600.00,'2024-11-20 08:00:00','2024-12-20 08:00:01'),(2,4,2,'final_price_sent',1100.00,1200.00,'2024-11-20 09:00:00','2024-12-20 10:59:59'),(3,4,3,'pending',NULL,NULL,'2024-11-21 10:00:00','2024-12-21 11:00:00');
/*!40000 ALTER TABLE `request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `auction_id` int NOT NULL,
  `buyer_id` int NOT NULL,
  `seller_id` int NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `fee` decimal(10,2) NOT NULL,
  `timestamp` datetime NOT NULL,
  `status` varchar(255) NOT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `auction_id` (`auction_id`),
  KEY `buyer_id` (`buyer_id`),
  KEY `seller_id` (`seller_id`),
  CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`auction_id`) REFERENCES `auction` (`auction_id`),
  CONSTRAINT `transaction_ibfk_2` FOREIGN KEY (`buyer_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `transaction_ibfk_3` FOREIGN KEY (`seller_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--
-- ORDER BY:  `transaction_id`

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `role` varchar(255) NOT NULL,
  `registration_date` datetime NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `profile_picture` varchar(255) DEFAULT NULL,
  `jcoin_balance` decimal(10,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--
-- ORDER BY:  `user_id`

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`user_id`, `username`, `password`, `email`, `first_name`, `last_name`, `role`, `registration_date`, `last_login`, `profile_picture`, `jcoin_balance`) VALUES (1,'admin','$2b$12$DJve53DwH.M/XWJ9Y7/N/ujfxQAQ7vM/sDTfiXhlT.bQONKq3Mh2u','admin@example.com','Admin','User','admin','2023-11-20 00:00:00',NULL,NULL,10000.00),(2,'manager1','$2b$12$DJve53DwH.M/XWJ9Y7/N/ujfxQAQ7vM/sDTfiXhlT.bQONKq3Mh2u','manager1@example.com','Manager','One','manager','2023-11-20 00:00:00',NULL,NULL,5000.00),(3,'staff1','$2b$12$DJve53DwH.M/XWJ9Y7/N/ujfxQAQ7vM/sDTfiXhlT.bQONKq3Mh2u','staff1@example.com','Staff','One','staff','2023-11-20 00:00:00',NULL,NULL,0.00),(4,'seller1','$2b$12$DJve53DwH.M/XWJ9Y7/N/ujfxQAQ7vM/sDTfiXhlT.bQONKq3Mh2u','seller1@example.com','Seller','One','member','2023-11-20 00:00:00',NULL,NULL,100.00),(5,'buyer1','$2b$12$DJve53DwH.M/XWJ9Y7/N/ujfxQAQ7vM/sDTfiXhlT.bQONKq3Mh2u','buyer1@example.com','Buyer','One','member','2023-11-20 00:00:00',NULL,NULL,2000.00),(6,'buyer2','$2b$12$DJve53DwH.M/XWJ9Y7/N/ujfxQAQ7vM/sDTfiXhlT.bQONKq3Mh2u','buyer2@example.com','Buyer','Two','member','2023-11-20 00:00:00',NULL,NULL,3000.00);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-18 21:28:31
