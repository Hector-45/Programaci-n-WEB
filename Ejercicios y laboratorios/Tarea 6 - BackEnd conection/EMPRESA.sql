CREATE DATABASE EMPRESA;
USE EMPRESA;

DROP DATABASE EMPRESA;

CREATE TABLE CLIENTES(
	codCliente int,
    Nombre varchar(25),
    apellidos varchar(25),
    empresa varchar(15),
    puesto varchar(25),
    CP varchar(10),
    provincia varchar(15),
    telefono int(25),
    fechaNacimiento date,
    primary key (codCliente)
);

CREATE TABLE COMPRA(
	-- id int auto_increment,
	codCliente int,
    codArticulo int,
    fecha date,
    unidades int(25),
    -- primary key(id),
    primary key(fecha),
    foreign key (codCliente) references CLIENTES(codCliente),
    foreign key (codArticulo) references ARTICULOS(codArticulo)
);

CREATE TABLE ARTICULOS(
	codArticulo int,
    Nombre varchar(25),
    Descripcion varchar(40),
    precioUnidad int(15),
    unidadesStock int(10),
    stockSeguridad varchar(25),
    imagen varchar(25),
    primary key (codArticulo)
);



