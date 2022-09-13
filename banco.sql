CREATE DATABASE IF NOT EXISTS API_a;
use API_a;
CREATE table IF NOT EXISTS associado(
	id_associado int not null primary key auto_increment,
    nome varchar(55),
    email varchar(256),
    sexo varchar(10)
);
Create table IF NOT EXISTS backoffice(
	id_back int not null primary key auto_increment,
    nome varchar(55)
);
Create table IF NOT EXISTS email(
	id_email int not null primary key auto_increment,
    fk_id_associado int,
    corpo varchar(7999),
    pagina varchar(999),
    dataenvio datetime(6),
    estado bool
);
ALTER TABLE email ADD FOREIGN KEY (fk_id_associado) REFERENCES associado(id_associado);

INSERT INTO associado VALUES (0, 'Marcela','marcela@gmail.com','Feminino');
INSERT INTO associado VALUES (0, 'Vitória','marcela@gmail.com','Feminino');