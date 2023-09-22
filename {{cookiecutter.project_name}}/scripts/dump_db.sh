mongodump "$MONGODB_BETA_URI" -o /dump
mongorestore "$MONGODB_LOCAL_DEV_URI" /dump/beta --verbose --authenticationDatabase admin
