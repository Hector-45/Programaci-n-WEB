-- EJERCICIO_1
CREATE database LIBRERIA;
USE LIBRERIA;

CREATE TABLE LIBROS(
	cod_lib int,
    descripcion varchar(15),
    titulo varchar(30) not null,
    autor varchar(20),
    editorial varchar(15),
    precio float,
    primary key (cod_lib)
);

-- EJERCICIO_2
INSERT INTO 
LIBROS(cod_lib, descripcion, titulo, autor, editorial, precio) 
VALUES 
(100, "Sistemas", "Fundamentos de base de datos","Elmarsi","McGraw Hill",45.00),
(101, "Sistemas", "Sistemas de base de datos","Connolly","Pearson",30),
(302, "Literatura", "Cervantes y el Quijote","Borges","Elmerce",25),
(204, "Matematicas", "Cálculo Diferencial e Integral","Hernandez","Pearson",35.25),
(106, "Literatura", "Aprenda SQL ya","Riordan","McGraw Hill",90.99)
;

-- EJERCICIO_3
DELETE FROM LIBROS WHERE cod_lib=106;

-- EJERCICIO_4
UPDATE LIBROS SET precio=75.00 WHERE cod_lib=100;  

SELECT * FROM LIBROS;
