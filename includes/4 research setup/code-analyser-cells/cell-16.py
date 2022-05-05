pmData = jiraImportPreselected[[PM_STORYPOINT_COLUMN]].copy()
pmData = pmData.set_index(pd.DatetimeIndex(jiraImportPreselected[PM_DATE_COLUMN]))
pmData = pmData.tz_convert('UTC')
pmData = pmData.rename(columns={PM_STORYPOINT_COLUMN: 'storypoints', PM_ISSUE_COLUMN: 'issue'})
pmData = pmData.sort_index(ascending=True)
pmData
