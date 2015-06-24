:-use_module(library(lists)).


{}

/*
neuron(1, 'ADAL', 'Glutamate', ['null']).
neuron(2, 'ADAR', 'Glutamate', ['null']).
neuron(3, 'ADEL', 'Dopamine', ['DOP#2', 'EXP#1']).
neuron(4, 'ADER', 'Dopamine', ['DOP#2', 'EXP#1']).
neuron(5, 'ADFL', 'Serotonin', ['OSM#9', 'OCR#2', 'SRB#6']).
neuron(6, 'ADFR', 'Serotonin', ['OSM#9 ', 'OCR#2', 'SRB#6']).
neuron(7, 'ADLL', 'FMRFamide', ['OSM#9', 'OCR#1', 'OCR#2', 'SRE#1', 'SRB#6']).
neuron(8, 'ADLR', 'FMRFamide', ['OSM#9', 'OCR#1', 'OCR#2', 'SRE#1', 'SRB#6']).
neuron(9, 'AFDL', 'Glutamate', ['GCY#12']).
neuron(10, 'AFDR', 'Glutamate', ['GCY#12']).
neuron(11, 'AIAL', 'Acetylcholine', ['GLR#2', 'SRA#11']).
neuron(12, 'AIAR', 'Acetylcholine', ['GLR#2', 'SRA#11']).
neuron(13, 'AIBL', 'Glutamate', ['GLR#1', 'GLR#2', 'GLR#5', 'GGR#1']).
neuron(14, 'AIBR', 'Glutamate', ['GLR#1', 'GLR#2', 'GLR#5', 'GGR#1']).
neuron(15, 'AIML', 'Serotonin', ['null']).
neuron(16, 'AIMR', 'Serotonin', ['null']).
neuron(17, 'AINL', 'Glutamate', ['null']).
neuron(18, 'AINR', 'Glutamate', ['null']).
neuron(19, 'AIYL', 'Acetylcholine', ['SER#2', 'SRA#11']).
neuron(20, 'AIYR', 'Acetylcholine', ['SER#2', 'SRA#11']).
neuron(21, 'AIZL', 'Glutamate', ['SER#2']).
neuron(22, 'AIZR', 'Glutamate', ['SER#2']).
neuron(23, 'ALA', 'Glutamate', ['SRA#10']).
neuron(24, 'ALML', 'Glutamate', ['MEC#2', 'MEC#4', 'MEC#10', 'MEC#9', 'MEC#6', 'DEG#3', 'DES#2', 'GLR#8', 'DOP#1']).
neuron(25, 'ALMR', 'Glutamate', ['MEC#2', 'MEC#4', 'MEC#10', 'MEC#9', 'MEC#6', 'DEG#3', 'DES#2', 'GLR#8', 'DOP#1']).
neuron(26, 'ALNL', 'Acetylcholine', ['SER#2', 'DOP#1', 'GCY#35']).
neuron(27, 'ALNR', 'Acetylcholine', ['SER#2', 'DOP#1', 'GCY#35']).
neuron(28, 'AQR', 'Glutamate', ['GCY#32', 'NPR#1', 'GCY#35']).
neuron(29, 'AS1', 'Acetylcholine', ['null']).
neuron(30, 'AS10', 'Acetylcholine', ['null']).
neuron(31, 'AS11', 'Acetylcholine', ['null']).
neuron(32, 'AS2', 'Acetylcholine', ['null']).
neuron(33, 'AS3', 'Acetylcholine', ['null']).
neuron(34, 'AS4', 'Acetylcholine', ['null']).
neuron(35, 'AS5', 'Acetylcholine', ['null']).
neuron(36, 'AS6', 'Acetylcholine', ['null']).
neuron(37, 'AS7', 'Acetylcholine', ['null']).
neuron(38, 'AS8', 'Acetylcholine', ['null']).
neuron(39, 'AS9', 'Acetylcholine', ['null']).
neuron(40, 'ASEL', 'FMRFamide', ['GCY#6', 'GCY#7', 'OSM#9', 'GCY#12', 'DOP#3']).
neuron(41, 'ASER', 'FMRFamide', ['GCY#5', 'OSM#9', 'GCY#12', 'DOP#3']).
neuron(42, 'ASGL', 'Glutamate', ['OSM#9', 'NPR#1']).
neuron(43, 'ASGR', 'Glutamate', ['NPR#1', 'OSM#9']).
neuron(44, 'ASHL', 'Glutamate', ['OSM#9', 'OCR#2', 'SRA#6', 'SRB#6', 'NPR#1', 'UNC#8']).
neuron(45, 'ASHR', 'Glutamate', ['OSM#9', 'OCR#2', 'SRA#6', 'SRB#6', 'NPR#1', 'UNC#8']).
neuron(46, 'ASIL', 'null', ['SRD#1', 'STR#2', 'STR#3', 'DAF#11', 'SRA#6']).
neuron(47, 'ASIR', 'null', ['SRD#1', 'STR#2', 'STR#3', 'DAF#11', 'SRA#6']).
neuron(48, 'ASJL', 'Glutamate', ['OSM#9', 'SRE#1', 'DAF#11']).
neuron(49, 'ASJR', 'Glutamate', ['OSM#9', 'SRE#1', 'DAF#11']).
neuron(50, 'ASKL', 'Glutamate', ['OSM#9', 'SRA#7', 'SRA#9', 'SRG#2', 'SRG#8', 'DAF#11']).
neuron(51, 'ASKR', 'Glutamate', ['OSM#9', 'SRA#7', 'SRA#9', 'SRG#2', 'SRG#8', 'DAF#11']).
neuron(52, 'AUAL', 'Glutamate', ['GLR#4', 'NPR#1', 'SER#2', 'DOP#1', 'SER#2']).
neuron(53, 'AUAR', 'Glutamate', ['GLR#4', 'NPR#1', 'SER#2', 'DOP#1', 'SER#2']).
neuron(54, 'AVAL', 'FMRFamide', ['GLR#1', 'GLR#2', 'GLR#4', 'GLR#5', 'NMR#1', 'GGR#3', 'GGR#2']).
neuron(55, 'AVAR', 'FMRFamide', ['GLR#1', 'GLR#2', 'GLR#4', 'GLR#5', 'NMR#1', 'GGR#3', 'GGR#2']).
neuron(56, 'AVBL', 'Glutamate', ['GLR#1', 'GLR#5', 'SRA#11', 'GGR#3', 'UNC#8', 'GGR#3']).
neuron(57, 'AVBR', 'Glutamate', ['GLR#1', 'GLR#5', 'SRA#11', 'GGR#3', 'UNC#8', 'GGR#3']).
neuron(58, 'AVDL', 'Glutamate', ['GLR#1', 'GLR#2', 'GLR#5', 'NMR#1', 'NMR#2', 'UNC#8']).
neuron(59, 'AVDR', 'Glutamate', ['GLR#1', 'GLR#2', 'GLR#5', 'NMR#1', 'NMR#2', 'UNC#8']).
neuron(60, 'AVEL', 'FMRFamide', ['GLR#1', 'GLR#2', 'GLR#5', 'NMR#1', 'NMR#2']).
neuron(61, 'AVER', 'FMRFamide', ['GLR#1', 'GLR#2', 'GLR#5', 'NMR#1', 'NMR#2']).
neuron(62, 'AVFL', 'Glutamate', ['null']).
neuron(63, 'AVFR', 'Glutamate', ['null']).
neuron(64, 'AVG', 'Glutamate', ['GLR#1', 'GLR#2', 'NMR#1', 'NMR#2', 'DEG#3']).
neuron(65, 'AVHL', 'Glutamate', ['GLR#4', 'SER#2', 'GGR#1']).
neuron(66, 'AVHR', 'Glutamate', ['GLR#4', 'SER#2', 'GGR#1']).
neuron(67, 'AVJL', 'Glutamate', ['GLR#1']).
neuron(68, 'AVJR', 'Glutamate', ['GLR#1']).
neuron(69, 'AVKL', 'FMRFamide', ['GLR#5']).
neuron(70, 'AVKR', 'FMRFamide', ['GLR#5']).
neuron(71, 'AVL', 'GABA', ['null']).
neuron(72, 'AVM', 'Glutamate', ['MEC#2', 'MEC#4', 'MEC#10', 'MEC#9', 'MEC#6', 'DOP#1', 'GCY#35']).
neuron(73, 'AWAL', 'null', ['ODR#10', 'OSM#9', 'OCR#1', 'OCR#2']).
neuron(74, 'AWAR', 'null', ['ODR#10', 'OSM#9', 'OCR#1', 'OCR#2']).
neuron(75, 'AWBL', 'Glutamate', ['STR#1', 'DAF#11', 'AEX#2']).
neuron(76, 'AWBR', 'Glutamate', ['STR#1', 'DAF#11', 'AEX#2']).
neuron(77, 'AWCL', 'Glutamate', ['OSM#9', 'DAF#11', 'STR#2', 'GCY#12']).
neuron(78, 'AWCR', 'Glutamate', ['OSM#9', 'DAF#11', 'STR#2', 'GCY#12']).
neuron(79, 'BAGL', 'Glutamate', ['GCY#33']).
neuron(80, 'BAGR', 'Glutamate', ['GCY#33']).
neuron(81, 'BDUL', 'GABA', ['GLR#8']).
neuron(82, 'BDUR', 'GABA', ['GLR#8', 'SER#2', 'GCY#35']).
neuron(83, 'CANL*', 'Monoamine', ['SER#2', 'GGR#2']).
neuron(84, 'CANR*', 'Monoamine', ['SER#2', 'GGR#2']).
neuron(85, 'CEPDL', 'Dopamine', ['DOP#2']).
neuron(86, 'CEPDR', 'Dopamine', ['DOP#2']).
neuron(87, 'CEPVL', 'Dopamine', ['DOP#2']).
neuron(88, 'CEPVR', 'Dopamine', ['DOP#2']).
neuron(89, 'DA1', 'Acetylcholine', ['UNC#8']).
neuron(90, 'DA2', 'Acetylcholine', ['UNC#8']).
neuron(91, 'DA3', 'Acetylcholine', ['UNC#8']).
neuron(92, 'DA4', 'Acetylcholine', ['UNC#8']).
neuron(93, 'DA5', 'Acetylcholine', ['UNC#8']).
neuron(94, 'DA6', 'Acetylcholine', ['UNC#8']).
neuron(95, 'DA7', 'Acetylcholine', ['UNC#8']).
neuron(96, 'DA8', 'Acetylcholine', ['UNC#8']).
neuron(97, 'DA9', 'Acetylcholine', ['SER#2']).
neuron(98, 'DB1', 'Acetylcholine', ['null']).
neuron(99, 'DB2', 'Acetylcholine', ['null']).
neuron(100, 'DB3', 'Acetylcholine', ['null']).
neuron(101, 'DB4', 'Acetylcholine', ['null']).
neuron(102, 'DB5', 'Acetylcholine', ['null']).
neuron(103, 'DB6', 'Acetylcholine', ['null']).
neuron(104, 'DB7', 'Acetylcholine', ['null']).
neuron(105, 'DD1', 'GABA', ['NPR#1', 'GGR#2', 'UNC#8']).
neuron(106, 'DD2', 'GABA', ['NPR#1', 'GGR#2', 'UNC#8']).
neuron(107, 'DD3', 'GABA', ['NPR#1', 'GGR#2', 'UNC#8']).
neuron(108, 'DD4', 'GABA', ['NPR#1', 'GGR#2', 'UNC#8']).
neuron(109, 'DD5', 'GABA', ['NPR#1', 'GGR#2', 'UNC#8']).
neuron(110, 'DD6', 'GABA', ['NPR#1', 'GGR#2', 'UNC#8']).
neuron(111, 'DVA', 'GABA', ['GLR#4', 'GLR#5', 'NMR#1', 'SER#2', 'SER#4', 'GGR#3', 'GGR#2']).
neuron(112, 'DVB', 'GABA', ['null']).
neuron(113, 'DVC', 'GABA', ['GLR#1', 'SER#4']).
neuron(114, 'FLPL', 'Glutamate', ['OSM#9', 'DEG#3', 'DES#2', 'GLR#4', 'MEC#10', 'DEL#1', 'UNC#8']).
neuron(115, 'FLPR', 'Glutamate', ['OSM#9', 'DEG#3', 'DES#2', 'GLR#4', 'MEC#10', 'DEL#1', 'UNC#8']).
neuron(116, 'HSNL', 'Serotonin', ['MEC#6', 'GAR#2', 'GLR#5', 'GGR#2']).
neuron(116, 'HSNL', 'Acetylcholine', ['MEC#6', 'GAR#2', 'GLR#5', 'GGR#2']).
neuron(117, 'HSNR', 'Acetylcholine', ['MEC#6', 'GAR#2', 'GLR#5', 'GGR#2']).
neuron(117, 'HSNR', 'Serotonin', ['MEC#6', 'GAR#2', 'GLR#5', 'GGR#2']).
neuron(118, 'I1L', 'Acetylcholine', ['GLR#7', 'GLR#8', 'ACM#2']).
neuron(119, 'I1R', 'Acetylcholine', ['GLR#7', 'GLR#8', 'ACM#2']).
neuron(120, 'I2L', 'Glutamate', ['GLR#7', 'GLR#8', 'ACM#2', 'SER#7b']).
neuron(121, 'I2R', 'Glutamate', ['GLR#7', 'GLR#8', 'ACM#2', 'SER#7b']).
neuron(122, 'I3', 'Glutamate', ['GLR#7', 'GLR7b', 'AEX#2']).
neuron(123, 'I4', 'Glutamate', ['null']).
neuron(124, 'I5', 'Serotonin', ['null']).
neuron(124, 'I5', 'Glutamate', ['null']).
neuron(125, 'I6', 'Acetylcholine', ['GLR#7', 'GLR#b8', 'SER#7b']).
neuron(126, 'IL1DL', 'Glutamate', ['DEG#3', 'MEC#6']).
neuron(127, 'IL1DR', 'Glutamate', ['DEG#3', 'MEC#6']).
neuron(128, 'IL1L', 'Glutamate', ['DEG#3', 'MEC#6']).
neuron(129, 'IL1R', 'Glutamate', ['DEG#3', 'MEC#6']).
neuron(130, 'IL1VL', 'Glutamate', ['DEG#3', 'MEC#6']).
neuron(131, 'IL1VR', 'Glutamate', ['DEG#3', 'MEC#6']).
neuron(132, 'IL2DL', 'Serotonin', ['DES#2']).
neuron(133, 'IL2DR', 'Serotonin', ['DES#2']).
neuron(134, 'IL2L', 'Acetylcholine', ['NPR#1']).
neuron(135, 'IL2R', 'Acetylcholine', ['NPR#1']).
neuron(136, 'IL2VL', 'Serotonin', ['DES#2']).
neuron(137, 'IL2VR', 'Serotonin', ['DES#2']).
neuron(138, 'LUAL', 'Glutamate', ['GLR#5', 'SER#2']).
neuron(139, 'LUAR', 'Glutamate', ['GLR#5', 'SER#2']).
neuron(140, 'M1', 'Acetylcholine', ['GLR#2', 'AVR#14']).
neuron(141, 'M2L', 'Acetylcholine', ['SER#7b']).
neuron(142, 'M2R', 'Acetylcholine', ['SER#7b']).
neuron(143, 'M3L', 'Glutamate', ['GLR#8', 'NPR#1']).
neuron(144, 'M3R', 'Glutamate', ['GLR#8', 'NPR#1']).
neuron(145, 'M4', 'Acetylcholine', ['SER7b', 'ACM#2', 'GLR#8']).
neuron(146, 'M5', 'Acetylcholine', ['GLR#8']).
neuron(147, 'MCL', 'Acetylcholine', ['GLR#8', 'SER#7']).
neuron(148, 'MCR', 'Acetylcholine', ['GLR#8', 'SER#7']).
neuron(149, 'MI', 'null', ['GLR#2 ']).
neuron(150, 'NSML', 'Serotonin', ['GLR#7', 'GLR#8', 'SER#2', 'AEX#2']).
neuron(150, 'NSML', 'Glutamate', ['GLR#7', 'GLR#8', 'SER#2', 'AEX#2']).
neuron(151, 'NSMR', 'Serotonin', ['GLR#7', 'GLR#8', 'SER#2', 'AEX#2']).
neuron(151, 'NSMR', 'Glutamate', ['GLR#7', 'GLR#8', 'SER#2', 'AEX#2']).
neuron(152, 'OLLL', 'Glutamate', ['SER#2']).
neuron(153, 'OLLR', 'Glutamate', ['SER#2']).
neuron(154, 'OLQDL', 'Glutamate', ['OSM#9', 'OCR#4', 'NPR#1']).
neuron(155, 'OLQDR', 'Glutamate', ['OSM#9', 'OCR#4', 'NPR#1']).
neuron(156, 'OLQVL', 'Glutamate', ['OSM#9', 'OCR#4', 'NPR#1']).
neuron(157, 'OLQVR', 'Glutamate', ['OSM#9', 'OCR#4', 'NPR#1']).
neuron(158, 'PDA', 'Serotonin', ['EXP#1', 'UNC#8', 'SER#2']).
neuron(159, 'PDB', 'FMRFamide', ['UNC#8']).
neuron(160, 'PDEL', 'Dopamine', ['DOP#2']).
neuron(161, 'PDER', 'Dopamine', ['DOP#2']).
neuron(162, 'PHAL', 'Glutamate', ['GCY#12', 'OSM#9', 'OCR#2', 'SRG#13', 'SRB#6', 'NPR#1']).
neuron(163, 'PHAR', 'Glutamate', ['GCY#12', 'OSM#9', 'OCR#2', 'SRG#13', 'SRB#6', 'NPR#1']).
neuron(164, 'PHBL', 'Serotonin', ['OSM#9', 'OCR#2', 'SRB#6', 'NPR#1']).
neuron(165, 'PHBR', 'Serotonin', ['OSM#9', 'OCR#2', 'SRB#6', 'NPR#1']).
neuron(166, 'PHCL', 'Glutamate', ['DOP#1']).
neuron(167, 'PHCR', 'Glutamate', ['DOP#1']).
neuron(168, 'PLML', 'Glutamate', ['MEC#2', 'MEC#4', 'MEC#6', 'MEC#9DES#2', 'DOP#1']).
neuron(169, 'PLMR', 'Glutamate', ['MEC#2', 'MEC#4', 'MEC#6', 'MEC#9', 'DES#2', 'DOP#1']).
neuron(170, 'PLNL', 'Acetylcholine', ['DOP#1', 'GCY#35']).
neuron(171, 'PLNR', 'Acetylcholine', ['DOP#1', 'GCY#35']).
neuron(172, 'PQR', 'Glutamate', ['GCY#32', 'NPR#1', 'GCY#35 ']).
neuron(173, 'PVCL', 'Glutamate', ['DEG#3', 'SER#2']).
neuron(174, 'PVCR', 'Glutamate', ['DEG#3', 'SER#2']).
neuron(175, 'PVDL', 'Glutamate', ['MEC#10', 'MEC#9', 'MEC#6', 'OSM#9', 'SER#2', 'DEG#3', 'DOP#3']).
neuron(176, 'PVDR', 'Glutamate', ['MEC#10', 'MEC#9', 'MEC#6', 'OSM#9', 'SER#2', 'DEG#3', 'DOP#3']).
neuron(177, 'PVM', 'Glutamate', ['GAR#1', 'MEC#2', 'MEC#4', 'MEC#10', 'MEC#9']).
neuron(178, 'PVNL', 'Glutamate', ['null']).
neuron(179, 'PVNR', 'Glutamate', ['null']).
neuron(180, 'PVPL', 'Glutamate', ['null']).
neuron(181, 'PVPR', 'Glutamate', ['null']).
neuron(182, 'PVQL', 'null', ['GLR#1', 'GLR#5', 'SRA#6', 'DOP#1', 'GGR#1']).
neuron(183, 'PVQR', 'null', ['GLR#1', 'GLR#5', 'SRA#6', 'DOP#1', 'GGR#1']).
neuron(184, 'PVR', 'Glutamate', ['GGR#1']).
neuron(185, 'PVT', 'Glutamate', ['SER#2', 'SER#4']).
neuron(186, 'PVWL', 'Serotonin', ['null']).
neuron(187, 'PVWR', 'Serotonin', ['null']).
neuron(188, 'RIAL', 'GABA', ['Glr#3', 'GLR#6', 'SER#2']).
neuron(189, 'RIAR', 'GABA', ['Glr#3', 'GLR#6', 'SER#2']).
neuron(190, 'RIBL', 'Glutamate', ['DOP#1']).
neuron(191, 'RIBR', 'Glutamate', ['DOP#1']).
neuron(192, 'RICL', 'Octapamine', ['DOP#3', 'SER#2']).
neuron(193, 'RICR', 'Octapamine', ['DOP#3', 'SER#2']).
neuron(194, 'RID', 'GABA', ['EXP#1', 'SER#2']).
neuron(195, 'RIFL', 'Glutamate', ['null']).
neuron(196, 'RIFR', 'Glutamate', ['null']).
neuron(197, 'RIGL', 'FRMFemide', ['null']).
neuron(198, 'RIGR', 'FRMFemide', ['null']).
neuron(199, 'RIH', 'Serotonin', ['null']).
neuron(200, 'RIML', 'Tyramine', ['DOP#1']).
neuron(200, 'RIML', 'Acetylcholine', ['DOP#1']).
neuron(201, 'RIMR', 'Tyramine', ['DOP#1']).
neuron(201, 'RIMR', 'Acetylcholine', ['DOP#1']).
neuron(202, 'RIPL', 'Serotonin', ['null']).
neuron(203, 'RIPR', 'Serotonin', ['null']).
neuron(204, 'RIR', 'null', ['null']).
neuron(205, 'RIS', 'GABA', ['GLR#1', 'SER#4', 'DOP#1']).
neuron(206, 'RIVL', 'GABA', ['null']).
neuron(207, 'RIVR', 'GABA', ['null']).
neuron(208, 'RMDDL', 'Acetylcholine', ['null']).
neuron(209, 'RMDDR', 'Acetylcholine', ['null']).
neuron(210, 'RMDL', 'Acetylcholine', ['null']).
neuron(211, 'RMDR', 'Acetylcholine', ['null']).
neuron(212, 'RMDVL', 'Acetylcholine', ['null']).
neuron(213, 'RMDVR', 'Acetylcholine', ['null']).
neuron(214, 'RMED', 'GABA', ['AVR#15', 'SER#2']).
neuron(215, 'RMEL', 'GABA', ['GLR#1', 'SER#2']).
neuron(216, 'RMER', 'GABA', ['GLR#1', 'SER#2']).
neuron(217, 'RMEV', 'GABA', ['AVR#15', 'SER#2']).
neuron(218, 'RMFL', 'Glutamate', ['null']).
neuron(219, 'RMFR', 'Glutamate', ['null']).
neuron(220, 'RMGL', 'FRMFemide', ['null']).
neuron(221, 'RMGR', 'FRMFemide', ['null']).
neuron(222, 'RMHL', 'Glutamate', ['null']).
neuron(223, 'RMHR', 'Glutamate', ['null']).
neuron(224, 'SAADL', 'Acetylcholine', ['null']).
neuron(225, 'SAADR', 'Acetylcholine', ['null']).
neuron(226, 'SAAVL', 'Acetylcholine', ['null']).
neuron(227, 'SAAVR', 'Acetylcholine', ['null']).
neuron(228, 'SABD', 'Acetylcholine', ['EXP#1', 'SER#2']).
neuron(229, 'SABVL', 'Acetylcholine', ['DEL#1', 'SER#2']).
neuron(230, 'SABVR', 'Acetylcholine', ['DEL#1', 'SER#2']).
neuron(231, 'SDQL', 'Acetylcholine', ['GCY#35', 'SER#2']).
neuron(232, 'SDQR', 'Acetylcholine', ['GCY#35', 'SER#2']).
neuron(233, 'SIADL', 'Acetylcholine', ['DOP#3', 'GGR#3', 'GGR#2', 'SER#2']).
neuron(234, 'SIADR', 'Acetylcholine', ['DOP#3', 'GGR#3', 'GGR#2', 'SER#2']).
neuron(235, 'SIAVL', 'Acetylcholine', ['GGR#2', 'DOP#3', 'SER#2']).
neuron(236, 'SIAVR', 'Acetylcholine', ['GGR#2', 'DOP#3', 'SER#2']).
neuron(237, 'SIBDL', 'Acetylcholine', ['null']).
neuron(238, 'SIBDR', 'Acetylcholine', ['null']).
neuron(239, 'SIBVL', 'Acetylcholine', ['null']).
neuron(240, 'SIBVR', 'Acetylcholine', ['null']).
neuron(241, 'SMBDL', 'Acetylcholine', ['null']).
neuron(242, 'SMBDR', 'Acetylcholine', ['null']).
neuron(243, 'SMBVL', 'Acetylcholine', ['null']).
neuron(244, 'SMBVR', 'Acetylcholine', ['null']).
neuron(245, 'SMDDL', 'Acetylcholine', ['GGR#2', 'GGR#3']).
neuron(246, 'SMDDR', 'Acetylcholine', ['GGR#2', 'GGR#3']).
neuron(247, 'SMDVL', 'Acetylcholine', ['GGR#1', 'GGR#2']).
neuron(248, 'SMDVR', 'Acetylcholine', ['GGR#1', 'GGR#2']).
neuron(249, 'URADL', 'Acetylcholine', ['null']).
neuron(250, 'URADR', 'Acetylcholine', ['null']).
neuron(251, 'URAVL', 'Acetylcholine', ['null']).
neuron(252, 'URAVR', 'Acetylcholine', ['null']).
neuron(253, 'URBL', 'Acetylcholine', ['null']).
neuron(254, 'URBR', 'Acetylcholine', ['null']).
neuron(255, 'URXL', 'Glutamate', ['GCY#32', 'GCY#35', 'NPR#1', 'SRA#10']).
neuron(256, 'URXR', 'Glutamate', ['GCY#32', 'GCY#35', 'NPR#1', 'SRA#10']).
neuron(257, 'URYDL', 'Glutamate', ['null']).
neuron(258, 'URYDR', 'Glutamate', ['null']).
neuron(259, 'URYVL', 'Glutamate', ['null']).
neuron(260, 'URYVR', 'Glutamate', ['null']).
neuron(261, 'VA1', 'Acetylcholine', ['DEL#1']).
neuron(262, 'VA10', 'Acetylcholine', ['DEL#1']).
neuron(263, 'VA11', 'Acetylcholine', ['DEL#1']).
neuron(264, 'VA12', 'Acetylcholine', ['DEL#1']).
neuron(265, 'VA2', 'Acetylcholine', ['DEL#1']).
neuron(266, 'VA3', 'Acetylcholine', ['DEL#1']).
neuron(267, 'VA4', 'Acetylcholine', ['DEL#1']).
neuron(268, 'VA5', 'Acetylcholine', ['DEL#1']).
neuron(269, 'VA6', 'Acetylcholine', ['DEL#1']).
neuron(270, 'VA7', 'Acetylcholine', ['DEL#1']).
neuron(271, 'VA8', 'Acetylcholine', ['DEL#1']).
neuron(272, 'VA9', 'Acetylcholine', ['DEL#1']).
neuron(273, 'VB1', 'Acetylcholine', ['DEL#1']).
neuron(274, 'VB10', 'Acetylcholine', ['DEL#1']).
neuron(275, 'VB11', 'Acetylcholine', ['DEL#1']).
neuron(276, 'VB2', 'Acetylcholine', ['DEL#1']).
neuron(277, 'VB3', 'Acetylcholine', ['DEL#1']).
neuron(278, 'VB4', 'Acetylcholine', ['DEL#1']).
neuron(279, 'VB5', 'Acetylcholine', ['DEL#1']).
neuron(280, 'VB6', 'Acetylcholine', ['DEL#1']).
neuron(281, 'VB7', 'Acetylcholine', ['DEL#1']).
neuron(282, 'VB8', 'Acetylcholine', ['DEL#1']).
neuron(283, 'VB9', 'Acetylcholine', ['DEL#1']).
neuron(284, 'VC1', 'Acetylcholine', ['GLR#5']).
neuron(284, 'VC1', 'Serotonin', ['GLR#5']).
neuron(285, 'VC2', 'Acetylcholine', ['GLR#5']).
neuron(285, 'VC2', 'Serotonin', ['GLR#5']).
neuron(286, 'VC3', 'Acetylcholine', ['GLR#5']).
neuron(286, 'VC3', 'Serotonin', ['GLR#5']).
neuron(287, 'VC4', 'Acetylcholine', ['GLR#5']).
neuron(287, 'VC4', 'Serotonin', ['GLR#5']).
neuron(288, 'VC5', 'Acetylcholine', ['GLR#5']).
neuron(288, 'VC5', 'Serotonin', ['GLR#5']).
neuron(289, 'VC6', 'Acetylcholine', ['GLR#5']).
neuron(289, 'VC6', 'Serotonin', ['GLR#5']).
neuron(290, 'VD1', 'GABA', ['NPR#1']).
neuron(291, 'VD10', 'GABA', ['NPR#1']).
neuron(292, 'VD11', 'GABA', ['NPR#1']).
neuron(293, 'VD12', 'GABA', ['NPR#1']).
neuron(294, 'VD13', 'GABA', ['NPR#1']).
neuron(295, 'VD2', 'GABA', ['NPR#1']).
neuron(296, 'VD3', 'GABA', ['NPR#1']).
neuron(297, 'VD4', 'GABA', ['NPR#1']).
neuron(298, 'VD5', 'GABA', ['NPR#1']).
neuron(299, 'VD6', 'GABA', ['NPR#1']).
neuron(300, 'VD7', 'GABA', ['NPR#1']).
neuron(301, 'VD8', 'GABA', ['NPR#1']).
neuron(302, 'VD9', 'GABA', ['NPR#1']).*/

