# clarivate.wos_starter.client.DocumentsApi

All URIs are relative to *http://example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documents_get**](DocumentsApi.md#documents_get) | **GET** /documents | Query Web of Science documents 
[**documents_uid_get**](DocumentsApi.md#documents_uid_get) | **GET** /documents/{uid} | 


# **documents_get**
> DocumentsList documents_get(q)

Query Web of Science documents 

TODO 

### Example


```python
import time
import clarivate.wos_starter.client
from clarivate.wos_starter.client.api import documents_api
from clarivate.wos_starter.client.model.documents_list import DocumentsList
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = clarivate.wos_starter.client.Configuration(
    host = "http://example.com"
)


# Enter a context with an instance of the API client
with clarivate.wos_starter.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    q = "q_example" # str | 
    db = "db_example" # str |  (optional)
    page = 1 # int |  (optional)
    limit = 1 # int |  (optional)
    sort_field = "sortField_example" # str | Order by field(s). Field name and order by clause separated by '+', use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. Supported fields:  * **LD** - Load Date * **PY** - Publication Year * **RS** - Relevance * **TS** - Times Cited  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Query Web of Science documents 
        api_response = api_instance.documents_get(q)
        pprint(api_response)
    except clarivate.wos_starter.client.ApiException as e:
        print("Exception when calling DocumentsApi->documents_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Query Web of Science documents 
        api_response = api_instance.documents_get(q, db=db, page=page, limit=limit, sort_field=sort_field)
        pprint(api_response)
    except clarivate.wos_starter.client.ApiException as e:
        print("Exception when calling DocumentsApi->documents_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  |
 **db** | **str**|  | [optional]
 **page** | **int**|  | [optional]
 **limit** | **int**|  | [optional]
 **sort_field** | **str**| Order by field(s). Field name and order by clause separated by &#39;+&#39;, use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. Supported fields:  * **LD** - Load Date * **PY** - Publication Year * **RS** - Relevance * **TS** - Times Cited  | [optional]

### Return type

[**DocumentsList**](DocumentsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_uid_get**
> Document documents_uid_get(uid)



### Example


```python
import time
import clarivate.wos_starter.client
from clarivate.wos_starter.client.api import documents_api
from clarivate.wos_starter.client.model.document import Document
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = clarivate.wos_starter.client.Configuration(
    host = "http://example.com"
)


# Enter a context with an instance of the API client
with clarivate.wos_starter.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    uid = "uid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.documents_uid_get(uid)
        pprint(api_response)
    except clarivate.wos_starter.client.ApiException as e:
        print("Exception when calling DocumentsApi->documents_uid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  |

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

