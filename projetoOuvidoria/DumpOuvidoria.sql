CREATE DATABASE  IF NOT EXISTS `ouvidoria` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ouvidoria`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ouvidoria
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `manifestacoes`
--

DROP TABLE IF EXISTS `manifestacoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manifestacoes` (
  `codigo` int NOT NULL AUTO_INCREMENT,
  `avaliacao` tinyint DEFAULT NULL,
  `tipo` enum('Sugestao','Elogio','Reclamacao') NOT NULL,
  `descricao_manifestacao` text NOT NULL,
  `data_hora` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`codigo`),
  CONSTRAINT `manifestacoes_chk_1` CHECK ((`avaliacao` between 1 and 5))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manifestacoes`
--

LOCK TABLES `manifestacoes` WRITE;
/*!40000 ALTER TABLE `manifestacoes` DISABLE KEYS */;
INSERT INTO `manifestacoes` VALUES (1,5,'Elogio','Ótimo atendimento, fui muito bem tratado e meu problema foi resolvido rapidamente.','2025-03-28 16:46:58'),(2,3,'Reclamacao','O atendimento foi mediano, demorou um pouco para responderem, mas resolveram meu problema.','2025-03-28 16:46:58'),(3,1,'Reclamacao','Péssimo serviço! Estou esperando uma resposta há mais de uma semana e nada até agora.','2025-03-28 16:46:58'),(4,4,'Sugestao','Bom atendimento, mas poderia ser um pouco mais rápido. No geral, foi uma boa experiência.','2025-03-28 16:46:58'),(5,2,'Elogio','Não gostei do suporte, foram educados, mas não resolveram meu problema corretamente.','2025-03-28 16:46:58'),(6,5,'Elogio','Atendimente incrivel, super recomendo','2025-03-28 18:16:01'),(7,4,'Elogio','Gostei','2025-03-29 17:06:33'),(8,2,'Elogio','.','2025-03-29 17:20:51'),(9,4,'Elogio','nada a comentar','2025-03-29 17:22:31');
/*!40000 ALTER TABLE `manifestacoes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-01 22:35:26
