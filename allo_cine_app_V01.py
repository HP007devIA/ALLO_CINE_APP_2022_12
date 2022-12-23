from app import db_set

TEST_CONFIG_JSON = False

if __name__ == "__main__":
    if(TEST_CONFIG_JSON):
        config = db.get_db("config.json")
        print(config)

    print(__name__)
    app.run(debug = True)
