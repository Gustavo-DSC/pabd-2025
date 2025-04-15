SELECT 
    p.codigo,
    p.descricao
FROM 
    projeto p
JOIN 
    departamento d ON p.cod_depto = d.codigo
JOIN 
    funcionario gerente ON d.cod_gerente = gerente.codigo
WHERE 
    gerente.salario = (
        SELECT MAX(f.salario)
        FROM departamento dep
        JOIN funcionario f ON dep.cod_gerente = f.codigo
    );