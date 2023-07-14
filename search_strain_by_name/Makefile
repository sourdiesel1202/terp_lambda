export LAMBDA_NAME=search_strain_by_name
export LAMBDA_REGION=us-west-2

.DEFAULT_GOAL := all
create:

	/bin/sh ./scripts/create.sh

build:

	/bin/sh ./scripts/build.sh

deploy:

	/bin/sh ./scripts/build.sh

run:
	/bin/sh ./scripts/run.sh

all:
	make build
	make deploy
	make run