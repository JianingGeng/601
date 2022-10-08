# follow the instruction on https://cloud.google.com/healthcare-api/docs

def create_dataset(project_id, location, dataset_id):
    
    # Imports the Google API Discovery Service.
    from googleapiclient import discovery

    api_version = "v1"
    service_name = "healthcare"
    client = discovery.build(service_name, api_version)

    
    project_id = 'my-project'  # replace with your GCP project ID
    location = 'us-central1'  # replace with the dataset's location
    dataset_id = 'my-dataset'  # replace with your dataset ID
    dataset_parent = "projects/{}/locations/{}".format(project_id, location)

    request = (
        client.projects()
        .locations()
        .datasets()
        .create(parent=dataset_parent, body={}, datasetId=dataset_id)
    )

    response = request.execute()
    print("Created dataset: {}".format(dataset_id))
    return response


def create_dicom_store(project_id, location, dataset_id, dicom_store_id):
    
    # Imports the Google API Discovery Service.
    from googleapiclient import discovery

    api_version = "v1"
    service_name = "healthcare"
   
    client = discovery.build(service_name, api_version)

    # TODO(developer): Uncomment these lines and replace with your values.
    project_id = 'my-project'  # replace with your GCP project ID
    location = 'us-central1'  # replace with the parent dataset's location
    dataset_id = 'my-dataset'  # replace with the DICOM store's parent dataset ID
    dicom_store_id = 'my-dicom-store'  # replace with the DICOM store's ID
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, location, dataset_id
    )

    request = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .create(parent=dicom_store_parent, body={}, dicomStoreId=dicom_store_id)
    )

    response = request.execute()
    print("Created DICOM store: {}".format(dicom_store_id))
    return response

def create_fhir_store(project_id, location, dataset_id, fhir_store_id, version):
   
    # Imports the Google API Discovery Service.
    from googleapiclient import discovery

    api_version = "v1"
    service_name = "healthcare"
   
    client = discovery.build(service_name, api_version)

    #TODO(developer): Uncomment these lines and replace with your values.
    project_id = 'my-project'  # replace with your GCP project ID
    location = 'us-central1'  # replace with the parent dataset's location
    dataset_id = 'my-dataset'  # replace with the FHIR store's parent dataset ID
    fhir_store_id = 'my-fhir-store'  # replace with the FHIR store's ID
    version = 'R4'  # replace with the FHIR store version
    fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, location, dataset_id
    )

    body = {"version": version}

    request = (
        client.projects()
        .locations()
        .datasets()
        .fhirStores()
        .create(parent=fhir_store_parent, body=body, fhirStoreId=fhir_store_id)
    )

    response = request.execute()
    print("Created FHIR store: {}".format(fhir_store_id))

    return response

def create_hl7v2_store(project_id, location, dataset_id, hl7v2_store_id):
   
    # Imports the Google API Discovery Service.
    from googleapiclient import discovery

    api_version = "v1"
    service_name = "healthcare"
    
    client = discovery.build(service_name, api_version)

    # TODO(developer): Uncomment these lines and replace with your values.
    project_id = 'my-project'  # replace with your GCP project ID
    location = 'us-central1'  # replace with the parent dataset's location
    dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset ID
    hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
    hl7v2_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, location, dataset_id
    )

    request = (
        client.projects()
        .locations()
        .datasets()
        .hl7V2Stores()
        .create(parent=hl7v2_store_parent, body={}, hl7V2StoreId=hl7v2_store_id)
    )

    response = request.execute()
    print("Created HL7v2 store: {}".format(hl7v2_store_id))
    return response

