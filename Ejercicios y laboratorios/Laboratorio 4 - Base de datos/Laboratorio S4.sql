CREATE DATABASE LABORATORIO;
USE LABORATORIO;
DROP DATABASE LABORATORIO;

CREATE TABLE genero(
	id_genero int,
    descripcion varchar(45),
    primary key(id_genero)
);

CREATE TABLE grupo(
	id_grupo int,
    nombre VARCHAR(45),
    formacion date,
    desintegracion date,
    primary key(id_grupo)
);

CREATE TABLE generoGrupos(
	id_grupo int,
	id_genero int,
    primary key (id_grupo,id_genero),
	foreign key (id_grupo) references grupo(id_grupo),
	foreign key (id_genero) references genero(id_genero)
);


CREATE TABLE musicosGrupos(
	id_grupo int,
    id_musico int,
    instrumento VARCHAR(45),
    fechaInicio date,
    fechaFin date,
    primary key (id_grupo),
    foreign key (id_musico) REFERENCES grupo(id_grupo)
);

CREATE TABLE musico(
	id_musico int,
    nombre VARCHAR(45),
    instrumento VARCHAR(45),
    lugarNacimiento VARCHAR(45),
    fechaNacimiento date,
    fechaMuerte date,
    primary key (id_musico),
    foreign key (id_musico) references musicosGrupos(id_grupo)
);
