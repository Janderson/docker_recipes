import json
import pendulum
from airflow.decorators import dag, task

# criar um dag usando o decorator
@dag(
    schedule_interval=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["treinos"]
)
def treino_taskflow_api_etl():
    
    # criar um task extract usando o decorator
    @task
    def extract():
        # converter data_string to json '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
        # + retornar no método
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
        order_data_dict = json.loads(data_string)
        return order_data_dict

    # criar um task transform recebe o dict do extract calcula a soma dos values
    # retorna um dict total_order_value
    @task(multiple_outputs=True)
    def transform(order_data_dict: dict):
        #
        total_order_value = 0

        for value in order_data_dict.values():
            total_order_value += value
        
        return {"total_order_value": total_order_value}
    

    # criar um task load total_order_value 
    # + printa na tela
    @task
    def load(total_order_value: float):
        pass
        print(f"Total order value is: {total_order_value:.2f}")
    
    # chamar ordem do dag extract+transform+load
    order_data = extract()
    order_summary = transform(order_data)
    load(order_summary["total_order_value"])


# criar dag + metodo

treino_taskflow_api_etl = treino_taskflow_api_etl()