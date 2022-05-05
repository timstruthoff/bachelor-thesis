codeAnalysisInput = pd.read_csv(CODE_CSV_PATH, parse_dates=['timestamp'])
codeAnalysisInput['timestamp'] = pd.to_datetime(codeAnalysisInput.timestamp, utc=True)

codeAnalysisInput.info()
codeAnalysisInput.head()