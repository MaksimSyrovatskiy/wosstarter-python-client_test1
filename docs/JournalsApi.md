# clarivate.wos_starter.client.JournalsApi

All URIs are relative to *http://example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**journals_get**](JournalsApi.md#journals_get) | **GET** /journals | 
[**journals_uid_get**](JournalsApi.md#journals_uid_get) | **GET** /journals/{uid} | 


# **journals_get**
> JournalsList journals_get()



### Example


```python
import time
import clarivate.wos_starter.client
from clarivate.wos_starter.client.api import journals_api
from clarivate.wos_starter.client.model.journals_list import JournalsList
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = clarivate.wos_starter.client.Configuration(
    host = "http://example.com"
)


# Enter a context with an instance of the API client
with clarivate.wos_starter.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = journals_api.JournalsApi(api_client)
    issn = "issn_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.journals_get(issn=issn)
        pprint(api_response)
    except clarivate.wos_starter.client.ApiException as e:
        print("Exception when calling JournalsApi->journals_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issn** | **str**|  | [optional]

### Return type

[**JournalsList**](JournalsList.md)

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

# **journals_uid_get**
> Journal journals_uid_get(uid)



### Example


```python
import time
import clarivate.wos_starter.client
from clarivate.wos_starter.client.api import journals_api
from clarivate.wos_starter.client.model.journal import Journal
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = clarivate.wos_starter.client.Configuration(
    host = "http://example.com"
)


# Enter a context with an instance of the API client
with clarivate.wos_starter.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = journals_api.JournalsApi(api_client)
    uid = "uid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.journals_uid_get(uid)
        pprint(api_response)
    except clarivate.wos_starter.client.ApiException as e:
        print("Exception when calling JournalsApi->journals_uid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  |

### Return type

[**Journal**](Journal.md)

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

