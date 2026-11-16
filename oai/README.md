# Static OAI-PMH response snapshots

These files are **pre-rendered OAI-PMH 2.0 responses**, not a live OAI-PMH endpoint.
A static host cannot answer `?verb=...` requests; these snapshots are intended for
offline import into a repository, for metadata-harvest tooling that accepts XML files,
and for human verification.

| verb | file |
|---|---|
| Identify | `Identify.xml` |
| ListMetadataFormats | `ListMetadataFormats.xml` |
| ListSets | `ListSets.xml` |
| ListIdentifiers | `ListIdentifiers.xml` |
| ListRecords | `ListRecords.xml` |

Live harvesting of this work should instead use the DOI registries (DataCite, Zenodo,
Figshare) and the machine-readable files at the site root (`datacite.xml`,
`oai_dc.xml`, `dublincore.xml`, `marcxml.xml`, `mets.xml`, `ro-crate-metadata.json`).

This is an open preprint, CC BY 4.0, author author name Didgeridoo, not peer reviewed.
