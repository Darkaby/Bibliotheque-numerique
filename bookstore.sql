

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `bookstore`
--

-- --------------------------------------------------------

--
-- Structure de la table `author`
--

DROP TABLE IF EXISTS `author`;
CREATE TABLE IF NOT EXISTS `author` (
  `A_ID` int(11) NOT NULL,
  `A_FNAME` varchar(45) COLLATE utf8_bin NOT NULL,
  `A_LNAME` varchar(45) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`A_ID`),
  UNIQUE KEY `A_ID` (`A_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Structure de la table `books`
--

DROP TABLE IF EXISTS `books`;
CREATE TABLE IF NOT EXISTS `books` (
  `B_ID` int(11) NOT NULL,
  `B_TITLE` varchar(45) COLLATE utf8_bin NOT NULL,
  `B_A_ID` int(11) NOT NULL,
  `B_PUBLISHER` varchar(45) COLLATE utf8_bin NOT NULL,
  `B_PUB_DATE` date NOT NULL,
  `B_SUBJECT` varchar(45) COLLATE utf8_bin NOT NULL,
  `B_UNIT_PRIZE` int(11) NOT NULL,
  `B_STOCK` int(11) NOT NULL,
  PRIMARY KEY (`B_ID`),
  UNIQUE KEY `B_ID` (`B_ID`),
  KEY `B_A_ID` (`B_A_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Structure de la table `customers`
--

DROP TABLE IF EXISTS `customers`;
CREATE TABLE IF NOT EXISTS `customers` (
  `C_ID` int(11) NOT NULL,
  `C_NAME` varchar(45) COLLATE utf8_bin NOT NULL,
  `C_ADD` varchar(45) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`C_ID`),
  UNIQUE KEY `C_ID` (`C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Structure de la table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
CREATE TABLE IF NOT EXISTS `reservation` (
  `R_ID` int(11) NOT NULL,
  `R_C_ID` int(11) NOT NULL,
  `R_C_NAME` varchar(45) COLLATE utf8_bin NOT NULL,
  `R_B_ID` int(11) NOT NULL,
  `R_B_TITLE` varchar(45) COLLATE utf8_bin NOT NULL,
  `R_B_QUANTITY` int(11) NOT NULL,
  PRIMARY KEY (`R_ID`),
  UNIQUE KEY `R_ID` (`R_ID`),
  KEY `R_B_ID` (`R_B_ID`),
  KEY `R_C_ID` (`R_C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `books_ibfk_1` FOREIGN KEY (`B_A_ID`) REFERENCES `author` (`A_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`R_B_ID`) REFERENCES `books` (`B_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`R_C_ID`) REFERENCES `customers` (`C_ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
