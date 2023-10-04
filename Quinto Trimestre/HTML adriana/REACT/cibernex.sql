-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-09-2023 a las 07:01:21
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cibernex`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbdetallefactura`
--

CREATE TABLE `tbdetallefactura` (
  `detFacId` int(11) NOT NULL,
  `facId` int(11) DEFAULT NULL,
  `resId` int(11) DEFAULT NULL,
  `serID` int(11) DEFAULT NULL,
  `detFacSubTotal` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbdetallefactura`
--

INSERT INTO `tbdetallefactura` (`detFacId`, `facId`, `resId`, `serID`, `detFacSubTotal`) VALUES
(1, 1, 10011, 1, NULL),
(2, 2, 10012, 2, NULL),
(3, 3, 10013, 3, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbfactura`
--

CREATE TABLE `tbfactura` (
  `facId` int(11) NOT NULL,
  `facFecha` date DEFAULT NULL,
  `facTotal` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbfactura`
--

INSERT INTO `tbfactura` (`facId`, `facFecha`, `facTotal`) VALUES
(1, '2023-05-21', NULL),
(2, '2023-05-22', NULL),
(3, '2023-05-23', NULL),
(4, '2023-05-24', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbhabitacion`
--

CREATE TABLE `tbhabitacion` (
  `habNumero` int(11) NOT NULL,
  `habEstado` varchar(20) DEFAULT NULL,
  `habCaracteristicas` varchar(200) DEFAULT NULL,
  `habCostoBase` decimal(10,2) DEFAULT NULL,
  `habCapacidad` int(11) DEFAULT NULL,
  `habNroCamaSensilla` int(11) DEFAULT NULL,
  `habNroCamaDoble` int(11) DEFAULT NULL,
  `habNroCamarotes` int(11) DEFAULT NULL,
  `tipHabId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbhabitacion`
--

INSERT INTO `tbhabitacion` (`habNumero`, `habEstado`, `habCaracteristicas`, `habCostoBase`, `habCapacidad`, `habNroCamaSensilla`, `habNroCamaDoble`, `habNroCamarotes`, `tipHabId`) VALUES
(1, 'Disponible', 'Habitacion con una cama sencilla', 120000.00, 1, 1, 0, 0, 1),
(2, 'Ocupado', 'Habitacion con una cama sencilla', 120000.00, 1, 1, 0, 0, 1),
(3, 'Disponible', 'Habitacion con dos camas sencillas', 250000.00, 2, 2, 0, 0, 2),
(4, 'Disponible', 'Habitacion con una cama doble', 250000.00, 2, 0, 2, 0, 2),
(5, 'Disponible', 'Habitacion con una cama sencilla y dos camas dobles', 350000.00, 3, 1, 2, 0, 3),
(6, 'Ocupado', 'Habitacion con una cama sencilla y un camarote', 350000.00, 3, 1, 0, 1, 3),
(7, 'Disponible', 'Habitacion con dos camas sencillas y una cama doble', 500000.00, 4, 2, 1, 0, 4),
(8, 'Disponible', 'Habitacion con dos camarotes', 500000.00, 4, 0, 0, 2, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbproductos`
--

CREATE TABLE `tbproductos` (
  `proId` int(11) NOT NULL,
  `proNombre` varchar(50) DEFAULT NULL,
  `proCosto` decimal(10,2) DEFAULT NULL,
  `tipProId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbproductos`
--

INSERT INTO `tbproductos` (`proId`, `proNombre`, `proCosto`, `tipProId`) VALUES
(1, 'ColaCoca', 3000.00, 1),
(2, 'Tamal', 8000.00, 2),
(3, 'Quipitos', 1500.00, 3),
(4, 'Agua mineral', 2000.00, 1),
(5, 'Galletas', 5000.00, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbreserva`
--

CREATE TABLE `tbreserva` (
  `resId` int(11) NOT NULL,
  `usuDocumento` int(11) DEFAULT NULL,
  `resEstado` varchar(20) DEFAULT NULL,
  `resCantidadAdultos` int(11) DEFAULT NULL,
  `resCantidadNiños` int(11) DEFAULT NULL,
  `resFechaIngreso` date DEFAULT NULL,
  `resFechaSalida` date DEFAULT NULL,
  `habNumero` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbreserva`
--

INSERT INTO `tbreserva` (`resId`, `usuDocumento`, `resEstado`, `resCantidadAdultos`, `resCantidadNiños`, `resFechaIngreso`, `resFechaSalida`, `habNumero`) VALUES
(10011, 2010234, 'Anulada', 1, 1, '2024-03-11', '2025-03-22', 1),
(10012, 2010235, 'Aprovada', 2, 0, '2024-03-12', '2025-03-21', 2),
(10013, 2010236, 'Anulada', 3, 0, '2024-03-13', '2025-03-23', 3),
(10014, 2010237, 'Aprovada', 2, 2, '2024-03-14', '2025-03-24', 4),
(10015, 2010238, 'Pendiente', 2, 0, '2024-03-15', '2025-03-25', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbservicios`
--

CREATE TABLE `tbservicios` (
  `serID` int(11) NOT NULL,
  `serNombre` varchar(50) DEFAULT NULL,
  `serDescripcion` varchar(100) DEFAULT NULL,
  `serCosto` decimal(10,2) DEFAULT NULL,
  `tipSerId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbservicios`
--

INSERT INTO `tbservicios` (`serID`, `serNombre`, `serDescripcion`, `serCosto`, `tipSerId`) VALUES
(1, 'Desayuno Buffet', 'Delicioso desayuno tipo buffet', 10000.00, 1),
(2, 'Masaje Relajante', 'Masaje relajante de cuerpo completo', 20000.00, 2),
(3, 'Transporte al Aeropuerto', 'Traslado en vehiculo privado al aeropuerto', 30000.00, 3),
(4, 'Acceso al Spa', 'Acceso a todas las instalaciones del spa', 25000.00, 2),
(5, 'Servicio de Habitacion', 'Entrega de comida y bebida en la habitacion', 15000.00, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbtipohabitacion`
--

CREATE TABLE `tbtipohabitacion` (
  `tipHabId` int(11) NOT NULL,
  `tipHabTipo` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbtipohabitacion`
--

INSERT INTO `tbtipohabitacion` (`tipHabId`, `tipHabTipo`) VALUES
(1, 'Individual'),
(2, 'Doble'),
(3, 'Triple'),
(4, 'Quad');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbtipoproducto`
--

CREATE TABLE `tbtipoproducto` (
  `tipProId` int(11) NOT NULL,
  `tipProCategoria` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbtipoproducto`
--

INSERT INTO `tbtipoproducto` (`tipProId`, `tipProCategoria`) VALUES
(1, 'Bebidas'),
(2, 'Comestibles'),
(3, 'Dulces'),
(4, 'Bebidas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbtiposervicio`
--

CREATE TABLE `tbtiposervicio` (
  `tipSerId` int(11) NOT NULL,
  `tipSerNombre` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbtiposervicio`
--

INSERT INTO `tbtiposervicio` (`tipSerId`, `tipSerNombre`) VALUES
(1, 'Alimentacion'),
(2, 'Bienestar'),
(3, 'Transporte'),
(4, 'Entretenimiento'),
(5, 'Transporte privado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbtipousuario`
--

CREATE TABLE `tbtipousuario` (
  `tipUsuId` int(11) NOT NULL,
  `tipUsuRol` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbtipousuario`
--

INSERT INTO `tbtipousuario` (`tipUsuId`, `tipUsuRol`) VALUES
(1, 'Admin'),
(2, 'Recepcion'),
(3, 'Cliente'),
(4, 'Gerente'),
(5, 'Seguridad');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbusuarios`
--

CREATE TABLE `tbusuarios` (
  `usuDocumento` int(11) NOT NULL,
  `usuNombre` varchar(50) DEFAULT NULL,
  `usuApellido` varchar(50) DEFAULT NULL,
  `usuEmail` varchar(50) DEFAULT NULL,
  `usuTelefono` varchar(15) DEFAULT NULL,
  `usuGenero` varchar(20) DEFAULT NULL,
  `usuContraseña` varchar(50) DEFAULT NULL,
  `usuEstado` varchar(20) DEFAULT NULL,
  `tipUsuId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbusuarios`
--

INSERT INTO `tbusuarios` (`usuDocumento`, `usuNombre`, `usuApellido`, `usuEmail`, `usuTelefono`, `usuGenero`, `usuContraseña`, `usuEstado`, `tipUsuId`) VALUES
(1, '2', 'd', '3', '3', 'usu', '3', '', 2),
(2, 'J', 'M', 'M', '305', 'M', 'J', 'A', 2),
(2010234, 'Fabian', 'Lombardi', 'fl@.com', '3133248001', 'Masculino', 'fl013', 'Activo', 3),
(2010235, 'Maria', 'Lopez', 'ml@.com', '3133248002', 'Femenino', 'ml023', 'Activo', 3),
(2010236, 'Gabriele', 'Gomez', 'gg@.com', '3133248003', 'Masculino', 'gg033', 'Activo', 3),
(2010237, 'Daniel', 'Mancini', 'dm@.com', '3133248004', 'Masculino', 'dm043', 'Inactivo', 3),
(2010238, 'Laura', 'Ruiz', 'lr@.com', '3133248005', 'Femenino', 'lr052', 'Activo', 2),
(2010239, 'Valentina', 'Martinez', 'vm@.com', '3133248006', 'Masculino', 'vm062', 'Inactivo', 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tbdetallefactura`
--
ALTER TABLE `tbdetallefactura`
  ADD PRIMARY KEY (`detFacId`),
  ADD KEY `facId` (`facId`),
  ADD KEY `resId` (`resId`),
  ADD KEY `serID` (`serID`);

--
-- Indices de la tabla `tbfactura`
--
ALTER TABLE `tbfactura`
  ADD PRIMARY KEY (`facId`);

--
-- Indices de la tabla `tbhabitacion`
--
ALTER TABLE `tbhabitacion`
  ADD PRIMARY KEY (`habNumero`),
  ADD KEY `tipHabId` (`tipHabId`);

--
-- Indices de la tabla `tbproductos`
--
ALTER TABLE `tbproductos`
  ADD PRIMARY KEY (`proId`),
  ADD KEY `tipProId` (`tipProId`);

--
-- Indices de la tabla `tbreserva`
--
ALTER TABLE `tbreserva`
  ADD PRIMARY KEY (`resId`),
  ADD KEY `usuDocumento` (`usuDocumento`),
  ADD KEY `habNumero` (`habNumero`);

--
-- Indices de la tabla `tbservicios`
--
ALTER TABLE `tbservicios`
  ADD PRIMARY KEY (`serID`),
  ADD KEY `tipSerId` (`tipSerId`);

--
-- Indices de la tabla `tbtipohabitacion`
--
ALTER TABLE `tbtipohabitacion`
  ADD PRIMARY KEY (`tipHabId`);

--
-- Indices de la tabla `tbtipoproducto`
--
ALTER TABLE `tbtipoproducto`
  ADD PRIMARY KEY (`tipProId`);

--
-- Indices de la tabla `tbtiposervicio`
--
ALTER TABLE `tbtiposervicio`
  ADD PRIMARY KEY (`tipSerId`);

--
-- Indices de la tabla `tbtipousuario`
--
ALTER TABLE `tbtipousuario`
  ADD PRIMARY KEY (`tipUsuId`);

--
-- Indices de la tabla `tbusuarios`
--
ALTER TABLE `tbusuarios`
  ADD PRIMARY KEY (`usuDocumento`),
  ADD KEY `tipUsuId` (`tipUsuId`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tbdetallefactura`
--
ALTER TABLE `tbdetallefactura`
  MODIFY `detFacId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tbfactura`
--
ALTER TABLE `tbfactura`
  MODIFY `facId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tbdetallefactura`
--
ALTER TABLE `tbdetallefactura`
  ADD CONSTRAINT `tbdetallefactura_ibfk_1` FOREIGN KEY (`facId`) REFERENCES `tbfactura` (`facId`),
  ADD CONSTRAINT `tbdetallefactura_ibfk_2` FOREIGN KEY (`resId`) REFERENCES `tbreserva` (`resId`),
  ADD CONSTRAINT `tbdetallefactura_ibfk_3` FOREIGN KEY (`serID`) REFERENCES `tbservicios` (`serID`);

--
-- Filtros para la tabla `tbhabitacion`
--
ALTER TABLE `tbhabitacion`
  ADD CONSTRAINT `tbhabitacion_ibfk_1` FOREIGN KEY (`tipHabId`) REFERENCES `tbtipohabitacion` (`tipHabId`);

--
-- Filtros para la tabla `tbproductos`
--
ALTER TABLE `tbproductos`
  ADD CONSTRAINT `tbproductos_ibfk_1` FOREIGN KEY (`tipProId`) REFERENCES `tbtipoproducto` (`tipProId`);

--
-- Filtros para la tabla `tbreserva`
--
ALTER TABLE `tbreserva`
  ADD CONSTRAINT `tbreserva_ibfk_1` FOREIGN KEY (`usuDocumento`) REFERENCES `tbusuarios` (`usuDocumento`),
  ADD CONSTRAINT `tbreserva_ibfk_2` FOREIGN KEY (`habNumero`) REFERENCES `tbhabitacion` (`habNumero`);

--
-- Filtros para la tabla `tbservicios`
--
ALTER TABLE `tbservicios`
  ADD CONSTRAINT `tbservicios_ibfk_1` FOREIGN KEY (`tipSerId`) REFERENCES `tbtiposervicio` (`tipSerId`);

--
-- Filtros para la tabla `tbusuarios`
--
ALTER TABLE `tbusuarios`
  ADD CONSTRAINT `tbusuarios_ibfk_1` FOREIGN KEY (`tipUsuId`) REFERENCES `tbtipousuario` (`tipUsuId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
