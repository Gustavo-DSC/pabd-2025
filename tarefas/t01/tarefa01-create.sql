-- Criação das tabelas para o esquema de atividades

CREATE TABLE departamento (
    codigo SERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL,
    cod_gerente INTEGER
);

CREATE TABLE funcionario (
    codigo SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sexo CHAR(1),
    dt_nasc DATE,
    salario DECIMAL(10,2),
    cod_depto INTEGER,
    FOREIGN KEY (cod_depto) REFERENCES departamento(codigo)
);

ALTER TABLE departamento ADD CONSTRAINT fk_gerente
FOREIGN KEY (cod_gerente) REFERENCES funcionario(codigo);

CREATE TABLE projeto (
    codigo SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    cod_depto INTEGER,
    cod_responsavel INTEGER,
    data_inicio DATE,
    data_fim DATE,
    FOREIGN KEY (cod_depto) REFERENCES departamento(codigo),
    FOREIGN KEY (cod_responsavel) REFERENCES funcionario(codigo)
);

CREATE TABLE atividade (
    codigo SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    cod_responsavel INTEGER,
    data_inicio DATE,
    data_fim DATE,
    FOREIGN KEY (cod_responsavel) REFERENCES funcionario(codigo)
);

CREATE TABLE atividade_projeto (
    cod_projeto INTEGER,
    cod_atividade INTEGER,
    PRIMARY KEY (cod_projeto, cod_atividade),
    FOREIGN KEY (cod_projeto) REFERENCES projeto(codigo),
    FOREIGN KEY (cod_atividade) REFERENCES atividade(codigo)
);