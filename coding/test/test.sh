#!/bin/bash

EXPECTED="1 Record inserted successfully into Inventory table"
bash import.sh capterra feed-products/capterra.yaml
RESULT=$?
if echo "$RESULT" | grep -q "$EXPECTED"; then
  echo "Test passed";
else
  echo "Test failed";
fi
