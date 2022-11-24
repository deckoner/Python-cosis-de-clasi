DROP SCHEMA IF EXISTS `examen1` ;
CREATE SCHEMA IF NOT EXISTS `examen1` DEFAULT CHARACTER SET latin1 COLLATE latin1_spanish_ci;
USE `examen1` ;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;

CREATE TABLE `productos` (
	`codigo` varchar(5) NOT NULL,
	`nombre` varchar(50) NOT NULL,
	`precio` float NOT NULL,
	`disponible` int DEFAULT 0,
    `imagen` blob NULL,
	PRIMARY KEY (`codigo`)
) ENGINE = InnoDB AUTO_INCREMENT = 10 DEFAULT CHARACTER SET = latin1 COLLATE = latin1_spanish_ci;

INSERT INTO `productos` ( `codigo`,`nombre`, `precio`, `disponible`)
VALUES
	('LIM33','LIMONES',1.89,1),
	('NAR44','NARANJAS',1.69,0),
	('PLT32','PLATANOS',1.75,1),
	('CHORI','CHORIZO',3.25,0),
	('JAM67','JAMON',4.21,1),
	('SALM1','SALMON',12.05,1),
	('BOLL5','BOLLERIA',2.1,1);

COMMIT;