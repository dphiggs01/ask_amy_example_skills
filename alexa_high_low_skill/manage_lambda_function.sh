#!/usr/bin/env bash

# prior to using this bash script you must first configure the
# aws cli and set the region appropriately

#assume the current directory name is the name for the skill function
SKILL_NM=${PWD##*/}
SKILL_DIR=${PWD}

SKILL_ROLE=arn:aws:iam::280056172273:role/AlexaLambdaRole
SKILL_HANDLER=ask_amy.lambda_function.lambda_handler
SKILL_ZIP=alexa_skill.zip


function create_source_zip {
   #install ask_amy in local directory
   pip install ask_amy -t $SKILL_DIR/dist/
   cp *.py *.json $SKILL_DIR/dist/
	cd $SKILL_DIR/dist
   zip -r $SKILL_DIR/$SKILL_ZIP *
   cd -
}

function update_function {
  aws lambda update-function-code \
     --region us-east-1 \
     --function-name $SKILL_NM  \
     --zip-file fileb://$SKILL_ZIP \
     --profile adminuser
}

function create_function {
  aws lambda create-function \
     --function-name $SKILL_NM \
     --runtime python3.6 \
     --role $SKILL_ROLE \
     --handler $SKILL_HANDLER \
     --description $SKILL_NM \
     --timeout 3 \
     --memory-size 128 \
     --zip-file fileb://$SKILL_ZIP \
	> /dev/null
}

function add_trigger {
  aws lambda add-permission \
     --function-name $SKILL_NM \
     --statement-id "alexa_trigger" \
     --action "lambda:InvokeFunction" \
     --principal "alexa-appkit.amazon.com"
}  


#create the source zip file
create_source_zip

#attempt to update the lambda function
update_function

#if update fails assume you need to create the function
if [ "$?" != "0" ]; then
   echo '  '
	echo CREATING FUNCTION $SKILL_NM
   echo ' '
   create_function
   add_trigger
else
	echo UPDATING FUNCTION $SKILL_NM
fi
