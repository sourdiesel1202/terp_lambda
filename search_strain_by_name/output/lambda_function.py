from functions import open_rds_connection
import json, logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    This function searches for strains given an input name string i.e. orte, northe, etc
    """
    request_data = event['queryStringParameters']
    search_string = request_data['query']
    # vertical = request_data['vertical/']


    # message = event['Records'][0]['body']
    # data = json.loads(message)
    # CustID = data['CustID']
    # Name = data['Name']

    # item_count = 0
    # sql_string = f"insert into Customer (CustID, Name) values({CustID}, '{Name}')"
    conn = open_rds_connection()

    with conn.cursor() as cur:
        # cur.execute("create table if not exists Customer ( CustID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (CustID))")
        sql = f"""select s.id, s.name, s.url, s.description, s.image, s.type, s.aliases, group_concat(distinct tt.name separator  ',') terpenes,group_concat(distinct sp.name separator  ',') parents,group_concat(distinct sc.name separator  ',') children from strains_strain s
    left join strains_strain_terpenes st on st.strain_id = s.id
    left join terpenes_terpene tt on st.terpene_id = tt.id
    -- get children
    left join strains_strain_children ssc on ssc.from_strain_id = s.id
    left join strains_strain sc on (sc.id = ssc.to_strain_id)

    left join strains_strain_parents ssp on ssp.from_strain_id = s.id
    left join strains_strain sp on (sp.id = ssp.to_strain_id)

where lower(s.name) like lower('%ortega%') group by s.id, s.name, s.url, s.description, s.image, s.type, s.aliases"""
        cur.execute(sql)
        # cur.execute(sql % UserId)
        columns = [field_md[0] for field_md in cur.description]
        json_result=[]
        for row in cur:
            json_entry = {}
            for field in columns:
                if field in ['aliases', 'parents', 'children','terpenes']:
                    json_entry[field] = row[columns.index(field)].split(",") if row[columns.index(field)] is not None else ''
                else:
                    json_entry[field] = row[columns.index(field)] if row[columns.index(field)] is not None else ''
            json_result.append(json_result)
    # conn.commit()
        return {'statusCode': 200,
                'headers': {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": 'GET, POST, PUT, DELETE, OPTIONS',
                    "content-type": "application/json"
                },
                'body': json_result
                }
        # return "Added %d items to RDS MySQL table" %(item_count)