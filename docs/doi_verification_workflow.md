# DOI Verification Workflow

## Purpose

The DOI verification tool scans repository markdown files for citation-like rows and DOI strings, then generates markdown and CSV reports. It is designed to be reusable across repositories.

## Local Scan

Run a local scan without remote API calls:

```bash
python scripts/verify_dois.py docs
```

This detects:

- Existing DOI strings
- Markdown table rows that appear to contain sources
- Citation candidates that need manual DOI review

Default outputs:

```text
reports/generated/doi_verification_report.md
reports/generated/doi_verification_report.csv
```

## Remote Crossref Scan

Run with Crossref lookup:

```bash
python scripts/verify_dois.py docs --crossref
```

This queries Crossref for candidate bibliographic matches and records candidate DOI/title metadata.

## Cross-Repo Use

Copy these components into another repository:

```text
src/ml_lab/citations/doi_verifier.py
scripts/verify_dois.py
```

Then run:

```bash
python scripts/verify_dois.py docs
```

For a repo-independent future version, rename the package from `ml_lab.citations` to a neutral utility namespace such as `research_tools.citations`.

## Output Statuses

| Status | Meaning |
|---|---|
| `doi_present_unverified` | A DOI was detected locally, but metadata was not checked remotely. |
| `needs_doi_review` | No DOI was detected for a citation-like candidate. |
| `crossref_candidate_found` | Crossref returned a candidate match with a DOI. |
| `crossref_match_without_doi` | Crossref returned a record but no DOI was present. |
| `no_crossref_match` | Crossref returned no candidate match. |
| `crossref_error` | Remote lookup failed. |

## Review Rules

Remote matches should be treated as candidates, not final truth. Before adding a DOI to a manuscript:

1. Confirm title match.
2. Confirm author and year match.
3. Confirm publication venue.
4. Prefer the published version over a preprint when both exist.
5. Record the verified DOI in `docs/apa_sources.md`.

## Future Improvements

- Add OpenAlex fallback lookup.
- Add BibTeX export.
- Add confidence thresholds for automatic flagging.
- Add GitHub Action for citation checks.
- Generalize the package for all repositories.
