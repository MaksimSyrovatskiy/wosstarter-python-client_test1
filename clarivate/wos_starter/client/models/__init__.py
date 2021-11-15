# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from clarivate.wos_starter.client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from clarivate.wos_starter.client.model.document import Document
from clarivate.wos_starter.client.model.document_citations import DocumentCitations
from clarivate.wos_starter.client.model.document_identifiers import DocumentIdentifiers
from clarivate.wos_starter.client.model.document_keywords import DocumentKeywords
from clarivate.wos_starter.client.model.document_links import DocumentLinks
from clarivate.wos_starter.client.model.document_names import DocumentNames
from clarivate.wos_starter.client.model.document_names_authors import DocumentNamesAuthors
from clarivate.wos_starter.client.model.document_names_inventors import DocumentNamesInventors
from clarivate.wos_starter.client.model.document_source import DocumentSource
from clarivate.wos_starter.client.model.document_source_pages import DocumentSourcePages
from clarivate.wos_starter.client.model.documents_list import DocumentsList
from clarivate.wos_starter.client.model.journal import Journal
from clarivate.wos_starter.client.model.journal_links import JournalLinks
from clarivate.wos_starter.client.model.journals_list import JournalsList
from clarivate.wos_starter.client.model.metadata import Metadata
