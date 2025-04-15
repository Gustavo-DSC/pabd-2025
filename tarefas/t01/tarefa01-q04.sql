SELECT f.nome, f.salario, d.descricao AS departamento
FROM funcionario f
LEFT JOIN departamento d ON f.cod_depto = d.codigo
WHERE f.codigo NOT IN (
    SELECT cod_gerente FROM departamento
)
ORDER BY f.cod_depto;
