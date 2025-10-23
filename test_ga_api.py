import os
import pandas as pd
import itertools

property_id = "510027342"
starting_date = "8daysAgo"
ending_date = "yesterday"

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'my-project-saleh-18dd914e9923.json'


from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
client = BetaAnalyticsDataClient()

request_api = RunReportRequest(
    property=f"properties/{property_id}",
    dimensions=[
        Dimension(name="landingPagePlusQueryString")
        ],
        metrics=[
            Metric(name="sessions")
        ],
        date_ranges=[DateRange(start_date=starting_date, end_date=ending_date)],
    )
response = client.run_report(request_api)

print(response)