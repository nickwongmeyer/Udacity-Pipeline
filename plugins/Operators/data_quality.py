from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 query_tested="",
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.query_tested = query_tested
        

    def execute(self, context):
        
        self.log.info('Getting credentials')
        reshift_hook= PostgresHook(postgres_conn_id=self.redshift_conn_id)
        records =reshift_hook.get_records(self.query_tested)
        if len(records) < 1 or len(records[0]) < 1:
            raise ValueError(f" failure of Data Quality Check")
        num_records =records[0][0]
        if num_records <1:
            raise ValueError(f"failure of Data Quality Check")
        self.log.info(f"Data quality check success")
            
            dq_checks=[
        {'check_sql': "SELECT COUNT(*) FROM users WHERE userid is null", 'expected_result': 0},
