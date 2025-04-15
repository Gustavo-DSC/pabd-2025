-- Inserção de dados para o esquema de atividades

INSERT INTO departamento (descricao) VALUES 
('TI'),
('Recursos Humanos'),
('Financeiro'),
('Marketing'),
('Produção');

INSERT INTO funcionario (nome, sexo, dt_nasc, salario, cod_depto) VALUES
('João Silva', 'M', '1985-03-15', 7500.00, 1),
('Maria Oliveira', 'F', '1990-07-22', 6500.00, 2),
('Carlos Pereira', 'M', '1982-11-30', 8200.00, 1),
('Ana Santos', 'F', '1992-05-10', 5800.00, 3),
('Pedro Costa', 'M', '1988-09-18', 7100.00, 4),
('Juliana Almeida', 'F', '1995-02-25', 5300.00, 5),
('Marcos Souza', 'M', '1980-12-05', 9000.00, 1),
('Fernanda Lima', 'F', '1987-06-12', 6800.00, 3),
('Ricardo Martins', 'M', '1991-08-20', 6200.00, 2),
('Patrícia Rocha', 'F', '1984-04-08', 7800.00, 4);

UPDATE departamento SET cod_gerente = 1 WHERE codigo = 1;
UPDATE departamento SET cod_gerente = 2 WHERE codigo = 2;
UPDATE departamento SET cod_gerente = 4 WHERE codigo = 3;
UPDATE departamento SET cod_gerente = 5 WHERE codigo = 4;
UPDATE departamento SET cod_gerente = 6 WHERE codigo = 5;

INSERT INTO projeto (nome, descricao, cod_depto, cod_responsavel, data_inicio, data_fim) VALUES
('Sistema ERP', 'Implementação de sistema integrado', 1, 1, '2023-01-15', '2023-12-20'),
('Treinamento RH', 'Programa de capacitação', 2, 2, '2023-03-01', '2023-11-30'),
('Controle Orçamentário', 'Sistema de gestão financeira', 3, 4, '2023-02-10', '2023-10-15'),
('Campanha Publicitária', 'Lançamento novo produto', 4, 5, '2023-04-05', '2023-09-30'),
('Otimização Produção', 'Melhoria processos fabris', 5, 6, '2023-05-20', '2023-12-10');

INSERT INTO atividade (nome, descricao, cod_responsavel, data_inicio, data_fim) VALUES
('Análise Requisitos', 'Levantamento de necessidades', 1, '2023-01-15', '2023-02-28'),
('Desenvolvimento Módulos', 'Programação do sistema', 3, '2023-03-01', '2023-08-31'),
('Treinamento Usuários', 'Capacitação dos funcionários', 2, '2023-09-01', '2023-10-31'),
('Elaboração Relatórios', 'Criação de relatórios gerenciais', 4, '2023-04-01', '2023-07-15'),
('Testes Sistema', 'Validação do sistema', 7, '2023-09-01', '2023-11-15');

INSERT INTO atividade_projeto (cod_projeto, cod_atividade) VALUES
(1, 1),
(1, 2),
(1, 5),
(2, 3),
(3, 4);