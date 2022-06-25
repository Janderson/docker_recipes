## docker_recipies


### docker-oracle 
`docker-compose run app bash`

*Altera sessao:*  
> ALTER session SET current_schema='schema'; 


*Pede a explicação:*  
`explain plan SET STATEMENT_ID='JJ_EXPLAIN' for 
(
    SELECT * FROM user
    WHERE 'J'='J'
);`

Ctrl+Enter  

*Ver o resultado:*   
`SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE','JJ_EXPLAIN', 'ALL'));`