transmit_recept('Acetylcholine', 'ACM#2', 'inhibitory').
transmit_recept('Acetylcholine', 'DEG#3 ', 'excitatory').
transmit_recept('Acetylcholine', 'DES#2', 'excitatory').
transmit_recept('Acetylcholine', 'GAR#1', 'inhibitory').
transmit_recept('Acetylcholine', 'GAR#2', 'inhibitory').
transmit_recept('Capsaicin', 'OCR#1 ', 'excitatory').
transmit_recept('Capsaicin', 'OCR#2', 'excitatory').
transmit_recept('Capsaicin', 'OSM#9', 'excitatory').
transmit_recept('Dopamine', 'DOP#1', 'inhibitory').
transmit_recept('Dopamine', 'DOP#2', 'inhibitory').
transmit_recept('Dopamine', 'DOP#3', 'inhibitory').
transmit_recept('FMRFamide', 'NPR#1 ', 'inhibitory').
transmit_recept('GABA', 'EXP#1', 'excitatory').
transmit_recept('GABA', 'GGR#1', 'inhibitory').
transmit_recept('GABA', 'GGR#2', 'inhibitory').
transmit_recept('GABA', 'GGR#3 ', 'inhibitory').
transmit_recept('Glutamate', 'AVR#14', 'inhibitory').
transmit_recept('Glutamate', 'AVR#15', 'inhibitory').
transmit_recept('Glutamate', 'GLR#1', 'excitatory').
transmit_recept('Glutamate', 'GLR#2', 'excitatory').
transmit_recept('Glutamate', 'GLR#3', 'excitatory').
transmit_recept('Glutamate', 'GLR#4', 'excitatory').
transmit_recept('Glutamate', 'GLR#5', 'excitatory').
transmit_recept('Glutamate', 'GLR#6', 'excitatory').
transmit_recept('Glutamate', 'GLR#7', 'excitatory').
transmit_recept('Glutamate', 'GLR#8', 'excitatory').
transmit_recept('Glutamate', 'NMR#1', 'excitatory').
transmit_recept('Glutamate', 'NMR#2', 'excitatory').
transmit_recept('Membrane', 'DAF#11', 'inhibitory').
transmit_recept('Membrane', 'DEL#1', 'excitatory ').
transmit_recept('Membrane', 'GCY#12', 'excitatory').
transmit_recept('Membrane', 'GCY#32', 'excitatory').
transmit_recept('Membrane', 'GCY#33', 'excitatory').
transmit_recept('Membrane', 'GCY#35 ', 'excitatory').
transmit_recept('Membrane', 'GCY#5', 'excitatory').
transmit_recept('Membrane', 'GCY#6', 'excitatory').
transmit_recept('Membrane', 'GCY#7', 'excitatory').
transmit_recept('Membrane', 'MEC#10 ', 'excitatory').
transmit_recept('Membrane', 'MEC#2', 'excitatory').
transmit_recept('Membrane', 'MEC#4 ', 'excitatory').
transmit_recept('Membrane', 'MEC#6', 'excitatory').
transmit_recept('Membrane', 'MEC#9 ', 'Unknown').
transmit_recept('Membrane', 'SRA#10', 'Unknown').
transmit_recept('Membrane', 'UNC#8', 'exitatory').
transmit_recept('Serotonin', 'SER#2 ', 'Unknown').
transmit_recept('Serotonin', 'SER#4 ', 'inhibitory').
transmit_recept('Serotonin', 'SER7b ', 'excitatory').
transmit_recept('Unknown', 'AEX#2', 'inhibitory').
transmit_recept('Unknown', 'ODR#10', 'Unknown').
transmit_recept('Unknown', 'SRA#11', 'Unknown').
transmit_recept('Unknown', 'SRA#6', 'Unknown').
transmit_recept('Unknown', 'SRA#7', 'Unknown').
transmit_recept('Unknown', 'SRA#9', 'Unknown').
transmit_recept('Unknown', 'SRB#6', 'Unknown').
transmit_recept('Unknown', 'SRD#1', 'Unknown').
transmit_recept('Unknown', 'SRE#1', 'Unknown').
transmit_recept('Unknown', 'SRG#13 ', 'Unknown').
transmit_recept('Unknown', 'SRG#2', 'Unknown').
transmit_recept('Unknown', 'SRG#8', 'Unknown').
transmit_recept('Unknown', 'STR#1', 'Unknown').
transmit_recept('Unknown', 'STR#2', 'Unknown').
transmit_recept('Unknown', 'STR#3', 'Unknown').

