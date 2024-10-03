CREATE DATABASE IF NOT EXISTS usuarios;
use usuarios;


CREATE TABLE IF NOT EXISTS cadastrousuarios(
nome VARCHAR(40),
email VARCHAR(40),
cpf VARCHAR(12),
primary key(cpf)
);