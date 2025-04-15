SELECT 
    p.nome AS nome_projeto,
    p.data_inicio AS inicio_projeto,
    p.data_fim AS fim_projeto,
    a.descricao AS descricao_atividade,
    a.data_inicio AS inicio_atividade,
    a.data_fim AS fim_atividade
FROM 
    projeto p 
JOIN 
    atividade_projeto ap ON p.codigo = ap.cod_projeto
JOIN 
    atividade a ON ap.cod_atividade = a.codigo
ORDER BY 
    p.nome, a.data_inicio;