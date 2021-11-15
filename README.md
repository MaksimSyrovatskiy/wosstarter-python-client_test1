# clarivate-wos-starter-python-client
The Web of Science™ Starter API provides basic metadata and search functionality for Web of Science™ Documents and Journals. Based on your subscription, this API can return times cited of documents.

## Resouces
This API follows the REST approach to disclose resources in URL format. Only the GET method is currently available to perform requests over HTTP.

The API is available on the [Clarivate Developer Portal](https://developer.clarivate.com/apis/wos-starter). You can find more details about the subscription and the Plans.

## Content

You can learn more about content at [Web of Science™ Product Page](https://clarivate.com/webofsciencegroup/solutions/web-of-science/) or in the [Web of Science™ Help](https://webofscience.help.clarivate.com/en-us/Content/home.htm).

(TODO: Add list of fields that are returned from this API.)

## Credentials

All requests require authentication with an API Key authentication flow. For more details, check the [Guide][https://developer.clarivate.com/help/api-access#key_access].


## API Client Libraries
TBD

## Search and field tags for Web of Science documents
Web of Science™ offers [advanced search query builder](https://webofscience.help.clarivate.com/en-us/Content/advanced-search.html). This API does not support all field tags for documents. [Web of Science API Expanded](https://developer.clarivate.com/apis/wos) offers all available field tags. The following table lists the field tags that are supported by this API.
| Field Tag | Description                                                                                                                                                 |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TI        | Title of document                                                                                                                                           |
| IS        | ISSN or ISBN                                                                                                                                                |
| SO        | Source title - The result contains all source titles within product database (for example, journal titles and/or book titles if the product includes books) |
| VL        | Volume                                                                                                                                                      |
| PG        | Page                                                                                                                                                        |
| CS        | Issue                                                                                                                                                       |
| PY        | Year Published                                                                                                                                              |
| AU        | Author                                                                                                                                                      |
| UT        | Accession Number                                                                                                                                            |
| DO        | DOI                                                                                                                                                         |
| PMID      | PubMed ID                                                                                                                                                   |
| OG        | Search for preferred organization names and/or their name variants from the Preferred Organization Index. <p> A search on a preferred organization name returns all records that contain the preferred name and all records that contain its name variants. A search on a name variant returns all records that contain the variant. For example, Cornell Law Sch returns all records that contain Cornell Law Sch in the Addresses field. <p> When searching for organization names that contain a Boolean (AND, NOT, NEAR, and SAME), always enclose the word in quotation marks ( \" \" ). For example: <p>   - OG=(Japan Science \"and\" Technology Agency (JST))      <br>   - OG=(\"Near\" East Univ)         <br> - OG=(\"OR\" Hlth Sci Univ)                           |
| TS        | Searches for topic terms in the following fields within a document: <p> - Title <br> - Abstract <br> - Author keywords <br> - Keywords Plus

## Pagination
To ensure fast response time, each search or multiple entity calls (such as `/documents`) retrieve only a certain number of hits/records.

There are two optional request parameters to browse along with the result&#58; _limit_ and _page_.

- limit&#58; Number of returned results, ranging from 0 to 50 (default **10**)
- page&#58; Specifying a page to retrieve (default **1**)

Moreover, this information is shown in the response body, in the tag **metadata**&#58;

```json
\"metadata\": {
  \"total\": 91,
  \"page\": 1,
  \"limit\": 10
}
```

## Errors
The WoS Journals API uses conventional HTTP success or failure status codes. For errors, some extra information is included to indicate what went wrong in the JSON response. The list of HTTP codes is listed below.

| Code  | Title  | Description |
|---|---|---|
| 400  | Bad request  | Request syntax error |
| 401  | Unauthorized  | The API key is invalid or missed |
| 404  | Not found  | The resource is not found |
| 405 | Method not allowed | Method other than GET is not allowed |
| 50X  | Server errors  | Technical error with servers|
Each error response (except `401 Unauthorized` error) contains the code of the error, the title of the error and detailed description of the error: a misprint in an endpoint, wrong URL parameter, etc. The example of the error message is shown below:

```json
  \"error\": {
    \"status\": 404,
    \"title\": \"Resource couldn't be found\",
    \"details\": \"There is no record found in the Web of Science database. Please check your query.\"
  }
```
For the `401 Unauthorized` error the response body is a little bit different:
```json
{
  \"error_description\": \"The access token is missing\",
  \"error\": \"invalid_request\"
}


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import clarivate.wos_starter.client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import clarivate.wos_starter.client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import clarivate.wos_starter.client
from pprint import pprint
from clarivate.wos_starter.client.api import documents_api
from clarivate.wos_starter.client.model.document import Document
from clarivate.wos_starter.client.model.documents_list import DocumentsList
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = clarivate.wos_starter.client.Configuration(
    host = "http://example.com"
)



# Enter a context with an instance of the API client
with clarivate.wos_starter.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    q = "q_example" # str | 
db = "db_example" # str |  (optional)
page = 1 # int |  (optional)
limit = 1 # int |  (optional)
sort_field = "sortField_example" # str | Order by field(s). Field name and order by clause separated by '+', use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. Supported fields:  * **LD** - Load Date * **PY** - Publication Year * **RS** - Relevance * **TS** - Times Cited  (optional)

    try:
        # Query Web of Science documents 
        api_response = api_instance.documents_get(q, db=db, page=page, limit=limit, sort_field=sort_field)
        pprint(api_response)
    except clarivate.wos_starter.client.ApiException as e:
        print("Exception when calling DocumentsApi->documents_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://example.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DocumentsApi* | [**documents_get**](docs/DocumentsApi.md#documents_get) | **GET** /documents | Query Web of Science documents 
*DocumentsApi* | [**documents_uid_get**](docs/DocumentsApi.md#documents_uid_get) | **GET** /documents/{uid} | 
*JournalsApi* | [**journals_get**](docs/JournalsApi.md#journals_get) | **GET** /journals | 
*JournalsApi* | [**journals_uid_get**](docs/JournalsApi.md#journals_uid_get) | **GET** /journals/{uid} | 


## Documentation For Models

 - [Document](docs/Document.md)
 - [DocumentCitations](docs/DocumentCitations.md)
 - [DocumentIdentifiers](docs/DocumentIdentifiers.md)
 - [DocumentKeywords](docs/DocumentKeywords.md)
 - [DocumentLinks](docs/DocumentLinks.md)
 - [DocumentNames](docs/DocumentNames.md)
 - [DocumentNamesAuthors](docs/DocumentNamesAuthors.md)
 - [DocumentNamesInventors](docs/DocumentNamesInventors.md)
 - [DocumentSource](docs/DocumentSource.md)
 - [DocumentSourcePages](docs/DocumentSourcePages.md)
 - [DocumentsList](docs/DocumentsList.md)
 - [Journal](docs/Journal.md)
 - [JournalLinks](docs/JournalLinks.md)
 - [JournalsList](docs/JournalsList.md)
 - [Metadata](docs/Metadata.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in clarivate.wos_starter.client.apis and clarivate.wos_starter.client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from clarivate.wos_starter.client.api.default_api import DefaultApi`
- `from clarivate.wos_starter.client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import clarivate.wos_starter.client
from clarivate.wos_starter.client.apis import *
from clarivate.wos_starter.client.models import *
```

