--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `reviews` (
  `place_id` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  `text` varchar(1024) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`place_id`) REFERENCES `places` (`id`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES 
('821a55f4-7d82-47d9-b54c-a76916479502','821a55f4-7d82-47d9-b54c-a76916479582','nice spot','821a55f4-7d82-47d9-b54c-a76916469599','2017-03-25 19:44:42','2017-03-25 19:44:42'),
('821a55f4-7d82-47d9-b54c-a76916479602','821a55f4-7d82-47d9-b54c-a76916479578','good customer service','821a55f4-7d82-47d9-b54c-a76916469888','2017-03-25 19:44:42','2017-03-25 19:44:42');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;