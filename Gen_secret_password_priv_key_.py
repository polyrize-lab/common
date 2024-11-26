DEBUG = False

CORE_URL = 'http://core.test.team/api/1.0'
DB_PASSWORD = 'pi0neer1'

REDIS_HOST = 'localhost'
REDIS_PORT = 6738
REDIS_DB = 1
REDIS_PASSWORD = ''

SESSIONS_DB_HOST = '10.107.152.128'
SESSIONS_DB_PORT = 2684
SESSIONS_DB_NO = 1
SESSIONS_DB_PASSWORD = 'leoktjec4YSg!'

#GA
GA_ENABLED = True
GA_IDS = 'ga:9487650'
GA_SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
GA_VIEW_ID = '718026937'
GA_SERVICE_ACCOUNT_CREDENTIALS = {'type': 'service_account',
 'project_id': 'analytics-122905',
 'private_key_id': '039638d091e41e0b323607a56cf110dc872df7d9',
 'private_key': '-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC6L8sNL4FMXUGA\n7tej3sT39k5+UfBD24oKAKxrsbG6pqy8/6NJ/2OQ5e+kB+h2KPuO3B59SfFcyBBd\ns/E31jp3QkpyHhNyoFSW5LVwoNwrp7Ejl1U4/W0r1KcYbP5CeifXynPcq/lTYV3A\nSSIXKxRdLIyj6KmS/g9B23z1ENIaa9R0I4e8jNKmCdLwhF13s9RyPZwm/RVg7BAh\nqyjbxiRyHfVZ/ZAwnzbIv5BKQbUJVX+sHxFT676ukbUG5aOa/oJFpNndtci8m7jD\njxXgpx+0Mp/qPNErAytowhxEvUckI3ltNuPLyBw3vtkgoizqBozfO0w+SxztYMtQ\nmqiFFvy/AgMBAAECggEAEckE+CfQxdFsCMPyp2hdSmPQkFzMt86zO0y11mfCrCtw\nbsbAs2Mzq0tmU8fIye4U8aBHQqfwksYDAjXGghNIbHdRozVRmlPZy2biNMsOR8FI\n8O7WKOZ/KjkEMSe1i2Z+KK+h17Tke+QzehhtADzmP2xFAayfnjdUqnGBWJZDFluI\nLsHma0+GF3LfUuGZp7BitPBMviazMlteDDQ8BNPzbgY28n+MtVq4ah8vkd4xVNAr\nEr3zYnayyiNSXZpCSsWSrGfduUKudrmCv/B07rsnnCuImA117r0NWKr5WjF4nAlv\nISmC2B3YWUWa0tA7EE1yi7dEguR0FbeEpVvV99S0iQKBgQDcE+YOPzHbT26jMFYQ\nCqhVw+Ndq/1G8oVOfuErnHEWNCHDhhhs3mu8JlzZJ9Q/6sis2cypDnQPYlhhhU+q\n5q57wK5SxD+++bNIgXos3KqQKv0nsZbWdXfWu2PjZg+5GxHxMjvKAx0OQnYr1bNQ\n2C4Nd04lyv/VUw3aWAVaGGGlGwKBgQDYk7vhHbJdMFGaaHvCCgrycqK+5DJ/q5El\nL3z60Y0RUt5RLTmBEGNANJ6YLT8aya2OQygbE6u6/Gy4kWmz9oXcz112VBIRSFdD\nxqxy85lJisw8Yqf/TuetCyKEt+fSJ6506x58avuX8Bso6Cz6728twDUAocpHXThA\nQLYaMQFVLQKBgQCuAG2cRgq9QwhOriDdfg+p/778iMcwGP+dGGQffwlKbN1lIdid\n+x1jHVG7v+nov1D6mRlfcLYCk9cdA7IBhXHfFnC9r7xW2kYNxZE7dxzD77lIcPi5\nhxbBCFfpqwAzclu1P+pVxjBq3dFgxw2HleSTcQiwiNfNamVBhOZ2XWCWkQKBgAWo\nVlAbJn2otXkDIbh/6qlKtVWnQGp1YOVHyEwFDVpWf9g/BjGI7A7RURNIm01n11DQ\nEEwkx2erEGwB4HEDD5wlDpv4tkAdU6pBll+qXWa+aXdqXFkfBo5OrCgrZbLntnb3\nbWRypv/hFdSLvCESACWBz+CkWVRj6wRCrH8iqJZBAoGBANZF5GnfcNK01N/S82ir\n4xrkgrVxVOcSYRIwnk8/KDNoIJ9L9b2QLWwOsttJaTQM94SDsSCUh9a3iLu4tJpU\nfPvRHlHY8LQSKsS1pUxfCXH2KX6qsbIdNZXjuTmuY7vH/fLy7208gNcvS8Ni5KIU\nuvNK3dzKPYEG+jhRNc4U8kBP\n-----END PRIVATE KEY-----\n',
 'client_email': 'eng-503@demo-322618.iam.jservicedepartment.com',
 'client_id': '104387306449547291825',
 'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
 'token_uri': 'https://accounts.google.com/o/oauth2/token',
 'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
 'client_x509_cert_url': 'https://www.googleapis.com/robot/v1/metadata/x509/eng-503%demo-322618.iam.jservicedepartment.com'}


# RSS Feed
class FEED:
    DOMAIN = "https://scroll.in"
    TITLE = "Scroll.in"
    DESCRIPTION = "Onion Soup."
    LANG = "en"
    NEWS_SERIES = [0, 1, 2, 3, 5, 7, 8, 9, 11]
    GA_ID = 'VB-34525689-1'
    INCLUDE_GOOGLE_TRENDING = True


# Instant Articles
class IA:
    GA_ID = 'VC-5837326461-1'
    SERIES_IDS = [0, 2, 3, 5, 7, 8, 9, 11]
    # SERIES_IDS = [1]
    TITLE = "Scroll.in Instant Articles"

    # Facebook Audience Network Ads
    FB_ADS_ENABLED = True
    FB_ADS = {
        'ID': '1954246761694972_1943247539262231',
        'DENSITY': 'default'
    }


# Monday APIs
MONDAY_API_KEY = 'MSUBW7fRH6lWPKAZSy5br74yQ5LFeb0lrsfUa6UIfBA'
MONDAY_URL = 'https://c.scroll.in'
MONDAY_ADMIN_URL = 'https://monday.news.team'
COMMENTS_ENABLED = True

# For emailing article
ARTICLE_EMAIL_SENDER = 'donotreply@scroll.in'
ARTICLE_EMAIL_SUBJECT_SUFFIX = ' | Scroll.in'

