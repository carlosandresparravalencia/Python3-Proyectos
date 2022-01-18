-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 18-01-2022 a las 08:31:30
-- Versión del servidor: 10.4.10-MariaDB
-- Versión de PHP: 7.4.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `patentescarlos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clase_patente`
--

DROP TABLE IF EXISTS `clase_patente`;
CREATE TABLE IF NOT EXISTS `clase_patente` (
  `id` varchar(7) COLLATE utf8mb4_spanish_ci NOT NULL,
  `nombre_patente` varchar(70) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `descripcion` varchar(100) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_patente` (`nombre_patente`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `clase_patente`
--

INSERT INTO `clase_patente` (`id`, `nombre_patente`, `descripcion`) VALUES
('ABZZ099', 'Carga inalámbrica', 'Teléfono'),
('ABCD009', 'Bombilla', 'Lámpara incandescente');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
