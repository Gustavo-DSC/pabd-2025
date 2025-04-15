SELECT f1.nome
FROM funcionario f1
WHERE f1.salario > ALL (
    SELECT f2.salario
    FROM funcionario f2
    WHERE f2.cod_depto = 2
);