neuron(1, 'ADAL', 'Glutamate', ['null']).
neuron(2, 'ADAR', 'Glutamate', ['null']).
neuron(3, 'ADEL', 'Dopamine', ['DOP#2', 'EXP#1']).
neuron(4, 'ADER', 'Dopamine', ['DOP#2', 'EXP#1']).
neuron(5, 'ADFL', 'Serotonin', ['OSM#9', 'OCR#2', 'SRB#6']).
neuron(6, 'ADFR', 'Serotonin', ['OSM#9 ', 'OCR#2', 'SRB#6']).
neuron(7, 'ADLL', 'null', ['OSM#9', 'OCR#1', 'OCR#2', 'SRE#1', 'SRB#6']).
neuron(8, 'ADLR', 'null', ['OSM#9', 'OCR#1', 'OCR#2', 'SRE#1', 'SRB#6']).
neuron(9, 'AFDL', 'null', ['GCY#12']).
neuron(10, 'AFDR', 'null', ['GCY#12']).
neuron(11, 'AIAL', 'Acetylcholine', ['GLR#2', 'SRA#11']).
neuron(12, 'AIAR', 'Acetylcholine', ['GLR#2', 'SRA#11']).
neuron(13, 'AIBL', 'null', ['GLR#1', 'GLR#2', 'GLR#5', 'GGR#1']).
neuron(14, 'AIBR', 'null', ['GLR#1', 'GLR#2', 'GLR#5', 'GGR#1']).
neuron(15, 'AIML', 'Serotonin', ['null']).
neuron(16, 'AIMR', 'Serotonin', ['null']).
neuron(17, 'AINL', 'Glutamate', ['null']).
neuron(18, 'AINR', 'Glutamate', ['null']).
neuron(19, 'AIYL', 'Acetylcholine', ['SER#2', 'SRA#11']).
neuron(20, 'AIYR', 'Acetylcholine', ['SER#2', 'SRA#11']).
neuron(21, 'AIZL', 'null', ['SER#2']).
neuron(22, 'AIZR', 'null', ['SER#2']).
neuron(23, 'ALA', 'null', ['SRA#10']).
neuron(24, 'ALML', 'Glutamate', ['MEC#2', 'MEC#4', 'MEC#10', 'MEC#9', 'MEC#6', 'DEG#3', 'DES#2', 'GLR#8', 'DOP#1']).
neuron(25, 'ALMR', 'Glutamate', ['MEC#2', 'MEC#4', 'MEC#10', 'MEC#9', 'MEC#6', 'DEG#3', 'DES#2', 'GLR#8', 'DOP#1']).
neuron(26, 'ALNL', 'Acetylcholine', ['SER#2', 'DOP#1', 'GCY#35']).
neuron(27, 'ALNR', 'Acetylcholine', ['SER#2', 'DOP#1', 'GCY#35']).
neuron(28, 'AQR', 'null', ['GCY#32', 'NPR#1', 'GCY#35']).
neuron(29, 'AS1', 'Acetylcholine', ['null']).
neuron(30, 'AS10', 'Acetylcholine', ['null']).
neuron(31, 'AS11', 'Acetylcholine', ['null']).
neuron(32, 'AS2', 'Acetylcholine', ['null']).
neuron(33, 'AS3', 'Acetylcholine', ['null']).
neuron(34, 'AS4', 'Acetylcholine', ['null']).
neuron(35, 'AS5', 'Acetylcholine', ['null']).
neuron(36, 'AS6', 'Acetylcholine', ['null']).
neuron(37, 'AS7', 'Acetylcholine', ['null']).
neuron(38, 'AS8', 'Acetylcholine', ['null']).
neuron(39, 'AS9', 'Acetylcholine', ['null']).
neuron(40, 'ASEL', 'null', ['GCY#6', 'GCY#7', 'OSM#9', 'GCY#12', 'DOP#3']).
neuron(41, 'ASER', 'null', ['GCY#5', 'OSM#9', 'GCY#12', 'DOP#3']).
neuron(42, 'ASGL', 'null', ['OSM#9', 'NPR#1']).
neuron(43, 'ASGR', 'null', ['NPR#1', 'OSM#9']).
neuron(44, 'ASHL', 'Glutamate', ['OSM#9', 'OCR#2', 'SRA#6', 'SRB#6', 'NPR#1', 'UNC#8']).
neuron(45, 'ASHR', 'Glutamate', ['OSM#9', 'OCR#2', 'SRA#6', 'SRB#6', 'NPR#1', 'UNC#8']).
neuron(46, 'ASIL', 'null', ['SRD#1', 'STR#2', 'STR#3', 'DAF#11', 'SRA#6']).
neuron(47, 'ASIR', 'null', ['SRD#1', 'STR#2', 'STR#3', 'DAF#11', 'SRA#6']).
neuron(48, 'ASJL', 'null', ['OSM#9', 'SRE#1', 'DAF#11']).
neuron(49, 'ASJR', 'null', ['OSM#9', 'SRE#1', 'DAF#11']).
neuron(50, 'ASKL', 'Glutamate', ['OSM#9', 'SRA#7', 'SRA#9', 'SRG#2', 'SRG#8', 'DAF#11']).
neuron(51, 'ASKR', 'Glutamate', ['OSM#9', 'SRA#7', 'SRA#9', 'SRG#2', 'SRG#8', 'DAF#11']).
neuron(52, 'AUAL', 'Glutamate', ['GLR#4', 'NPR#1', 'SER#2', 'DOP#1', 'SER#2']).
neuron(53, 'AUAR', 'Glutamate', ['GLR#4', 'NPR#1', 'SER#2', 'DOP#1', 'SER#2']).
neuron(54, 'AVAL', 'FMRFamide', ['GLR#1', 'GLR#2', 'GLR#4', 'GLR#5', 'NMR#1', 'GGR#3', 'GGR#2']).
neuron(55, 'AVAR', 'FMRFamide', ['GLR#1', 'GLR#2', 'GLR#4', 'GLR#5', 'NMR#1', 'GGR#3', 'GGR#2']).
neuron(56, 'AVBL', 'null', ['GLR#1', 'GLR#5', 'SRA#11', 'GGR#3', 'UNC#8', 'GGR#3']).
neuron(57, 'AVBR', 'null', ['GLR#1', 'GLR#5', 'SRA#11', 'GGR#3', 'UNC#8', 'GGR#3']).
neuron(58, 'AVDL', 'Glutamate', ['GLR#1', 'GLR#2', 'GLR#5', 'NMR#1', 'NMR#2', 'UNC#8']).
neuron(59, 'AVDR', 'Glutamate', ['GLR#1', 'GLR#2', 'GLR#5', 'NMR#1', 'NMR#2', 'UNC#8']).
neuron(60, 'AVEL', 'FMRFamide', ['GLR#1', 'GLR#2', 'GLR#5', 'NMR#1', 'NMR#2']).
neuron(61, 'AVER', 'FMRFamide', ['GLR#1', 'GLR#2', 'GLR#5', 'NMR#1', 'NMR#2']).
neuron(62, 'AVFL', 'null', ['null']).
neuron(63, 'AVFR', 'null', ['null']).
neuron(64, 'AVG', 'null', ['GLR#1', 'GLR#2', 'NMR#1', 'NMR#2', 'DEG#3']).
neuron(65, 'AVHL', 'null', ['GLR#4', 'SER#2', 'GGR#1']).
neuron(66, 'AVHR', 'null', ['GLR#4', 'SER#2', 'GGR#1']).
neuron(67, 'AVJL', 'Glutamate', ['GLR#1']).
neuron(68, 'AVJR', 'Glutamate', ['GLR#1']).
neuron(69, 'AVKL', 'FMRFamide', ['GLR#5']).
neuron(70, 'AVKR', 'FMRFamide', ['GLR#5']).
neuron(71, 'AVL', 'GABA', ['null']).
neuron(72, 'AVM', 'Glutamate', ['MEC#2', 'MEC#4', 'MEC#10', 'MEC#9', 'MEC#6', 'DOP#1', 'GCY#35']).
neuron(73, 'AWAL', 'null', ['ODR#10', 'OSM#9', 'OCR#1', 'OCR#2']).
neuron(74, 'AWAR', 'null', ['ODR#10', 'OSM#9', 'OCR#1', 'OCR#2']).
neuron(75, 'AWBL', 'null', ['STR#1', 'DAF#11', 'AEX#2']).
neuron(76, 'AWBR', 'null', ['STR#1', 'DAF#11', 'AEX#2']).
neuron(77, 'AWCL', 'null', ['OSM#9', 'DAF#11', 'STR#2', 'GCY#12']).
neuron(78, 'AWCR', 'null', ['OSM#9', 'DAF#11', 'STR#2', 'GCY#12']).
neuron(79, 'BAGL', 'null', ['GCY#33']).
neuron(80, 'BAGR', 'null', ['GCY#33']).
neuron(81, 'BDUL', 'null', ['GLR#8']).
neuron(82, 'BDUR', 'null', ['GLR#8', 'SER#2', 'GCY#35']).
neuron(83, 'CANL*', 'Monoamine', ['SER#2', 'GGR#2']).
neuron(84, 'CANR*', 'Monoamine', ['SER#2', 'GGR#2']).
neuron(85, 'CEPDL', 'Dopamine', ['DOP#2']).
neuron(86, 'CEPDR', 'Dopamine', ['DOP#2']).
neuron(87, 'CEPVL', 'Dopamine', ['DOP#2']).
neuron(88, 'CEPVR', 'Dopamine', ['DOP#2']).
neuron(89, 'DA1', 'Acetylcholine', ['UNC#8']).
neuron(90, 'DA2', 'Acetylcholine', ['UNC#8']).
neuron(91, 'DA3', 'Acetylcholine', ['UNC#8']).
neuron(92, 'DA4', 'Acetylcholine', ['UNC#8']).
neuron(93, 'DA5', 'Acetylcholine', ['UNC#8']).
neuron(94, 'DA6', 'Acetylcholine', ['UNC#8']).
neuron(95, 'DA7', 'Acetylcholine', ['UNC#8']).
neuron(96, 'DA8', 'Acetylcholine', ['UNC#8']).
neuron(97, 'DA9', 'Acetylcholine', ['SER#2']).
neuron(98, 'DB1', 'Acetylcholine', ['null']).
neuron(99, 'DB2', 'Acetylcholine', ['null']).
neuron(100, 'DB3', 'Acetylcholine', ['null']).
neuron(101, 'DB4', 'Acetylcholine', ['null']).
neuron(102, 'DB5', 'Acetylcholine', ['null']).
neuron(103, 'DB6', 'Acetylcholine', ['null']).
neuron(104, 'DB7', 'Acetylcholine', ['null']).
neuron(105, 'DD1', 'GABA', ['NPR#1', 'GGR#2', 'UNC#8']).
neuron(106, 'DD2', 'GABA', ['NPR#1', 'GGR#2', 'UNC#8']).
neuron(107, 'DD3', 'GABA', ['NPR#1', 'GGR#2', 'UNC#8']).
neuron(108, 'DD4', 'GABA', ['NPR#1', 'GGR#2', 'UNC#8']).
neuron(109, 'DD5', 'GABA', ['NPR#1', 'GGR#2', 'UNC#8']).
neuron(110, 'DD6', 'GABA', ['NPR#1', 'GGR#2', 'UNC#8']).
neuron(111, 'DVA', 'null', ['GLR#4', 'GLR#5', 'NMR#1', 'SER#2', 'SER#4', 'GGR#3', 'GGR#2']).
neuron(112, 'DVB', 'GABA', ['null']).
neuron(113, 'DVC', 'null', ['GLR#1', 'SER#4']).
neuron(114, 'FLPL', 'Glutamate', ['OSM#9', 'DEG#3', 'DES#2', 'GLR#4', 'MEC#10', 'DEL#1', 'UNC#8']).
neuron(115, 'FLPR', 'Glutamate', ['OSM#9', 'DEG#3', 'DES#2', 'GLR#4', 'MEC#10', 'DEL#1', 'UNC#8']).
neuron(116, 'HSNL', 'Serotonin', ['MEC#6', 'GAR#2', 'GLR#5', 'GGR#2']).
neuron(116, 'HSNL', 'Acetylcholine', ['MEC#6', 'GAR#2', 'GLR#5', 'GGR#2']).
neuron(117, 'HSNR', 'Acetylcholine', ['MEC#6', 'GAR#2', 'GLR#5', 'GGR#2']).
neuron(117, 'HSNR', 'Serotonin', ['MEC#6', 'GAR#2', 'GLR#5', 'GGR#2']).
neuron(118, 'I1L', 'Acetylcholine', ['GLR#7', 'GLR#8', 'ACM#2']).
neuron(119, 'I1R', 'Acetylcholine', ['GLR#7', 'GLR#8', 'ACM#2']).
neuron(120, 'I2L', 'null', ['GLR#7', 'GLR#8', 'ACM#2', 'SER#7b']).
neuron(121, 'I2R', 'null', ['GLR#7', 'GLR#8', 'ACM#2', 'SER#7b']).
neuron(122, 'I3', 'null', ['GLR#7', 'GLR7b', 'AEX#2']).
neuron(123, 'I4', 'null', ['null']).
neuron(124, 'I5', 'Serotonin', ['null']).
%neuron(124, 'I5', 'Glutamate', ['null']).
neuron(125, 'I6', 'Acetylcholine', ['GLR#7', 'GLR#b8', 'SER#7b']).
neuron(126, 'IL1DL', 'Glutamate', ['DEG#3', 'MEC#6']).
neuron(127, 'IL1DR', 'Glutamate', ['DEG#3', 'MEC#6']).
neuron(128, 'IL1L', 'Glutamate', ['DEG#3', 'MEC#6']).
neuron(129, 'IL1R', 'Glutamate', ['DEG#3', 'MEC#6']).
neuron(130, 'IL1VL', 'Glutamate', ['DEG#3', 'MEC#6']).
neuron(131, 'IL1VR', 'Glutamate', ['DEG#3', 'MEC#6']).
neuron(132, 'IL2DL', 'null', ['DES#2']).
neuron(133, 'IL2DR', 'null', ['DES#2']).
neuron(134, 'IL2L', 'Acetylcholine', ['NPR#1']).
neuron(135, 'IL2R', 'Acetylcholine', ['NPR#1']).
neuron(136, 'IL2VL', 'null', ['DES#2']).
neuron(137, 'IL2VR', 'null', ['DES#2']).
neuron(138, 'LUAL', 'Glutamate', ['GLR#5', 'SER#2']).
neuron(139, 'LUAR', 'Glutamate', ['GLR#5', 'SER#2']).
neuron(140, 'M1', 'Acetylcholine', ['GLR#2', 'AVR#14']).
neuron(141, 'M2L', 'Acetylcholine', ['SER#7b']).
neuron(142, 'M2R', 'Acetylcholine', ['SER#7b']).
neuron(143, 'M3L', 'Glutamate', ['GLR#8', 'NPR#1']).
neuron(144, 'M3R', 'Glutamate', ['GLR#8', 'NPR#1']).
neuron(145, 'M4', 'Acetylcholine', ['SER7b', 'ACM#2', 'GLR#8']).
neuron(146, 'M5', 'Acetylcholine', ['GLR#8']).
neuron(147, 'MCL', 'Acetylcholine', ['GLR#8', 'SER#7']).
neuron(148, 'MCR', 'Acetylcholine', ['GLR#8', 'SER#7']).
neuron(149, 'MI', 'null', ['GLR#2 ']).
neuron(150, 'NSML', 'Serotonin', ['GLR#7', 'GLR#8', 'SER#2', 'AEX#2']).
neuron(150, 'NSML', 'Glutamate', ['GLR#7', 'GLR#8', 'SER#2', 'AEX#2']).
neuron(151, 'NSMR', 'Serotonin', ['GLR#7', 'GLR#8', 'SER#2', 'AEX#2']).
neuron(151, 'NSMR', 'Glutamate', ['GLR#7', 'GLR#8', 'SER#2', 'AEX#2']).
neuron(152, 'OLLL', 'Glutamate', ['SER#2']).
neuron(153, 'OLLR', 'Glutamate', ['SER#2']).
neuron(154, 'OLQDL', 'Glutamate', ['OSM#9', 'OCR#4', 'NPR#1']).
neuron(155, 'OLQDR', 'Glutamate', ['OSM#9', 'OCR#4', 'NPR#1']).
neuron(156, 'OLQVL', 'Glutamate', ['OSM#9', 'OCR#4', 'NPR#1']).
neuron(157, 'OLQVR', 'Glutamate', ['OSM#9', 'OCR#4', 'NPR#1']).
neuron(158, 'PDA', 'null', ['EXP#1', 'UNC#8', 'SER#2']).
neuron(159, 'PDB', 'FMRFamide', ['UNC#8']).
neuron(160, 'PDEL', 'Dopamine', ['DOP#2']).
neuron(161, 'PDER', 'Dopamine', ['DOP#2']).
neuron(162, 'PHAL', 'null', ['GCY#12', 'OSM#9', 'OCR#2', 'SRG#13', 'SRB#6', 'NPR#1']).
neuron(163, 'PHAR', 'null', ['GCY#12', 'OSM#9', 'OCR#2', 'SRG#13', 'SRB#6', 'NPR#1']).
neuron(164, 'PHBL', 'Serotonin', ['OSM#9', 'OCR#2', 'SRB#6', 'NPR#1']).
neuron(165, 'PHBR', 'Serotonin', ['OSM#9', 'OCR#2', 'SRB#6', 'NPR#1']).
neuron(166, 'PHCL', 'null', ['DOP#1']).
neuron(167, 'PHCR', 'null', ['DOP#1']).
neuron(168, 'PLML', 'Glutamate', ['MEC#2', 'MEC#4', 'MEC#6', 'MEC#9DES#2', 'DOP#1']).
neuron(169, 'PLMR', 'Glutamate', ['MEC#2', 'MEC#4', 'MEC#6', 'MEC#9', 'DES#2', 'DOP#1']).
neuron(170, 'PLNL', 'Acetylcholine', ['DOP#1', 'GCY#35']).
neuron(171, 'PLNR', 'Acetylcholine', ['DOP#1', 'GCY#35']).
neuron(172, 'PQR', 'null', ['GCY#32', 'NPR#1', 'GCY#35 ']).
neuron(173, 'PVCL', 'null', ['DEG#3', 'SER#2']).
neuron(174, 'PVCR', 'null', ['DEG#3', 'SER#2']).
neuron(175, 'PVDL', 'Glutamate', ['MEC#10', 'MEC#9', 'MEC#6', 'OSM#9', 'SER#2', 'DEG#3', 'DOP#3']).
neuron(176, 'PVDR', 'Glutamate', ['MEC#10', 'MEC#9', 'MEC#6', 'OSM#9', 'SER#2', 'DEG#3', 'DOP#3']).
neuron(177, 'PVM', 'null', ['GAR#1', 'MEC#2', 'MEC#4', 'MEC#10', 'MEC#9']).
neuron(178, 'PVNL', 'null', ['null']).
neuron(179, 'PVNR', 'null', ['null']).
neuron(180, 'PVPL', 'null', ['null']).
neuron(181, 'PVPR', 'null', ['null']).
neuron(182, 'PVQL', 'null', ['GLR#1', 'GLR#5', 'SRA#6', 'DOP#1', 'GGR#1']).
neuron(183, 'PVQR', 'null', ['GLR#1', 'GLR#5', 'SRA#6', 'DOP#1', 'GGR#1']).
neuron(184, 'PVR', 'Glutamate', ['GGR#1']).
neuron(185, 'PVT', 'null', ['SER#2', 'SER#4']).
neuron(186, 'PVWL', 'null', ['null']).
neuron(187, 'PVWR', 'null', ['null']).
neuron(188, 'RIAL', 'null', ['Glr#3', 'GLR#6', 'SER#2']).
neuron(189, 'RIAR', 'null', ['Glr#3', 'GLR#6', 'SER#2']).
neuron(190, 'RIBL', 'null', ['DOP#1']).
neuron(191, 'RIBR', 'null', ['DOP#1']).
neuron(192, 'RICL', 'Octapamine', ['DOP#3', 'SER#2']).
neuron(193, 'RICR', 'Octapamine', ['DOP#3', 'SER#2']).
neuron(194, 'RID', 'GABA', ['EXP#1', 'SER#2']).
neuron(195, 'RIFL', 'null', ['null']).
neuron(196, 'RIFR', 'null', ['null']).
neuron(197, 'RIGL', 'FRMFemide', ['null']).
neuron(198, 'RIGR', 'FRMFemide', ['null']).
neuron(199, 'RIH', 'Serotonin', ['null']).
neuron(200, 'RIML', 'Tyramine', ['DOP#1']).
neuron(200, 'RIML', 'Acetylcholine', ['DOP#1']).
neuron(201, 'RIMR', 'Tyramine', ['DOP#1']).
neuron(201, 'RIMR', 'Acetylcholine', ['DOP#1']).
neuron(202, 'RIPL', 'Serotonin', ['null']).
neuron(203, 'RIPR', 'Serotonin', ['null']).
neuron(204, 'RIR', 'null', ['null']).
neuron(205, 'RIS', 'GABA', ['GLR#1', 'SER#4', 'DOP#1']).
neuron(206, 'RIVL', 'null', ['null']).
neuron(207, 'RIVR', 'null', ['null']).
neuron(208, 'RMDDL', 'Acetylcholine', ['null']).
neuron(209, 'RMDDR', 'Acetylcholine', ['null']).
neuron(210, 'RMDL', 'Acetylcholine', ['null']).
neuron(211, 'RMDR', 'Acetylcholine', ['null']).
neuron(212, 'RMDVL', 'Acetylcholine', ['null']).
neuron(213, 'RMDVR', 'Acetylcholine', ['null']).
neuron(214, 'RMED', 'GABA', ['AVR#15', 'SER#2']).
neuron(215, 'RMEL', 'GABA', ['GLR#1', 'SER#2']).
neuron(216, 'RMER', 'GABA', ['GLR#1', 'SER#2']).
neuron(217, 'RMEV', 'GABA', ['AVR#15', 'SER#2']).
neuron(218, 'RMFL', 'null', ['null']).
neuron(219, 'RMFR', 'null', ['null']).
neuron(220, 'RMGL', 'FRMFemide', ['null']).
neuron(221, 'RMGR', 'FRMFemide', ['null']).
neuron(222, 'RMHL', 'null', ['null']).
neuron(223, 'RMHR', 'null', ['null']).
neuron(224, 'SAADL', 'Acetylcholine', ['null']).
neuron(225, 'SAADR', 'Acetylcholine', ['null']).
neuron(226, 'SAAVL', 'Acetylcholine', ['null']).
neuron(227, 'SAAVR', 'Acetylcholine', ['null']).
neuron(228, 'SABD', 'Acetylcholine', ['EXP#1', 'SER#2']).
neuron(229, 'SABVL', 'Acetylcholine', ['DEL#1', 'SER#2']).
neuron(230, 'SABVR', 'Acetylcholine', ['DEL#1', 'SER#2']).
neuron(231, 'SDQL', 'Acetylcholine', ['GCY#35', 'SER#2']).
neuron(232, 'SDQR', 'Acetylcholine', ['GCY#35', 'SER#2']).
neuron(233, 'SIADL', 'Acetylcholine', ['DOP#3', 'GGR#3', 'GGR#2', 'SER#2']).
neuron(234, 'SIADR', 'Acetylcholine', ['DOP#3', 'GGR#3', 'GGR#2', 'SER#2']).
neuron(235, 'SIAVL', 'Acetylcholine', ['GGR#2', 'DOP#3', 'SER#2']).
neuron(236, 'SIAVR', 'Acetylcholine', ['GGR#2', 'DOP#3', 'SER#2']).
neuron(237, 'SIBDL', 'Acetylcholine', ['null']).
neuron(238, 'SIBDR', 'Acetylcholine', ['null']).
neuron(239, 'SIBVL', 'Acetylcholine', ['null']).
neuron(240, 'SIBVR', 'Acetylcholine', ['null']).
neuron(241, 'SMBDL', 'Acetylcholine', ['null']).
neuron(242, 'SMBDR', 'Acetylcholine', ['null']).
neuron(243, 'SMBVL', 'Acetylcholine', ['null']).
neuron(244, 'SMBVR', 'Acetylcholine', ['null']).
neuron(245, 'SMDDL', 'Acetylcholine', ['GGR#2', 'GGR#3']).
neuron(246, 'SMDDR', 'Acetylcholine', ['GGR#2', 'GGR#3']).
neuron(247, 'SMDVL', 'Acetylcholine', ['GGR#1', 'GGR#2']).
neuron(248, 'SMDVR', 'Acetylcholine', ['GGR#1', 'GGR#2']).
neuron(249, 'URADL', 'Acetylcholine', ['null']).
neuron(250, 'URADR', 'Acetylcholine', ['null']).
neuron(251, 'URAVL', 'Acetylcholine', ['null']).
neuron(252, 'URAVR', 'Acetylcholine', ['null']).
neuron(253, 'URBL', 'Acetylcholine', ['null']).
neuron(254, 'URBR', 'Acetylcholine', ['null']).
neuron(255, 'URXL', 'null', ['GCY#32', 'GCY#35', 'NPR#1', 'SRA#10']).
neuron(256, 'URXR', 'null', ['GCY#32', 'GCY#35', 'NPR#1', 'SRA#10']).
neuron(257, 'URYDL', 'null', ['null']).
neuron(258, 'URYDR', 'null', ['null']).
neuron(259, 'URYVL', 'null', ['null']).
neuron(260, 'URYVR', 'null', ['null']).
neuron(261, 'VA1', 'Acetylcholine', ['DEL#1']).
neuron(262, 'VA10', 'Acetylcholine', ['DEL#1']).
neuron(263, 'VA11', 'Acetylcholine', ['DEL#1']).
neuron(264, 'VA12', 'Acetylcholine', ['DEL#1']).
neuron(265, 'VA2', 'Acetylcholine', ['DEL#1']).
neuron(266, 'VA3', 'Acetylcholine', ['DEL#1']).
neuron(267, 'VA4', 'Acetylcholine', ['DEL#1']).
neuron(268, 'VA5', 'Acetylcholine', ['DEL#1']).
neuron(269, 'VA6', 'Acetylcholine', ['DEL#1']).
neuron(270, 'VA7', 'Acetylcholine', ['DEL#1']).
neuron(271, 'VA8', 'Acetylcholine', ['DEL#1']).
neuron(272, 'VA9', 'Acetylcholine', ['DEL#1']).
neuron(273, 'VB1', 'Acetylcholine', ['DEL#1']).
neuron(274, 'VB10', 'Acetylcholine', ['DEL#1']).
neuron(275, 'VB11', 'Acetylcholine', ['DEL#1']).
neuron(276, 'VB2', 'Acetylcholine', ['DEL#1']).
neuron(277, 'VB3', 'Acetylcholine', ['DEL#1']).
neuron(278, 'VB4', 'Acetylcholine', ['DEL#1']).
neuron(279, 'VB5', 'Acetylcholine', ['DEL#1']).
neuron(280, 'VB6', 'Acetylcholine', ['DEL#1']).
neuron(281, 'VB7', 'Acetylcholine', ['DEL#1']).
neuron(282, 'VB8', 'Acetylcholine', ['DEL#1']).
neuron(283, 'VB9', 'Acetylcholine', ['DEL#1']).
neuron(284, 'VC1', 'Acetylcholine', ['GLR#5']).
neuron(284, 'VC1', 'Serotonin', ['GLR#5']).
neuron(285, 'VC2', 'Acetylcholine', ['GLR#5']).
neuron(285, 'VC2', 'Serotonin', ['GLR#5']).
neuron(286, 'VC3', 'Acetylcholine', ['GLR#5']).
neuron(286, 'VC3', 'Serotonin', ['GLR#5']).
neuron(287, 'VC4', 'Acetylcholine', ['GLR#5']).
neuron(287, 'VC4', 'Serotonin', ['GLR#5']).
neuron(288, 'VC5', 'Acetylcholine', ['GLR#5']).
neuron(288, 'VC5', 'Serotonin', ['GLR#5']).
neuron(289, 'VC6', 'Acetylcholine', ['GLR#5']).
neuron(289, 'VC6', 'Serotonin', ['GLR#5']).
neuron(290, 'VD1', 'GABA', ['NPR#1']).
neuron(291, 'VD10', 'GABA', ['NPR#1']).
neuron(292, 'VD11', 'GABA', ['NPR#1']).
neuron(293, 'VD12', 'GABA', ['NPR#1']).
neuron(294, 'VD13', 'GABA', ['NPR#1']).
neuron(295, 'VD2', 'GABA', ['NPR#1']).
neuron(296, 'VD3', 'GABA', ['NPR#1']).
neuron(297, 'VD4', 'GABA', ['NPR#1']).
neuron(298, 'VD5', 'GABA', ['NPR#1']).
neuron(299, 'VD6', 'GABA', ['NPR#1']).
neuron(300, 'VD7', 'GABA', ['NPR#1']).
neuron(301, 'VD8', 'GABA', ['NPR#1']).
neuron(302, 'VD9', 'GABA', ['NPR#1']).


