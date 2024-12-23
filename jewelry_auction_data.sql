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
-- Table structure for table `auctions_auction`
--

DROP TABLE IF EXISTS `auctions_auction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auctions_auction` (
  `auction_id` int NOT NULL AUTO_INCREMENT,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `jewelry_id` int NOT NULL,
  `manager_id` int DEFAULT NULL,
  `staff_id` int DEFAULT NULL,
  PRIMARY KEY (`auction_id`),
  KEY `auctions_auction_jewelry_id_8ca17da2_fk_jewelry_j` (`jewelry_id`),
  KEY `auctions_auction_manager_id_77aa1746_fk_users_user_user_id` (`manager_id`),
  KEY `auctions_auction_staff_id_186b347b_fk_users_user_user_id` (`staff_id`),
  CONSTRAINT `auctions_auction_jewelry_id_8ca17da2_fk_jewelry_j` FOREIGN KEY (`jewelry_id`) REFERENCES `jewelry_jewelry` (`jewelry_id`),
  CONSTRAINT `auctions_auction_manager_id_77aa1746_fk_users_user_user_id` FOREIGN KEY (`manager_id`) REFERENCES `users_user` (`user_id`),
  CONSTRAINT `auctions_auction_staff_id_186b347b_fk_users_user_user_id` FOREIGN KEY (`staff_id`) REFERENCES `users_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auctions_auction`
--

LOCK TABLES `auctions_auction` WRITE;
/*!40000 ALTER TABLE `auctions_auction` DISABLE KEYS */;
/*!40000 ALTER TABLE `auctions_auction` ENABLE KEYS */;
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

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add jewelry',7,'add_jewelry'),(26,'Can change jewelry',7,'change_jewelry'),(27,'Can delete jewelry',7,'delete_jewelry'),(28,'Can view jewelry',7,'view_jewelry'),(29,'Can add auction',8,'add_auction'),(30,'Can change auction',8,'change_auction'),(31,'Can delete auction',8,'delete_auction'),(32,'Can view auction',8,'view_auction'),(33,'Can add bid',9,'add_bid'),(34,'Can change bid',9,'change_bid'),(35,'Can delete bid',9,'delete_bid'),(36,'Can view bid',9,'view_bid'),(37,'Can add transaction',10,'add_transaction'),(38,'Can change transaction',10,'change_transaction'),(39,'Can delete transaction',10,'delete_transaction'),(40,'Can view transaction',10,'view_transaction'),(41,'Can add blog',11,'add_blog'),(42,'Can change blog',11,'change_blog'),(43,'Can delete blog',11,'delete_blog'),(44,'Can view blog',11,'view_blog'),(45,'Can add fee configuration',12,'add_feeconfiguration'),(46,'Can change fee configuration',12,'change_feeconfiguration'),(47,'Can delete fee configuration',12,'delete_feeconfiguration'),(48,'Can view fee configuration',12,'view_feeconfiguration'),(49,'Can add j coin management',13,'add_jcoinmanagement'),(50,'Can change j coin management',13,'change_jcoinmanagement'),(51,'Can delete j coin management',13,'delete_jcoinmanagement'),(52,'Can view j coin management',13,'view_jcoinmanagement');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bids_bid`
--

DROP TABLE IF EXISTS `bids_bid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bids_bid` (
  `bid_id` int NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `auction_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`bid_id`),
  KEY `bids_bid_auction_id_ecc5c9f8_fk_auctions_auction_auction_id` (`auction_id`),
  KEY `bids_bid_user_id_5ba34cc3_fk_users_user_user_id` (`user_id`),
  CONSTRAINT `bids_bid_auction_id_ecc5c9f8_fk_auctions_auction_auction_id` FOREIGN KEY (`auction_id`) REFERENCES `auctions_auction` (`auction_id`),
  CONSTRAINT `bids_bid_user_id_5ba34cc3_fk_users_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bids_bid`
--

LOCK TABLES `bids_bid` WRITE;
/*!40000 ALTER TABLE `bids_bid` DISABLE KEYS */;
/*!40000 ALTER TABLE `bids_bid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_blog`
--

DROP TABLE IF EXISTS `blog_blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_blog` (
  `blog_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` longtext NOT NULL,
  `publication_date` datetime(6) NOT NULL,
  `author_id` int NOT NULL,
  PRIMARY KEY (`blog_id`),
  KEY `blog_blog_author_id_8791af69_fk_users_user_user_id` (`author_id`),
  CONSTRAINT `blog_blog_author_id_8791af69_fk_users_user_user_id` FOREIGN KEY (`author_id`) REFERENCES `users_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_blog`
--

LOCK TABLES `blog_blog` WRITE;
/*!40000 ALTER TABLE `blog_blog` DISABLE KEYS */;
INSERT INTO `blog_blog` (`blog_id`, `title`, `content`, `publication_date`, `author_id`) VALUES (1,'Caring for Diamond Jewelry','Tips on maintaining the sparkle of your diamond jewelry...','2023-12-20 00:00:00.000000',1),(2,'The Evolution of Gold Jewelry','A journey through the history of gold jewelry designs...','2023-12-17 00:00:00.000000',1),(3,'Understanding Gemstones','An informative guide about different types of gemstones...','2023-12-13 00:00:00.000000',1),(4,'Latest Trends in Jewelry','Stay updated with the latest trends in the world of jewelry...','2023-12-08 00:00:00.000000',1);
/*!40000 ALTER TABLE `blog_blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_feeconfiguration`
--

DROP TABLE IF EXISTS `core_feeconfiguration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_feeconfiguration` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fee_rate` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_feeconfiguration`
--

LOCK TABLES `core_feeconfiguration` WRITE;
/*!40000 ALTER TABLE `core_feeconfiguration` DISABLE KEYS */;
INSERT INTO `core_feeconfiguration` (`id`, `fee_rate`) VALUES (1,0.05);
/*!40000 ALTER TABLE `core_feeconfiguration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_jcoinmanagement`
--

DROP TABLE IF EXISTS `core_jcoinmanagement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_jcoinmanagement` (
  `id` int NOT NULL AUTO_INCREMENT,
  `total_jcoin` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_jcoinmanagement`
--

LOCK TABLES `core_jcoinmanagement` WRITE;
/*!40000 ALTER TABLE `core_jcoinmanagement` DISABLE KEYS */;
INSERT INTO `core_jcoinmanagement` (`id`, `total_jcoin`) VALUES (1,100000.00);
/*!40000 ALTER TABLE `core_jcoinmanagement` ENABLE KEYS */;
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
  KEY `django_admin_log_user_id_c564eba6_fk_users_user_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`user_id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

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

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (1,'admin','logentry'),(8,'auctions','auction'),(3,'auth','group'),(2,'auth','permission'),(9,'bids','bid'),(11,'blog','blog'),(4,'contenttypes','contenttype'),(12,'core','feeconfiguration'),(13,'core','jcoinmanagement'),(7,'jewelry','jewelry'),(5,'sessions','session'),(10,'transactions','transaction'),(6,'users','user');
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
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (1,'contenttypes','0001_initial','2024-12-23 11:24:14.894689'),(2,'contenttypes','0002_remove_content_type_name','2024-12-23 11:24:14.953390'),(3,'auth','0001_initial','2024-12-23 11:24:15.192113'),(4,'auth','0002_alter_permission_name_max_length','2024-12-23 11:24:15.248063'),(5,'auth','0003_alter_user_email_max_length','2024-12-23 11:24:15.254570'),(6,'auth','0004_alter_user_username_opts','2024-12-23 11:24:15.260028'),(7,'auth','0005_alter_user_last_login_null','2024-12-23 11:24:15.265895'),(8,'auth','0006_require_contenttypes_0002','2024-12-23 11:24:15.269183'),(9,'auth','0007_alter_validators_add_error_messages','2024-12-23 11:24:15.273928'),(10,'auth','0008_alter_user_username_max_length','2024-12-23 11:24:15.279105'),(11,'auth','0009_alter_user_last_name_max_length','2024-12-23 11:24:15.284936'),(12,'auth','0010_alter_group_name_max_length','2024-12-23 11:24:15.299522'),(13,'auth','0011_update_proxy_permissions','2024-12-23 11:24:15.305262'),(14,'auth','0012_alter_user_first_name_max_length','2024-12-23 11:24:15.311027'),(15,'users','0001_initial','2024-12-23 11:24:15.640847'),(16,'admin','0001_initial','2024-12-23 11:24:15.772089'),(17,'admin','0002_logentry_remove_auto_add','2024-12-23 11:24:15.778604'),(18,'admin','0003_logentry_add_action_flag_choices','2024-12-23 11:24:15.786827'),(19,'jewelry','0001_initial','2024-12-23 11:24:15.805817'),(20,'auctions','0001_initial','2024-12-23 11:24:15.823657'),(21,'auctions','0002_initial','2024-12-23 11:24:15.880737'),(22,'auctions','0003_initial','2024-12-23 11:24:16.005000'),(23,'bids','0001_initial','2024-12-23 11:24:16.080693'),(24,'bids','0002_initial','2024-12-23 11:24:16.179170'),(25,'blog','0001_initial','2024-12-23 11:24:16.199378'),(26,'blog','0002_initial','2024-12-23 11:24:16.261578'),(27,'core','0001_initial','2024-12-23 11:24:16.298438'),(28,'jewelry','0002_initial','2024-12-23 11:24:16.362146'),(29,'sessions','0001_initial','2024-12-23 11:24:16.392786'),(30,'transactions','0001_initial','2024-12-23 11:24:16.485625'),(31,'transactions','0002_initial','2024-12-23 11:24:16.617203');
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

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jewelry_jewelry`
--

DROP TABLE IF EXISTS `jewelry_jewelry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jewelry_jewelry` (
  `jewelry_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `initial_price` decimal(10,2) NOT NULL,
  `preliminary_price` decimal(10,2) DEFAULT NULL,
  `final_price` decimal(10,2) DEFAULT NULL,
  `image_1` varchar(100) NOT NULL,
  `image_2` varchar(100) DEFAULT NULL,
  `image_3` varchar(100) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `owner_id` int NOT NULL,
  PRIMARY KEY (`jewelry_id`),
  KEY `jewelry_jewelry_owner_id_2089ac34_fk_users_user_user_id` (`owner_id`),
  CONSTRAINT `jewelry_jewelry_owner_id_2089ac34_fk_users_user_user_id` FOREIGN KEY (`owner_id`) REFERENCES `users_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jewelry_jewelry`
--

LOCK TABLES `jewelry_jewelry` WRITE;
/*!40000 ALTER TABLE `jewelry_jewelry` DISABLE KEYS */;
INSERT INTO `jewelry_jewelry` (`jewelry_id`, `name`, `description`, `initial_price`, `preliminary_price`, `final_price`, `image_1`, `image_2`, `image_3`, `status`, `owner_id`) VALUES (1,'Elegant Diamond Ring','A stunning ring featuring a brilliant-cut diamond.',1500.00,NULL,NULL,'jewelry/Elegant_Diamond_Ring.jpg','','','PENDING',4),(2,'Classic Gold Bangle','A timeless bangle crafted from 18k gold.',800.00,NULL,NULL,'jewelry/Classic_Gold_Bangle.jpg','','','APPROVED',4),(3,'Stylish Silver Pendant','A contemporary pendant made with sterling silver.',300.00,NULL,NULL,'jewelry/Stylish_Silver_Pendant.jpg','','','REJECTED',4),(4,'Exquisite Pearl Earrings','Elegant earrings with high-quality pearls.',950.00,NULL,NULL,'jewelry/Exquisite_Pearl_Earrings.jpg','','','APPROVED',4),(5,'Luxurious Emerald Necklace','A necklace featuring a deep-green emerald.',2500.00,NULL,NULL,'jewelry/Luxurious_Emerald_Necklace.jpg','','','PENDING',4),(6,'Modern Titanium Watch','A sleek, modern watch made with durable titanium.',1200.00,NULL,NULL,'jewelry/Modern_Titanium_Watch.jpg','','','APPROVED',4),(7,'Antique Ruby Brooch','An antique brooch adorned with a vibrant ruby.',700.00,NULL,NULL,'jewelry/Antique_Ruby_Brooch.jpg','','','PENDING',4),(8,'Charming Sapphire Ring','A charming ring featuring a blue sapphire.',450.00,NULL,NULL,'jewelry/Charming_Sapphire_Ring.jpg','','','APPROVED',4),(9,'Delicate Amethyst Bracelet','A delicate bracelet with amethyst stones.',600.00,NULL,NULL,'jewelry/Delicate_Amethyst_Bracelet.jpg','','','REJECTED',4),(10,'Unique Opal Pendant','A unique pendant with a colorful opal gemstone.',550.00,NULL,NULL,'jewelry/Unique_Opal_Pendant.jpg','','','APPROVED',4);
/*!40000 ALTER TABLE `jewelry_jewelry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions_transaction`
--

DROP TABLE IF EXISTS `transactions_transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions_transaction` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `fee` decimal(10,2) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `auction_id` int NOT NULL,
  `jewelry_owner_id` int NOT NULL,
  `winning_bidder_id` int NOT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `transactions_transac_auction_id_28df9b54_fk_auctions_` (`auction_id`),
  KEY `transactions_transac_jewelry_owner_id_4d2c2fb5_fk_users_use` (`jewelry_owner_id`),
  KEY `transactions_transac_winning_bidder_id_43415369_fk_users_use` (`winning_bidder_id`),
  CONSTRAINT `transactions_transac_auction_id_28df9b54_fk_auctions_` FOREIGN KEY (`auction_id`) REFERENCES `auctions_auction` (`auction_id`),
  CONSTRAINT `transactions_transac_jewelry_owner_id_4d2c2fb5_fk_users_use` FOREIGN KEY (`jewelry_owner_id`) REFERENCES `users_user` (`user_id`),
  CONSTRAINT `transactions_transac_winning_bidder_id_43415369_fk_users_use` FOREIGN KEY (`winning_bidder_id`) REFERENCES `users_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions_transaction`
--

LOCK TABLES `transactions_transaction` WRITE;
/*!40000 ALTER TABLE `transactions_transaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `transactions_transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `role` varchar(20) NOT NULL,
  `registration_date` datetime(6) NOT NULL,
  `profile_picture` varchar(200) DEFAULT NULL,
  `jcoin_balance` decimal(10,2) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` (`password`, `last_login`, `is_superuser`, `user_id`, `username`, `first_name`, `last_name`, `role`, `registration_date`, `profile_picture`, `jcoin_balance`, `is_active`, `is_staff`) VALUES ('pbkdf2_sha256$390000$l5hMgx595lOM$L7HCMB4sF+D15c9tx4/jkRx+q/j8RvapP/XU9/J6VjE=',NULL,1,1,'admin','Admin','User','ADMIN','2023-12-23 00:00:00.000000',NULL,0.00,1,1),('pbkdf2_sha256$390000$l5hMgx595lOM$L7HCMB4sF+D15c9tx4/jkRx+q/j8RvapP/XU9/J6VjE=',NULL,0,2,'manager1','Manager','One','MANAGER','2023-12-23 00:00:00.000000',NULL,0.00,1,1),('pbkdf2_sha256$390000$l5hMgx595lOM$L7HCMB4sF+D15c9tx4/jkRx+q/j8RvapP/XU9/J6VjE=',NULL,0,3,'staff1','Staff','One','STAFF','2023-12-23 00:00:00.000000',NULL,0.00,1,1),('pbkdf2_sha256$390000$l5hMgx595lOM$L7HCMB4sF+D15c9tx4/jkRx+q/j8RvapP/XU9/J6VjE=',NULL,0,4,'member1','Member','One','MEMBER','2023-12-23 00:00:00.000000',NULL,1000.00,1,0);
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_groups`
--

DROP TABLE IF EXISTS `users_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_groups_user_id_group_id_b88eab82_uniq` (`user_id`,`group_id`),
  KEY `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_groups`
--

LOCK TABLES `users_user_groups` WRITE;
/*!40000 ALTER TABLE `users_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_user_permissions`
--

DROP TABLE IF EXISTS `users_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_user_permissions_user_id_permission_id_43338c45_uniq` (`user_id`,`permission_id`),
  KEY `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_user_user_perm_user_id_20aca447_fk_users_use` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_user_permissions`
--

LOCK TABLES `users_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-23 19:57:24
