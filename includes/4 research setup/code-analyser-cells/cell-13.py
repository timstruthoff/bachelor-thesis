jiraImport = pd.read_csv(PM_CSV_PATH, parse_dates=[PM_DATE_COLUMN])
jiraImportFiltered = jiraImport[jiraImport[PM_DATE_COLUMN].notnull()]