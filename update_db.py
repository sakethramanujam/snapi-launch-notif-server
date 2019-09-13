#! /usr/bin/env python
import asyncio
from helpers import notifications, db
import os
import logging

logging.basicConfig(level=logging.DEBUG)

async def update_db(collection: object, article: dict):
    id = article['id']
    collection = db.connect()
    try:
        obj_id = collection.find_one_and_update(filter={'id': id},
                                                update={"$set": article},
                                                upsert=True)
    except Exception:
        print(f"Failed to add article {id}")


async def add_articles_to_db():
    collection = db.connect()
    api_articles = notifications.get_articles('https://spacelaunchnow.me/api/3.3.0/launch/upcoming?limit=5')
    articles = [notifications._generate_doc(article) for article in api_articles]
    for article in articles:
        await update_db(collection, article)


async def main():
    await asyncio.gather(add_articles_to_db())


if __name__ == "__main__":
    asyncio.run(main())
