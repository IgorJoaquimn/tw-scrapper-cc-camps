import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level

set_log_level("DEBUG")
async def main():
    proxy = "https://104.248.98.31:3128"
    proxy = "http://200.174.198.86:8888"
    
    api = API(proxy=proxy)  # or API("path-to.db") - default is `accounts.db`

    # NOTE 1: gather is a helper function to receive all data as list, FOR can be used as well:
    async for tweet in api.search("elon musk",limit = 5):
        print(tweet.id, tweet.user.username, tweet.rawContent)  # tweet is `Tweet` object

if __name__ == "__main__":
    asyncio.run(main())
