# DOI Verification Pipeline

## Purpose

The DOI verification pipeline turns citation checking into a repeatable repository workflow. It scans markdown files, detects citation candidates, checks DOI coverage, writes reports, and can enforce configurable pass/fail rules in CI.

## Configuration

The pipeline is controlled by:

```text
citation_pipeline.json
```

Default configuration:

```json
{
  "scan_paths": ["docs"],
  "outputs": {
    "markdown": "reports/generated/doi_verification_report.md",
    "csv": "reports/generated/doi_verification_report.csv",
    "summary_json": "reports/generated/doi_verification_summary.json"
  },
  "policy": {
    "allow_missing_doi": true,
    "allow_crossref_errors": true,
    "fail_on_unverified_existing_doi": false,
    "max_missing_doi_candidates": null
  },
  "remote": {
    "use_crossref": false
  }
}
```

## Local Run

```bash
python scripts/run_doi_pipeline.py --config citation_pipeline.json
```

Strict mode exits with a nonzero code when the configured policy fails:

```bash
python scripts/run_doi_pipeline.py --config citation_pipeline.json --strict
```

## Reports

The pipeline writes:

```text
reports/generated/doi_verification_report.md
reports/generated/doi_verification_report.csv
reports/generated/doi_verification_summary.json
```

## CI Workflow

The GitHub Actions workflow lives at:

```text
.github/workflows/doi-verification.yml
```

It runs on:

- Push to main
- Pull request to main
- Manual workflow dispatch

The default CI configuration is intentionally permissive because the current citation table is still being built. Tighten the policy when the bibliography is ready.

## Tightening Policy

For draft development:

```json
"allow_missing_doi": true
```

For pre-submission review:

```json
"allow_missing_doi": false
```

For a limited tolerance policy:

```json
"max_missing_doi_candidates": 3
```

## Crossref Mode

Remote Crossref lookup is available through the older verifier CLI:

```bash
python scripts/verify_dois.py docs --crossref
```

The configurable pipeline currently defaults to local scanning so CI does not depend on network lookups. Crossref can be enabled in `citation_pipeline.json` by setting:

```json
"remote": {
  "use_crossref": true
}
```

Remote matches must be treated as candidates. Confirm author, title, year, and venue before adding a DOI to the manuscript.

## Reusing Across Repositories

Minimum files to copy:

```text
citation_pipeline.json
src/ml_lab/citations/doi_verifier.py
src/ml_lab/citations/doi_pipeline.py
scripts/run_doi_pipeline.py
scripts/verify_dois.py
.github/workflows/doi-verification.yml
```

For a general research-tool package, rename the Python namespace from `ml_lab.citations` to something neutral such as `research_tools.citations`.
