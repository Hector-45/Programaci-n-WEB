CREATE DATABASE CEUTEC;

CREATE TABLE estudiante(
	id int auto_increment,
	nombre varchar(15),
	apellido varchar(15),
	correo varchar(15),
	edad int,
	carrera varchar(35),
    primary key (id)
);

INSERT INTO 
estudiante(nombre, apellido, correo, edad, carrera) 
VALUES 
("Hector", "lopez","lopez.hector@gmail.com",25,"Ingenieria informatica"),
("Ricardo", "Pastrana","ricardo.pastrana@gmail.com",21,"Ingenieria ambiental"),
("Juan", "Valladares","juan.jose@gmail.com",20,"Ingenieria mecatronica"),
("Miguel", "Rodriguez","miguel.rodriguez@gmail.com",24,"Ingenieria informatica"),
("Manuel", "Baldez","manuel.baldez@gmail.com",23,"Derecho"),
("Fredy", "Garay","fredy.garay@gmail.com",19,"Licenciatura en Mercadotecnia"),
("Rosa", "Martinez","rosa.martinez@gmail.com",25,"Ingenieria informatica"),
("Siria", "cruz","siria.cruz@gmail.com",23,"Ingenieria mecatronica"),
("Melanye", "Ordoñez","melanye.ordonez@gmail.com",21,"Ingenieria informatica"),
("Teresa", "izaguirre","teresa.izaguirre@gmail.com",25,"Ingenieria ambiental")
;