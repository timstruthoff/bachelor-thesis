# Import as Dataframe
jiraImport = pd.read_csv(PM_CSV_PATH, parse_dates=[PM_DATE_COLUMN])
# jiraImportFiltered = jiraImport[jiraImport[PM_STORYPOINT_COLUMN].notnull() jiraImport['Story Points'].notnull()]
jiraImportFiltered = jiraImport[jiraImport[PM_DATE_COLUMN].notnull()]

jiraImportFiltered.info()
jiraImportFiltered