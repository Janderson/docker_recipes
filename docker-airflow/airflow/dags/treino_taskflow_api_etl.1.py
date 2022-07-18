from unicodedata import name
from airflow.decorators import dag, task
import pendulum, json
from datetime import datetime
from airflow.operators.python import get_current_context
from airflow.models import Variable


# criar um dag usando o decorator
    # ==> CÓDIGO AQUI
@dag(
    catchup=False,
    tags=["treinos", "garra"],
    start_date=pendulum.datetime(2022,5,3),
    schedule_interval="@hourly",
    default_args = {"env": "dev"}
)
def treino_taskflow_api_etl1():
  

    @task(task_id="extractor")
    def extract(variables):
        filename = variables.get("filename")
        if filename is None:
            data = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
            return json.loads(data)
        else:
            with open(f"/app/data/{filename}", "r") as r:
                return json.loads(r.read())

    # criar um task extract usando o decorator
    # ==> CÓDIGO AQUI

    # converter data_string to json '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
    # + retornar no método
    # ==> CÓDIGO AQUI

    # criar um task transform recebe o dict do extract calcula a soma dos values
    # retorna um dict total_order_value
    # ==> CÓDIGO AQUI
    

    # criar um task load total_order_value 

    @task
    def get_context_vars():
        context = get_current_context()
        confs = context["dag_run"].conf
        print("-------current context ------")
        print("-------variable ------")
        print(Variable)
        print(Variable.get("oracle_dev"))
        print(confs)    
        return confs

    # + printa na tela
    # ==> CÓDIGO AQUI


    # chamar ordem do dag extract+transform+load
    # ==> CÓDIGO AQUI
    data = extract(get_context_vars())


# criar dag + metodo
# ==> CÓDIGO AQUI

treino_taskflow_api_etl1 = treino_taskflow_api_etl1()