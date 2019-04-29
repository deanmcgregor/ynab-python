SWAGGER GENERATION INSTRUCTIONS

1. Install swagger-codegen
1. Change into the ynab-python directory
1. Remove all the test files with `rm -r test/`
1. Bump the version in swagger-codegen-python-config.js
1. Generate new fixtures with `swagger-codegen generate -i https://api.youneedabudget.com/papi/spec-v1-swagger.json -l python -o . --config swagger-codegen-python-config.json --git-user-id deanmcgregor --git-repo-id ynab-python`
1. Manually fix up the tests to call `ynab.api` and `ynab.models` for imports
1. Install the test requirements with `pip install -r test-requirements.txt`
1. Run the tests with `nosetests`
