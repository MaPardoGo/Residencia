from django.db import models

import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import pandas as pd
import os

# Cargar las variables de entorno desde archivo .env
load_dotenv()

# Configuración de la instancia y credenciales
INSTANCE = os.getenv('INSTANCE')
USER = os.getenv('USER')
PASS = os.getenv('PASS')
URL = f'https://{INSTANCE}.service-now.com/api/now/table'

ubicaciones_dict = {
    "202daf7347ac3910d9d3a03a536d4329": "Hospital Del Trabajador",
    "79036756476c3110d9d3a03a536d4325": "Centro Medico",
    "7d036756476c3110d9d3a03a536d4326": "Otec Servicios",
    "e04d9a0f1be53510d5166392b24bcb78": "Centro De Atencion Ambulatoria",
    "f1036756476c3110d9d3a03a536d4326": "Agencia Providencia",
    "f3377b3e47f07d50d9d3a03a536d43d7": "Sala Cuna",
    "f5036756476c3110d9d3a03a536d4327": "Esachs Servicios",
    "f8dc277347ac3910d9d3a03a536d43e6": "Casa Central"
}
company = {
    "b482d6a91b66a8101df3bb7f034bcbf0": "ACHS"
}


def ent_agendador_records(table, value):
    url = f"{URL}/{table}"
    params = {
        'sysparm_query': f'company={value}',
        'sysparm_fields': [],  # Añade aquí los otros campos que necesites
    }
    try:
        response = requests.get(url, auth=HTTPBasicAuth(USER, PASS), params=params)
        if response.status_code == 200:
            records = response.json().get('result', [])
            print(f'Registros obtenidos de {table}: {len(records)}')

            # Modifica el valor de 'task_for' con <value> en cada registro
            for record in records:
                if 'task_for' in record and 'value' in record['task_for']:
                    record['task_for'] = record['task_for']['value']
                else:
                    record['task_for'] = None  # O cualquier valor por defecto que prefieras

            return records
        else:
            print(f"{response.status_code} al obtener registros: {response.text}")
            return []
    except requests.exceptions.Timeout:
        print("Timeout alcanzado al intentar obtener registros")
        return []


def groups_assignament(table):
    url = f"{URL}/{table}"
    params = {
        'sysparm_fields': 'sys_id,name'
    }
    try:
        response = requests.get(url, auth=HTTPBasicAuth(USER, PASS), params=params)
        if response.status_code == 200:
            records = response.json().get('result', [])
            print(f'Registros obtenidos de {table}: {len(records)}')
            return records
        else:
            print(f"{response.status_code} al obtener registros: {response.text}")
            return []
    except requests.exceptions.Timeout:
        print("Timeout alcanzado al intentar obtener registros")
        return []


def cat_groups(table):
    url = f"{URL}/{table}"
    params = {
        'sysparm_fields': 'sys_id,u_tipo,u_modelo'
    }
    try:
        response = requests.get(url, auth=HTTPBasicAuth(USER, PASS), params=params)
        if response.status_code == 200:
            records = response.json().get('result', [])
            print(f'Registros obtenidos de {table}: {len(records)}')
            return records
        else:
            print(f"{response.status_code} al obtener registros: {response.text}")
            return []
    except requests.exceptions.Timeout:
        print("Timeout alcanzado al intentar obtener registros")
        return []

def tables_meta(table):
    url = f"{URL}/{table}"
    params = {
        'sysparm_fields': 'name,label'
    }
    try:
        response = requests.get(url, auth=HTTPBasicAuth(USER, PASS), params=params)
        if response.status_code == 200:
            records = response.json().get('result', [])
            print(f'Registros obtenidos de {table}: {len(records)}')
            return records
        else:
            print(f"{response.status_code} al obtener registros: {response.text}")
            return []
    except requests.exceptions.Timeout:
        print("Timeout alcanzado al intentar obtener registros")
        return []

