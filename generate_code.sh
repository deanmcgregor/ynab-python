#! /bin/bash

# Remove all of the test files because swagger-codegen does not regenerate them if they exist
rm -rf test/* 

# Generate the code
swagger-codegen generate -i ynab-swagger-api-spec-v1.json -l python -o . --config swagger-codegen-python-config.json --git-user-id deanmcgregor --git-repo-id ynab-python

# Fix the models module path
git grep -lz test | xargs -0 sed -i '' 's/from models\./from ynab\.models\./g'

# Fix the api module path
git grep -lz test | xargs -0 sed -i '' 's/from api\./from ynab\.api\./g'

# Fix the api function call path
git grep -lz test | xargs -0 sed -i '' 's/self\.api = api\./self\.api = ynab\.api\./g'

git ls-files -z ynab/models | xargs -0 perl -i -p0e 's/\s+if \w+ is None:\n\s+raise ValueError.*//g'

# Run the tests
nosetests