%TRANSMITTERS:
process_missing_transmitters:-
	neuron(_ID, OrigNeuron, _NT, _L),
	findall(Receptors, (synapse(OrigNeuron, RNeuron, _), neuron(_, RNeuron, 'null', Receptors)), RNs),
	prepare_element_list(RNs, RNNew),
	correspond_transmitter(RNNew, PossibleTransmitters),
	output_nicely(OrigNeuron, PossibleTransmitters),
	fail.
process_missing_transmitters.

correspond_transmitter(RNs, TRs):-
	correspond_transmitter(RNs, [], TRsTemp),
	flatten(TRsTemp, TRs).
correspond_transmitter([], TRs, TRs).
correspond_transmitter([H|T], AccTRs, TRs):-
	findall(Transmitter, transmit_recept(Transmitter, H, _), Transmitters),
	correspond_transmitter(T, [Transmitters| AccTRs], TRs).

%RECEPTORS:
process_missing_receptors:-
	neuron(_ID, OrigNeuron, _NT, _L),
	findall(Transmitter, (synapse(OrigNeuron, RNeuron, _), neuron(_, RNeuron, Transmitter, ['null'])), TRs),
	prepare_element_list(TRs, TRNew),
	correspond_receptor(TRNew, PossibleReceptors),
	output_nicely(OrigNeuron, PossibleReceptors),
	fail.
