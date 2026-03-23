# Contributing migrations

If you have a migration script you'd like to share, please submit a pull request to this repository! Your script should be placed in a subdirectory under `src/bunji/migrations/` and also update this `MIGRATION.md` file with instructions on how to migrate.

**IMPORTANT**: Running migrations on an existing Bunji database may have unexpected results. Always backup your Bunji database before running the migration.

# Actual Budget to Bunji Migration

Migrate data from Actual Budget (https://actualbudget.com/) to Bunji. It transfers your accounts, categories, and transactions while preserving their relationships and attributes.

## Rules

- Transactions without categories in Actual Budget will be assigned to an "Uncategorized" category in Bunji
- The script converts all amounts from cents (Actual Budget) to dollars (Bunji)

## Steps to Migrate

1. Export Your Actual Budget Data:

- Open Actual Budget
- Navigate to More → Settings → Export Data
- Save and extract the zip file
- Locate the `db.sqlite` file in the extracted contents

2. Run the Migration:

```bash
bunji --migrate actualbudget --source "path/to/actualbudget/db.sqlite"
```
