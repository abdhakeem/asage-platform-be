from google.cloud import bigquery


# Converts schema dictionary to BigQuery's expected format for job_config.schema
def format_schema(schema):
    formatted_schema = []
    for row in schema:
        formatted_schema.append(bigquery.SchemaField(row['name'], row['type'], row['mode']))
    return formatted_schema


table_schema = {
    "name": "client_id",
    "type": "INTEGER",
    "mode": "REQUIRED"
}, {
    "name": "item",
    "type": "STRING",
    "mode": "NULLABLE"
}, {
    "name": "file_source",
    "type": "STRING",
    "mode": "NULLABLE"
}, {
    "name": "facility",
    "type": "STRING",
    "mode": "NULLABLE"
}, {
    "name": "origin",
    "type": "STRING",
    "mode": "NULLABLE"
}, {
    "name": "destination",
    "type": "STRING",
    "mode": "NULLABLE"
}, {
    "name": "quantity",
    "type": "INTEGER",
    "mode": "NULLABLE"
}, {
    "name": "units",
    "type": "STRING",
    "mode": "NULLABLE"
}, {
    "name": "equipment",
    "type": "STRING",
    "mode": "NULLABLE"
}, {
    "name": "scope_category",
    "type": "INTEGER",
    "mode": "NULLABLE"
}, {
    "name": "scope_sub_category",
    "type": "STRING",
    "mode": "NULLABLE"
}, {
    "name": "process",
    "type": "STRING",
    "mode": "NULLABLE"
}, {
    "name": "calc_method",
    "type": "STRING",
    "mode": "NULLABLE"
}, {
    "name": "ef_source",
    "type": "STRING",
    "mode": "NULLABLE"
}, {
    "name": "ef",
    "type": "FLOAT",
    "mode": "NULLABLE"
}, {
    "name": "emissions",
    "type": "INTEGER",
    "mode": "NULLABLE"
}


class DAO:
    def __init__(self):
        self.client = bigquery.Client(project="polar-equinox-420601")
        self.table = self.client.get_dataset('polar-equinox-420601.aluminium_materials_demo').table(
            'aluminium_materials_demo_v2')
        self.job_config = bigquery.LoadJobConfig()
        self.job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
        self.job_config.schema = format_schema(table_schema)

    def write(self, data):
        job = self.client.load_table_from_json(data, self.table, job_config=self.job_config)
        print(job.result())