process_missing_receptors.

correspond_receptor(TRs, RNs):-
	correspond_receptor(TRs, [], RNsTemp),
	flatten(RNsTemp, RNs).
correspond_receptor([], TRs, TRs).
correspond_receptor([H|T], AccTRs, TRs):-
	findall(Receptor, transmit_recept(H, Receptor, _), Receptors),
	correspond_receptor(T, [Receptors| AccTRs], TRs).

%GENERAL FUNCTIONS:
prepare_element_list(RNs, RNNew):-
	flatten(RNs, RNFlat),
	prepare_element_list(RNFlat, [], RNNew).

prepare_element_list([], L, L).
prepare_element_list([H|T], AccList, RNnew):-
	\+ memberchk(H, AccList),  !,
	prepare_element_list(T, [H|AccList], RNnew).
prepare_element_list([H|T], AccList, RNnew):-
	prepare_element_list(T, AccList, RNnew).

count(Nj, L, C):-
	count(Nj, L, C, 0).
count(_Nj, [], C, C):-!.
count(Nj, [H| T], CountNj, Acc):-
	(Nj == H ->
		AccNew is Acc + 1
	;
		AccNew is Acc
	),
	count(Nj, T, CountNj, AccNew).

counted_single_list(Orig, Res):-
	csl(Orig, [], [], Res).

csl([], _, Res, Res):-!.
csl([H|T], SeenList, AccCountedList, Res):-
	\+ memberchk(H, SeenList), !,
	count(H, T, C),
	C_and_self is C+1,
	csl(T, [H|SeenList], [[H,C_and_self]| AccCountedList], Res).
csl([H|T], SeenList, AccCountedList, Res):-
	memberchk(H, SeenList),
	csl(T, SeenList, AccCountedList, Res).

output_nicely(Neuron, PossibleTransmitters):-
	write('--For neuron '), write(Neuron), writeln(': '),
	counted_single_list(PossibleTransmitters, CountedList),
	printout_nicely(CountedList),
	write('--END of neuron '), writeln(Neuron).

printout_nicely([]).
printout_nicely([[Transmitter, Count]|Rest]):-
	write(Transmitter), write(' - '), writeln(Count),
	printout_nicely(Rest).


:-writeln('Processing Unknown Transmitters:'), process_missing_transmitters.
:-writeln('').
:-writeln('Processing Unknown Receptors:'), process_missing_receptors.