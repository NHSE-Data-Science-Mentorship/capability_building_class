import os
import pandas as pd
from pyfoundry_sql import connect

from toy_example.constants import ADMITTED_DISCHARGE_DESTINATION
from toy_example.utils import list_to_sql_array


class FoundrySQLWrapper:
    def __init__(
        self,
    ):
        foundry_domain = (os.environ["FOUNDRY_DOMAIN"],)
        foundry_auth_header = (os.environ["FOUNDRY_AUTH_HEADER"],)
        self.conn = connect(foundry_domain, foundry_auth_header)

    def execute_sql_query(self, query_string):
        return pd.read_sql(query_string, self.conn)

    def get_acute_type_one_trusts(self):
        query_string = """
        SELECT organisation_code as location_id
        FROM "/NHS/Locations Ontology/data/objects/nhs_trust"
        WHERE trust_type = 'Acute Trust Type 1'
        """
        location_df = self.execute_sql_query(query_string)

        return location_df["location_id"].values

    def get_ecds(self, location_ids):
        query_string = f"""
            SELECT der_provider_code, age_at_arrival, sex, 
            CASE
                WHEN (discharge_destination_snomed_ct IN {list_to_sql_array(ADMITTED_DISCHARGE_DESTINATION)}) THEN 1
                ELSE 0
            END AS admitted
            FROM "/NHS/NHS: ECDS Patient Level/data/transform/ecds_v2"
            WHERE (der_provider_code IN {list_to_sql_array(location_ids)}) AND (discharge_destination_snomed_ct IS NOT NULL) AND (DATE(arrival_time)>=DATE('2022-03-01')) AND DATE(arrival_time)<=DATE('2022-03-02')
            """

        ecds_df = self.execute_sql_query(query_string)

        return ecds_df
