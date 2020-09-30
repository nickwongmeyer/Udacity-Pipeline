from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 table="",
                 redshift_conn_id="",
                 select_sql = "",
                 append_only=False,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.table=table
        self.redshift_conn_id= redshift_conn_id
        self.select_sql = select_sql
        self.append_only = append_only

    def execute(self, context):
        
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        if self.append_only:
            insert_sql_table =f""" 
               create table stage_{self.table};
            
               insert into stage_{self.table}
               {select.select_sql}
            
               delete from {self.table}
               using stage_{self.table}
               where {self.table}.{self.primary_key} = stage_{self.table}.{self.primary_key};
            
               insert into {self.table}
               select * from stage_{self.table};
            """
        else:
            insert_sql_table =f"""
               insert into {self.table}
               {self.select_sql}
            """
            self.log.info("Delete data from dimension table")
            redshift_hook.run(f"TRUNCATE TABLE {self.table};")      
        
        self.log.info("Data loaded into dimension table into Redshift")
       
        redshift_hook.run(insert_sql_table)
             