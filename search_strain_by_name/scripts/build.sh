pip3 install -r ~/PycharmProjects/terp_lambda/requirements.txt \
		--target=output \

rm -rf function/
rm function.zip
pushd output && cp ../lambda_function.py ./lambda_function.py && cp ../../functions.py ./functions.py && zip -r ../function.zip .
#popd && cd .. && zip search_strain_by_name/function.zip ./functions.py search_strain_by_name/lambda_function.py
#zip search_strain_by_name/function.zip search_strain_by_name/lambda_function.py
#zip function.zip
