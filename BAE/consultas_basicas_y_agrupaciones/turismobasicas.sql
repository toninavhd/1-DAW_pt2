-- Dump File
--
-- Database is ported from MS Access
----------------------------------------------------------
-- Program Version 3.0.148

USE [master]
go
IF EXISTS (SELECT * FROM master.dbo.sysdatabases WHERE name = N'turismobasicas') ALTER DATABASE [turismobasicas] SET SINGLE_USER With ROLLBACK IMMEDIATE
IF EXISTS (SELECT * FROM master.dbo.sysdatabases WHERE name = N'turismobasicas') DROP DATABASE [turismobasicas]
IF NOT EXISTS (SELECT * FROM master.dbo.sysdatabases WHERE name = N'turismobasicas') CREATE DATABASE [turismobasicas]
go
USE [turismobasicas]

--
-- Table structure for table 'DatosTuristas'
--

IF object_id('DatosTuristas', 'U') IS NOT NULL DROP TABLE [DatosTuristas]
go

CREATE TABLE [DatosTuristas] (
  [Id] INT NOT NULL, 
  [grupoedad] VARCHAR(255), 
  [periodo] INT, 
  [sexo] VARCHAR(255), 
  [pais] VARCHAR(255), 
  [turistas] numeric(10,0)
)
GO

--
-- Dumping data for table 'DatosTuristas'
--

INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (1, 'De 16 a 24 años', 2013, 'Hombres', 'Alemania', 22152)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (2, 'De 16 a 24 años', 2013, 'Hombres', 'Bélgica', 2134)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (3, 'De 16 a 24 años', 2013, 'Hombres', 'España', 23091)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (4, 'De 16 a 24 años', 2013, 'Hombres', 'Francia', 2256)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (5, 'De 16 a 24 años', 2013, 'Hombres', 'Holanda', 8000)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (6, 'De 16 a 24 años', 2013, 'Hombres', 'Irlanda', 5265)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (7, 'De 16 a 24 años', 2013, 'Hombres', 'Italia', 2996)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (8, 'De 16 a 24 años', 2013, 'Hombres', 'Países Nórdicos', 4266)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (9, 'De 16 a 24 años', 2013, 'Hombres', 'Reino Unido', 35044)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (10, 'De 16 a 24 años', 2013, 'Hombres', 'Suiza', 3207)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (11, 'De 16 a 24 años', 2013, 'Hombres', 'Otros países', 5377)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (12, 'De 16 a 24 años', 2012, 'Hombres', 'Alemania', 22414)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (13, 'De 16 a 24 años', 2012, 'Hombres', 'Bélgica', 1950)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (14, 'De 16 a 24 años', 2012, 'Hombres', 'España', 21707)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (15, 'De 16 a 24 años', 2012, 'Hombres', 'Francia', 2727)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (16, 'De 16 a 24 años', 2012, 'Hombres', 'Holanda', 6263)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (17, 'De 16 a 24 años', 2012, 'Hombres', 'Irlanda', 3053)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (18, 'De 16 a 24 años', 2012, 'Hombres', 'Italia', 2993)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (19, 'De 16 a 24 años', 2012, 'Hombres', 'Países Nórdicos', 3609)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (20, 'De 16 a 24 años', 2012, 'Hombres', 'Reino Unido', 24294)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (21, 'De 16 a 24 años', 2012, 'Hombres', 'Suiza', 6181)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (22, 'De 16 a 24 años', 2012, 'Hombres', 'Otros países', 8073)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (23, 'De 16 a 24 años', 2011, 'Hombres', 'Alemania', 21018)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (24, 'De 16 a 24 años', 2011, 'Hombres', 'Bélgica', 1659)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (25, 'De 16 a 24 años', 2011, 'Hombres', 'España', 26103)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (26, 'De 16 a 24 años', 2011, 'Hombres', 'Francia', 902)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (27, 'De 16 a 24 años', 2011, 'Hombres', 'Holanda', 7358)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (28, 'De 16 a 24 años', 2011, 'Hombres', 'Irlanda', 6014)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (29, 'De 16 a 24 años', 2011, 'Hombres', 'Italia', 3463)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (30, 'De 16 a 24 años', 2011, 'Hombres', 'Países Nórdicos', 1509)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (31, 'De 16 a 24 años', 2011, 'Hombres', 'Reino Unido', 27247)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (32, 'De 16 a 24 años', 2011, 'Hombres', 'Suiza', 4207)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (33, 'De 16 a 24 años', 2011, 'Hombres', 'Otros países', 5390)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (34, 'De 16 a 24 años', 2013, 'Mujeres', 'Alemania', 34902)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (35, 'De 16 a 24 años', 2013, 'Mujeres', 'Bélgica', 4393)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (36, 'De 16 a 24 años', 2013, 'Mujeres', 'España', 27973)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (37, 'De 16 a 24 años', 2013, 'Mujeres', 'Francia', 3566)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (38, 'De 16 a 24 años', 2013, 'Mujeres', 'Holanda', 8883)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (39, 'De 16 a 24 años', 2013, 'Mujeres', 'Irlanda', 6155)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (40, 'De 16 a 24 años', 2013, 'Mujeres', 'Italia', 5099)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (41, 'De 16 a 24 años', 2013, 'Mujeres', 'Países Nórdicos', 4596)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (42, 'De 16 a 24 años', 2013, 'Mujeres', 'Reino Unido', 41710)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (43, 'De 16 a 24 años', 2013, 'Mujeres', 'Suiza', 4745)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (44, 'De 16 a 24 años', 2013, 'Mujeres', 'Otros países', 15790)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (45, 'De 16 a 24 años', 2012, 'Mujeres', 'Alemania', 33919)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (46, 'De 16 a 24 años', 2012, 'Mujeres', 'Bélgica', 3223)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (47, 'De 16 a 24 años', 2012, 'Mujeres', 'España', 25845)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (48, 'De 16 a 24 años', 2012, 'Mujeres', 'Francia', 4199)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (49, 'De 16 a 24 años', 2012, 'Mujeres', 'Holanda', 10600)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (50, 'De 16 a 24 años', 2012, 'Mujeres', 'Irlanda', 4893)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (51, 'De 16 a 24 años', 2012, 'Mujeres', 'Italia', 4309)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (52, 'De 16 a 24 años', 2012, 'Mujeres', 'Países Nórdicos', 4083)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (53, 'De 16 a 24 años', 2012, 'Mujeres', 'Reino Unido', 35887)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (54, 'De 16 a 24 años', 2012, 'Mujeres', 'Suiza', 6271)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (55, 'De 16 a 24 años', 2012, 'Mujeres', 'Otros países', 9895)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (56, 'De 16 a 24 años', 2011, 'Mujeres', 'Alemania', 32754)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (57, 'De 16 a 24 años', 2011, 'Mujeres', 'Bélgica', 2402)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (58, 'De 16 a 24 años', 2011, 'Mujeres', 'España', 29850)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (59, 'De 16 a 24 años', 2011, 'Mujeres', 'Francia', 1000)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (60, 'De 16 a 24 años', 2011, 'Mujeres', 'Holanda', 9400)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (61, 'De 16 a 24 años', 2011, 'Mujeres', 'Irlanda', 6414)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (62, 'De 16 a 24 años', 2011, 'Mujeres', 'Italia', 2844)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (63, 'De 16 a 24 años', 2011, 'Mujeres', 'Países Nórdicos', 1643)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (64, 'De 16 a 24 años', 2011, 'Mujeres', 'Reino Unido', 39254)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (65, 'De 16 a 24 años', 2011, 'Mujeres', 'Suiza', 8110)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (66, 'De 16 a 24 años', 2011, 'Mujeres', 'Otros países', 9671)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (67, 'De 25 a 44 años', 2013, 'Hombres', 'Alemania', 122289)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (68, 'De 25 a 44 años', 2013, 'Hombres', 'Bélgica', 9706)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (69, 'De 25 a 44 años', 2013, 'Hombres', 'España', 132017)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (70, 'De 25 a 44 años', 2013, 'Hombres', 'Francia', 27131)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (71, 'De 25 a 44 años', 2013, 'Hombres', 'Holanda', 26355)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (72, 'De 25 a 44 años', 2013, 'Hombres', 'Irlanda', 32343)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (73, 'De 25 a 44 años', 2013, 'Hombres', 'Italia', 28337)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (74, 'De 25 a 44 años', 2013, 'Hombres', 'Países Nórdicos', 18724)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (75, 'De 25 a 44 años', 2013, 'Hombres', 'Reino Unido', 165140)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (76, 'De 25 a 44 años', 2013, 'Hombres', 'Suiza', 13876)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (77, 'De 25 a 44 años', 2013, 'Hombres', 'Otros países', 65460)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (78, 'De 25 a 44 años', 2012, 'Hombres', 'Alemania', 126578)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (79, 'De 25 a 44 años', 2012, 'Hombres', 'Bélgica', 13709)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (80, 'De 25 a 44 años', 2012, 'Hombres', 'España', 125888)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (81, 'De 25 a 44 años', 2012, 'Hombres', 'Francia', 23174)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (82, 'De 25 a 44 años', 2012, 'Hombres', 'Holanda', 22381)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (83, 'De 25 a 44 años', 2012, 'Hombres', 'Irlanda', 25622)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (84, 'De 25 a 44 años', 2012, 'Hombres', 'Italia', 26249)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (85, 'De 25 a 44 años', 2012, 'Hombres', 'Países Nórdicos', 15585)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (86, 'De 25 a 44 años', 2012, 'Hombres', 'Reino Unido', 158889)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (87, 'De 25 a 44 años', 2012, 'Hombres', 'Suiza', 11237)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (88, 'De 25 a 44 años', 2012, 'Hombres', 'Otros países', 66760)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (89, 'De 25 a 44 años', 2011, 'Hombres', 'Alemania', 130722)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (90, 'De 25 a 44 años', 2011, 'Hombres', 'Bélgica', 18477)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (91, 'De 25 a 44 años', 2011, 'Hombres', 'España', 145199)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (92, 'De 25 a 44 años', 2011, 'Hombres', 'Francia', 11816)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (93, 'De 25 a 44 años', 2011, 'Hombres', 'Holanda', 28207)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (94, 'De 25 a 44 años', 2011, 'Hombres', 'Irlanda', 29235)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (95, 'De 25 a 44 años', 2011, 'Hombres', 'Italia', 27231)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (96, 'De 25 a 44 años', 2011, 'Hombres', 'Países Nórdicos', 14502)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (97, 'De 25 a 44 años', 2011, 'Hombres', 'Reino Unido', 169942)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (98, 'De 25 a 44 años', 2011, 'Hombres', 'Suiza', 8113)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (99, 'De 25 a 44 años', 2011, 'Hombres', 'Otros países', 49924)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (100, 'De 25 a 44 años', 2013, 'Mujeres', 'Alemania', 103832)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (101, 'De 25 a 44 años', 2013, 'Mujeres', 'Bélgica', 12782)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (102, 'De 25 a 44 años', 2013, 'Mujeres', 'España', 121431)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (103, 'De 25 a 44 años', 2013, 'Mujeres', 'Francia', 25682)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (104, 'De 25 a 44 años', 2013, 'Mujeres', 'Holanda', 26540)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (105, 'De 25 a 44 años', 2013, 'Mujeres', 'Irlanda', 27395)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (106, 'De 25 a 44 años', 2013, 'Mujeres', 'Italia', 21752)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (107, 'De 25 a 44 años', 2013, 'Mujeres', 'Países Nórdicos', 30999)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (108, 'De 25 a 44 años', 2013, 'Mujeres', 'Reino Unido', 200527)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (109, 'De 25 a 44 años', 2013, 'Mujeres', 'Suiza', 10157)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (110, 'De 25 a 44 años', 2013, 'Mujeres', 'Otros países', 60723)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (111, 'De 25 a 44 años', 2012, 'Mujeres', 'Alemania', 126418)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (112, 'De 25 a 44 años', 2012, 'Mujeres', 'Bélgica', 17787)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (113, 'De 25 a 44 años', 2012, 'Mujeres', 'España', 121029)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (114, 'De 25 a 44 años', 2012, 'Mujeres', 'Francia', 19662)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (115, 'De 25 a 44 años', 2012, 'Mujeres', 'Holanda', 22526)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (116, 'De 25 a 44 años', 2012, 'Mujeres', 'Irlanda', 27734)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (117, 'De 25 a 44 años', 2012, 'Mujeres', 'Italia', 19253)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (118, 'De 25 a 44 años', 2012, 'Mujeres', 'Países Nórdicos', 17240)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (119, 'De 25 a 44 años', 2012, 'Mujeres', 'Reino Unido', 168035)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (120, 'De 25 a 44 años', 2012, 'Mujeres', 'Suiza', 15098)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (121, 'De 25 a 44 años', 2012, 'Mujeres', 'Otros países', 56761)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (122, 'De 25 a 44 años', 2011, 'Mujeres', 'Alemania', 117588)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (123, 'De 25 a 44 años', 2011, 'Mujeres', 'Bélgica', 13216)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (124, 'De 25 a 44 años', 2011, 'Mujeres', 'España', 134065)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (125, 'De 25 a 44 años', 2011, 'Mujeres', 'Francia', 13474)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (126, 'De 25 a 44 años', 2011, 'Mujeres', 'Holanda', 23184)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (127, 'De 25 a 44 años', 2011, 'Mujeres', 'Irlanda', 25212)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (128, 'De 25 a 44 años', 2011, 'Mujeres', 'Italia', 26324)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (129, 'De 25 a 44 años', 2011, 'Mujeres', 'Países Nórdicos', 14932)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (130, 'De 25 a 44 años', 2011, 'Mujeres', 'Reino Unido', 182750)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (131, 'De 25 a 44 años', 2011, 'Mujeres', 'Suiza', 8089)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (132, 'De 25 a 44 años', 2011, 'Mujeres', 'Otros países', 62682)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (133, 'Mayor de 44 años', 2013, 'Hombres', 'Alemania', 108202)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (134, 'Mayor de 44 años', 2013, 'Hombres', 'Bélgica', 22596)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (135, 'Mayor de 44 años', 2013, 'Hombres', 'España', 77028)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (136, 'Mayor de 44 años', 2013, 'Hombres', 'Francia', 19721)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (137, 'Mayor de 44 años', 2013, 'Hombres', 'Holanda', 22566)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (138, 'Mayor de 44 años', 2013, 'Hombres', 'Irlanda', 24157)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (139, 'Mayor de 44 años', 2013, 'Hombres', 'Italia', 19109)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (140, 'Mayor de 44 años', 2013, 'Hombres', 'Países Nórdicos', 38405)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (141, 'Mayor de 44 años', 2013, 'Hombres', 'Reino Unido', 217000)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (142, 'Mayor de 44 años', 2013, 'Hombres', 'Suiza', 15760)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (143, 'Mayor de 44 años', 2013, 'Hombres', 'Otros países', 41032)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (144, 'Mayor de 44 años', 2012, 'Hombres', 'Alemania', 120687)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (145, 'Mayor de 44 años', 2012, 'Hombres', 'Bélgica', 20362)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (146, 'Mayor de 44 años', 2012, 'Hombres', 'España', 74861)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (147, 'Mayor de 44 años', 2012, 'Hombres', 'Francia', 22003)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (148, 'Mayor de 44 años', 2012, 'Hombres', 'Holanda', 30477)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (149, 'Mayor de 44 años', 2012, 'Hombres', 'Irlanda', 22049)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (150, 'Mayor de 44 años', 2012, 'Hombres', 'Italia', 15892)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (151, 'Mayor de 44 años', 2012, 'Hombres', 'Países Nórdicos', 26550)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (152, 'Mayor de 44 años', 2012, 'Hombres', 'Reino Unido', 222855)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (153, 'Mayor de 44 años', 2012, 'Hombres', 'Suiza', 5903)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (154, 'Mayor de 44 años', 2012, 'Hombres', 'Otros países', 22494)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (155, 'Mayor de 44 años', 2011, 'Hombres', 'Alemania', 117055)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (156, 'Mayor de 44 años', 2011, 'Hombres', 'Bélgica', 28409)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (157, 'Mayor de 44 años', 2011, 'Hombres', 'España', 89240)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (158, 'Mayor de 44 años', 2011, 'Hombres', 'Francia', 14047)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (159, 'Mayor de 44 años', 2011, 'Hombres', 'Holanda', 27124)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (160, 'Mayor de 44 años', 2011, 'Hombres', 'Irlanda', 23885)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (161, 'Mayor de 44 años', 2011, 'Hombres', 'Italia', 12141)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (162, 'Mayor de 44 años', 2011, 'Hombres', 'Países Nórdicos', 27751)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (163, 'Mayor de 44 años', 2011, 'Hombres', 'Reino Unido', 220566)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (164, 'Mayor de 44 años', 2011, 'Hombres', 'Suiza', 8967)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (165, 'Mayor de 44 años', 2011, 'Hombres', 'Otros países', 42589)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (166, 'Mayor de 44 años', 2013, 'Mujeres', 'Alemania', 122371)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (167, 'Mayor de 44 años', 2013, 'Mujeres', 'Bélgica', 24813)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (168, 'Mayor de 44 años', 2013, 'Mujeres', 'España', 70751)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (169, 'Mayor de 44 años', 2013, 'Mujeres', 'Francia', 17504)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (170, 'Mayor de 44 años', 2013, 'Mujeres', 'Holanda', 29078)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (171, 'Mayor de 44 años', 2013, 'Mujeres', 'Irlanda', 19125)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (172, 'Mayor de 44 años', 2013, 'Mujeres', 'Italia', 12349)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (173, 'Mayor de 44 años', 2013, 'Mujeres', 'Países Nórdicos', 16783)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (174, 'Mayor de 44 años', 2013, 'Mujeres', 'Reino Unido', 244351)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (175, 'Mayor de 44 años', 2013, 'Mujeres', 'Suiza', 10065)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (176, 'Mayor de 44 años', 2013, 'Mujeres', 'Otros países', 37993)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (177, 'Mayor de 44 años', 2012, 'Mujeres', 'Alemania', 123252)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (178, 'Mayor de 44 años', 2012, 'Mujeres', 'Bélgica', 15755)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (179, 'Mayor de 44 años', 2012, 'Mujeres', 'España', 71003)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (180, 'Mayor de 44 años', 2012, 'Mujeres', 'Francia', 13765)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (181, 'Mayor de 44 años', 2012, 'Mujeres', 'Holanda', 32331)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (182, 'Mayor de 44 años', 2012, 'Mujeres', 'Irlanda', 14030)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (183, 'Mayor de 44 años', 2012, 'Mujeres', 'Italia', 18648)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (184, 'Mayor de 44 años', 2012, 'Mujeres', 'Países Nórdicos', 19998)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (185, 'Mayor de 44 años', 2012, 'Mujeres', 'Reino Unido', 247639)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (186, 'Mayor de 44 años', 2012, 'Mujeres', 'Suiza', 4297)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (187, 'Mayor de 44 años', 2012, 'Mujeres', 'Otros países', 34465)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (188, 'Mayor de 44 años', 2011, 'Mujeres', 'Alemania', 124922)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (189, 'Mayor de 44 años', 2011, 'Mujeres', 'Bélgica', 17399)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (190, 'Mayor de 44 años', 2011, 'Mujeres', 'España', 83272)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (191, 'Mayor de 44 años', 2011, 'Mujeres', 'Francia', 20403)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (192, 'Mayor de 44 años', 2011, 'Mujeres', 'Holanda', 20910)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (193, 'Mayor de 44 años', 2011, 'Mujeres', 'Irlanda', 19600)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (194, 'Mayor de 44 años', 2011, 'Mujeres', 'Italia', 16509)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (195, 'Mayor de 44 años', 2011, 'Mujeres', 'Países Nórdicos', 21092)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (196, 'Mayor de 44 años', 2011, 'Mujeres', 'Reino Unido', 252136)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (197, 'Mayor de 44 años', 2011, 'Mujeres', 'Suiza', 7852)
INSERT INTO [DatosTuristas] ([Id], [grupoedad], [periodo], [sexo], [pais], [turistas]) VALUES (198, 'Mayor de 44 años', 2011, 'Mujeres', 'Otros países', 30013)
-- 198 records
GO