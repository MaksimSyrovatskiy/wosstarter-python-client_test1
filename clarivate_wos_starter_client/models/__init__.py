# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from clarivate_wos_starter_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from clarivate_wos_starter_client.model.document import Document
from clarivate_wos_starter_client.model.document_citations import DocumentCitations
from clarivate_wos_starter_client.model.document_identifiers import DocumentIdentifiers
from clarivate_wos_starter_client.model.document_keywords import DocumentKeywords
from clarivate_wos_starter_client.model.document_links import DocumentLinks
from clarivate_wos_starter_client.model.document_names import DocumentNames
from clarivate_wos_starter_client.model.document_names_authors import DocumentNamesAuthors
from clarivate_wos_starter_client.model.document_names_inventors import DocumentNamesInventors
from clarivate_wos_starter_client.model.document_source import DocumentSource
from clarivate_wos_starter_client.model.document_source_pages import DocumentSourcePages
from clarivate_wos_starter_client.model.documents_list import DocumentsList
from clarivate_wos_starter_client.model.journal import Journal
from clarivate_wos_starter_client.model.journal_links import JournalLinks
from clarivate_wos_starter_client.model.journals_list import JournalsList
from clarivate_wos_starter_client.model.metadata import Metadata
