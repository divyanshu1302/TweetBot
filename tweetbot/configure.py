# set twitter keys & tokens
twitter_config = {
  "access_token" : "",
	"access_token_secret" : "",
	"consumer_key" : "" ,
	"consumer_secret" : "",
}

es_mappings = {
    "tweet_index": {
        "mappings": {
            "tweet": {
                "properties": {
                    "timestamp_ms": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "hashtags": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "created_at": {
                      "type": "datetime",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "datetime"
                        }
                      }
                    },
                    "screen_name": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "user_name": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "location": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "source_device": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "country": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "country_code": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "tweet_text": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "lang": {
                  "type": "string",
                  "fields": {
                    "raw": {
                      "index": "not_analyzed",
                      "type": "string"
                    }
                  }
                }
                }
            }
        }
    }

}

