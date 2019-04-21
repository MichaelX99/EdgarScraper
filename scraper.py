import utils

url = "https://www.sec.gov/Archives/edgar/data/320193/000032019318000145/a10-k20189292018.htm"
fname = 'parsed.txt'
utils.parse_url(url, fname)