def all_inc(query,params,table):
    url = f"{URL}/{table}"
    try:
        response = requests.get(url, auth=HTTPBasicAuth(USER, PASS), params=params)
        if response.status_code == 200:
            records = response.json().get('result', [])
            for record in records:
                location_id = record.get('location')
                if isinstance(location_id, dict):  # Verifica si location_id es un diccionario
                    location_id = location_id.get('value')  # Extrae el valor
                if location_id in ubicaciones_dict:
                    record['location'] = ubicaciones_dict[location_id]
                company_id = record.get('company')
                if isinstance(company_id, dict):  # Verifica si location_id es un diccionario
                    company_id = company_id.get('value')  # Extrae el valor
                if company_id in company:
                    record['company'] = company[company_id]
            print(f'Registros obtenidos de {table}: {len(records)}')

            # Modifica el valor de 'task_for' con <value> en cada registro
            for record in records:
                if 'task_for' in record and 'value' in record['task_for']:
                    record['task_for'] = record['task_for']['value']
                else:
                    record['task_for'] = None  # O cualquier valor por defecto que prefieras

            return records
        else:
            print(f"{response.status_code} al obtener registros de {table}: {response.text}")
            return []
    except requests.exceptions.Timeout:
        print(f"Timeout alcanzado al intentar obtener ubicaciones de {table}")
        return []


def all_req(query,params,table):
    url = f"{URL}/{table}"
    try:
        response = requests.get(url, auth=HTTPBasicAuth(USER, PASS), params=params)
        if response.status_code == 200:
            records = response.json().get('result', [])
            for record in records:
                location_id = record.get('location')
                if isinstance(location_id, dict):  # Verifica si location_id es un diccionario
                    location_id = location_id.get('value')  # Extrae el valor
                if location_id in ubicaciones_dict:
                    record['location'] = ubicaciones_dict[location_id]
                company_id = record.get('company')
                if isinstance(company_id, dict):  # Verifica si location_id es un diccionario
                    company_id = company_id.get('value')  # Extrae el valor
                if company_id in company:
                    record['company'] = company[company_id]
            print(f'Registros obtenidos de {table}: {len(records)}')

            # Modifica el valor de 'task_for' con <value> en cada registro
            for record in records:
                if 'task_for' in record and 'value' in record['task_for']:
                    record['task_for'] = record['task_for']['value']
                else:
                    record['task_for'] = None  # O cualquier valor por defecto que prefieras

            return records
        else:
            print(f"{response.status_code} al obtener registros de {table}: {response.text}")
            return []
    except requests.exceptions.Timeout:
        print(f"Timeout alcanzado al intentar obtener ubicaciones de {table}")
        return []

# Guardar lista en planilla.
def save_to_excel(dataframe, output_file='Reporte/Cons_pend_residencia.xlsx'):
    # Abrir un escritor de Excel
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        for sheet_name,dataframe in dataframe.items():
            # Guardar el DataFrame en la hoja
            dataframe.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f'Hoja Excel guardada como {sheet_name}')
        print(f"Archivo guardado en {output_file}")


