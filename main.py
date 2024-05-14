from bot import Bot, APP_ID, API_HASH

Bot().run()

owner_client = Client("owner_session", api_id=APP_ID, api_hash=API_HASH)


owner_client.start()
owner_client.run()
