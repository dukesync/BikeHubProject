base_path = "/Volumes/bike_data/bronze/source_system"

ingestion_config = [
    # crm
    {
        "source": "crm",
        "path": f"{base_path}/source_crm/cust_info.csv",
        "table": "cust_info_raw"
    },
    {
        "source": "crm",
        "path": f"{base_path}/source_crm/prd_info.csv",
        "table": "prd_info_raw"
    },
    {
        "source": "crm",
        "path": f"{base_path}/source_crm/sales_details.csv",
        "table": "sales_details_raw"
    },
    # erp
    {
        "source": "erp",
        "path": f"{base_path}/source_erp/CUST_AZ12.csv",
        "table": "cust_az12_raw"
    },
    {
        "source": "erp",
        "path": f"{base_path}/source_erp/LOC_A101.csv",
        "table": "loc_a101_raw"
    },
    {
        "source": "erp",
        "path": f"{base_path}/source_erp/PX_CAT_G1V2.csv",
        "table": "px_cat_g1v2_raw"
    },
]