def main():
    query_inc = (
        'state=3^ORstate=2'
        '^location=f8dc277347ac3910d9d3a03a536d43e6'
        '^ORlocation=7d036756476c3110d9d3a03a536d4326'
        '^ORlocation=f5036756476c3110d9d3a03a536d4327'
        '^ORlocation=f3377b3e47f07d50d9d3a03a536d43d7'
        '^ORlocation=202daf7347ac3910d9d3a03a536d4329'
        '^ORlocation=f1036756476c3110d9d3a03a536d4326'
        '^ORlocation=79036756476c3110d9d3a03a536d4325'
        '^assignment_group=56068a6d1bf16410f720524f034bcbdf'
        '^ORassigned_to=0c49ca78478e2d54a8cae9e8536d437d')
    query_req = (
        'location=f8dc277347ac3910d9d3a03a536d43e6'
        '^ORlocation=79036756476c3110d9d3a03a536d4325'
        '^ORlocation=f5036756476c3110d9d3a03a536d4327'
        '^ORlocation=f3377b3e47f07d50d9d3a03a536d43d7'
        '^ORlocation=202daf7347ac3910d9d3a03a536d4329'
        '^ORlocation=7d036756476c3110d9d3a03a536d4326'
        '^ORlocation=f1036756476c3110d9d3a03a536d4326'
        '^ORlocation=e04d9a0f1be53510d5166392b24bcb78'
        '^assignment_group=56068a6d1bf16410f720524f034bcbdf'
        '^state=5'
        '^assigned_to=0c49ca78478e2d54a8cae9e8536d437d')
    params_inc = {
        'sysparm_query': query_inc,
        'sysparm_fields': ['number,'
                           'upon_reject,'
                           'sys_updated_on,'
                           'u_gbl_contadoe,'
                           'u_std_importance,'
                           'state,'
                           'sys_created_by,'
                           'knowledge,'
                           'impact,'
                           'active,'
                           'priority,'
                           'sys_domain_path,'
                           'business_duration,'
                           'u_assignment_group_count,'
                           'u_assigned_to_count,'
                           'short_description,'
                           'u_devuelto_por_remedy,'
                           'notify,'
                           'service_offering,'
                           'sys_class_name,'
                           'closed_by,'
                           'u_cancelado_por_usuario,'
                           'reopened_by'
                           'reassignment_count,'
                           'assigned_to,'
                           'u_agent_action,'
                           'u_integrado_con_cisco,'
                           'escalation,'
                           'upon_approval,'
                           'made_sla,'
                           'child_incidents,'
                           'task_effective_number,'
                           'u_origen,'
                           'resolved_by,'
                           'sys_updated_by,'
                           'opened_by,'
                           'sys_created_on,'
                           'u_gbl_service_string,'
                           'u_resuelto_por_remedy,'
                           'task_for,'
                           'calendar_stc,'
                           'closed_at,'
                           'opened_at,'
                           'caller_id,'
                           'reopened_time,'
                           'resolved_at,'
                           'subcategory,'
                           'u_std_fail_condition,'
                           'u_reaperturas,'
                           'close_code,'
                           'assignment_group,'
                           'business_stc,'
                           'description,'
                           'origin_id,'
                           'calendar_duration,'
                           'close_notes,'
                           'sys_id,'
                           'u_std_substate,'
                           'contact_type,'
                           'u_std_incident_type,'
                           'incident_state,'
                           'urgency,'
                           'company,'
                           'product,'
                           'severity,'
                           'approval,'
                           'sys_mod_count,'
                           'u_std_contect,'
                           'reopen_count,'
                           'location,'
                           'category'
],
        'sysparm_limit': 200
    }
    params_req = {
        'sysparm_query': query_req,
        'sysparm_fields': [],
        'sysparm_limit': 200
    }

    company = 'b482d6a91b66a8101df3bb7f034bcbf0'

    # Obtener registros de tablas
    incident_records = all_inc(query_inc,params_inc,'incident')
    req_item_records = all_req(query_req,params_req,'sc_req_item')
    #all_groups = groups_assignament('sys_user_group')
    #all_cat_groups = cat_groups('u_eus_cat_producto')
    #all_tables_meta = tables_meta('sys_db_object')
    all_ent_agendador = ent_agendador_records('u_ent_agendador',company)

    # Convertir registros obtenidos en dataframe
    incident_df= pd.DataFrame(incident_records)
    req_item_df = pd.DataFrame(req_item_records)
    #groups_df = pd.DataFrame(all_groups)
    #cat_products_df = pd.DataFrame(all_cat_groups)
    #tables_df = pd.DataFrame(all_tables_meta)
    ent_agendador_df = pd.DataFrame(all_ent_agendador)


    incident_df.rename(columns={
        'u_eus_product': 'product'}, inplace=True)
    req_item_df.rename(columns={
        'u_eus_cat_producto' : 'product'}, inplace=True)

    reporte_sentral = pd.concat([incident_df, req_item_df], ignore_index=True)

    dict_sheetname = {
        'Incidentes': incident_df,
        'Requerimientos': req_item_df,
        'Reporte-Sentral': reporte_sentral,
        #'Grupos': groups_df,
        #'Categoria productos': cat_products_df
        #'Tablas': tables_df,
        'WFM': ent_agendador_df
    }
    #Genera consolidado de INC y RITM
    save_to_excel(dict_sheetname)
main()