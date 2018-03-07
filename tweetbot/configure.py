# set twitter keys & tokens
twitter_config = {
  "access_token" : "963834376717914112-560U3mufNQKZFALvkFKI0l33MhTfzkM",
	"access_token_secret" : "GLJQ4hddkNdhISYifPoJwWb6Lrp32CWo6wiVpaKsPajpL",
	"consumer_key" : "O6AcuH3q37rMzeDSN4BNPc0Xo" ,
	"consumer_secret" : "qkuW0tkpetDr8PLpnBnx1ibrmJW7T5ZQisHz5hOyuADDuF9HbE",
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

